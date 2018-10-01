from contrib.exceptions import GracefulExit
from multiprocessing import (
    Process, current_process, pool)
from contrib.event import shutdown_event


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
            pass


class StoppablePool(pool.Pool):
    Process = StoppableProcess
