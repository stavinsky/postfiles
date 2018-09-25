from multiprocessing import current_process, Process, pool, Event
import time
from exceptions import GracefulExit
import signal


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


def test_func(val):
    if shutdown_event.is_set():
        return val, 0
    i = 0
    try:
        while True:
            time.sleep(0.1)
            i += 1
    except GracefulExit:
        pass
    return val, i


if __name__ == "__main__":
    signal.signal(
            signal.SIGINT, terminate_handler)
    data = dict()
    shutdown_event = Event()

    with StoppablePool(5) as p:
        r = p.map(test_func, range(100))
        for k, v in r:
            data[k] = v
    print(data)
