import urllib


class HTTPSernder():
    def __init__(self, url, ssl_context=None):
        self.url = url
        self.ssl_context = ssl_context

    def post(self, data):
        """ data should be endoded byte string """
        r = urllib.request.Requst(
            url=self.url, data=data)
        with urllib.request.urlopen(
                r, context=self.ssl_context) as f:
            return f.status
