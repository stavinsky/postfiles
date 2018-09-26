from multiprocessing import current_process, Process, pool, Event
from exceptions import GracefulExit
import signal # noqa
from file_reader import get_files_list, get_line
from db import Serializer
from datetime import datetime


shutdown_event = None


def terminate_handler(signum, frame):
    shutdown_event.set()
    if current_process().name == 'MainProcess':
        return
    raise GracefulExit()


class StoppableProcess(Process):
    def run(self):
        try:
            super().run()
        except GracefulExit:
            print("graceful exit")


class StoppablePool(pool.Pool):
    Process = StoppableProcess


def process_file(args):
    f, offset = args
    new_offset = offset
    new_mtime = 0

    if shutdown_event.is_set():
        return f["name"], new_mtime, new_offset

    try:
        for line, offset in get_line(
                f["name"], offset=db.get_offset(f["name"]), sep=b'\n'):
            new_offset = offset
        new_mtime = datetime.now().timestamp()

    except GracefulExit:
        pass
    return f["name"], new_mtime, new_offset


if __name__ == "__main__":
    signal.signal(
        signal.SIGINT, terminate_handler)
    data = dict()
    shutdown_event = Event()
    db = Serializer("test_db.json")
    db.load()

    while True:
        files = list()
        for f in get_files_list("tests/test_files/", r"file\d.txt"):
            if f["mtime"] > db.get_access_time(f["name"]):
                files.append((f, db.get_offset(f["name"])))
        with StoppablePool(1) as p:
            processed_files = p.map(process_file, files)
        for name, mtime, offset in processed_files:
            db.set_access_time(name, mtime)
            db.set_offset(name, offset)
        db.save()
        break
