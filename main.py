import signal
from contrib.reader import get_files_list
from contrib.db import Serializer
from contrib.pool import (
    StoppablePool, terminate_handler)
from contrib.process import process_file


def main_loop(run_once=False):
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
        if run_once:
            break


if __name__ == "__main__":
    signal.signal(
        signal.SIGINT, terminate_handler)
    main_loop(run_once=True)
