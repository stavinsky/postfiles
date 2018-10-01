import asyncio
from  reader_aio import get_line
import ssl
from os.path import abspath, expanduser
import aiohttp
import json


# def get_ssl_context(
        # enable=False, cafile=None, client_crt=None, client_key=None):
    # if not enable:
        # return None
    # ssl_context = ssl.create_default_context(
        # ssl.Purpose.SERVER_AUTH, cafile=cafile)
    # ssl_context.check_hostname = False
    # ssl_context.load_cert_chain(client_crt, client_key)
    # return ssl_context


# async def main():
    # data = {
       # "message": "testtest",
       # "fields": {"program": "mt4"},
       # "source": "python",
       # "offset": 0
    # }
    # cntx = get_ssl_context(
            # enable=True,
            # cafile=expanduser("~/temp/config/certs/rootCA.crt"),
            # client_crt=expanduser("~/temp/config/certs/client.pem"),
            # client_key=expanduser("~/temp/config/certs/client.key"),
           # )
    # async with aiohttp.ClientSession() as session:
        # async with session.post("https://logstash.fortfs.net:5048", json=data, ssl=cntx) as resp:
             # print(resp.status)


# async def main():
    # async for i in get_line("test.log", sep=b"\n"):
        # print(i)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

