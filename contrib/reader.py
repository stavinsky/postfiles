import os
import re


def get_line(name, offset=0, sep=b'\r\n', chunk_size=4096):
    name = os.path.abspath(name)
    with open(name, 'r+b') as f:
        f.seek(offset)
        tmp_line = b""
        chunk = f.read(chunk_size)
        while chunk:
            if len(tmp_line):
                chunk = tmp_line + chunk
                tmp_line = b''
            while chunk:
                line, s, chunk = chunk.partition(sep)
                if 0 in line:
                    return
                if s is sep:
                    offset = offset + len(line) + len(sep)
                    yield (line, offset)
                if s is b'':
                    tmp_line = tmp_line + line
            chunk = f.read(chunk_size)


def get_files_list(dir_path, pattern):
    files = list()
    pattern = re.compile(pattern)
    with os.scandir(dir_path) as it:
        for fo in it:
            if fo.is_dir():
                continue
            if pattern.match(fo.name):
                full_path = os.path.abspath(
                    os.path.join(dir_path, fo.name))
                f = {
                    "name": full_path,
                    "mtime": fo.stat().st_mtime,
                }
                files.append(f)
    return files
