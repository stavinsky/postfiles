from contrib.exceptions import GracefulExit
from contrib.event import shutdown_event
from contrib.reader import get_line
from datetime import datetime


def process_file(args):
    f, offset = args
    new_offset = offset
    new_mtime = 0

    if shutdown_event.is_set():
        return f["name"], new_mtime, new_offset

    try:
        for line, offset in get_line(
                f["name"], offset=offset, sep=b'\n'):
            new_offset = offset
            print(line)
            import time
            time.sleep(1)
        new_mtime = datetime.now().timestamp()

    except GracefulExit:
        pass
    return f["name"], new_mtime, new_offset
