import json
import os


class Serializer():
    def __init__(self, filename="db.yaml"):
        self.filename = filename
        self.data = dict()

    def load(self):
        if not os.path.isfile(self.filename):
            return

        with open(self.filename, "r") as f:
            self.data = json.load(f)

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f)

    def set_offset(self, filename, offset):
        if filename not in self.data:
            self.data[filename] = dict()
        self.data[filename]["offset"] = offset

    def get_offset(self, filename):
        offset = 0
        try:
            offset = self.data[filename]["offset"]
        except KeyError:
            pass
        return offset

    def set_access_time(self, filename, access_time):
        if filename not in self.data:
            self.data[filename] = dict()
        self.data[filename]["access_time"] = access_time

    def get_access_time(self, filename):
        access_time = 0
        try:
            access_time = self.data[filename]["access_time"]
        except KeyError:
            pass
        return access_time
