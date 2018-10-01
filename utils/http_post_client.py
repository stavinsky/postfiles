from urllib.request import Request
# from urllib.parse import urlencode
from urllib.request import urlopen
import json


data = {
    "test_key": "test_value"
}
data = json.dumps(data).encode()
# data = urlencode(data).encode()
r = Request(url="http://localhost:8000", data=data)
with urlopen(r) as f:
    print(f.status)
    print(f.read())
