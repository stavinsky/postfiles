from contrib.db import Serializer
from datetime import datetime
import os


def test_get_line_unix(tmpdir):
    tmp_file = tmpdir.join("test_slash_n.txt")
    filename = os.path.join(tmp_file.dirname, tmp_file.basename)

    db = Serializer(filename=filename)
    data = db.data = {
        "test": "test",
        "test1": "test2",
    }
    db.save()

    db.data = {}
    db.load()

    assert db.data == data


def test_time_serialization():
    db = Serializer("test.file")
    now = datetime.now()
    db.set_access_time("test", now)
    assert now == db.get_access_time("test")
