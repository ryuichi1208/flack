import os
import sys
import re
import requests

class Foo():
    def multiplication(a, b):
        return a * b

    def division(a, b):
        return a / b

    def http_request(url):
        r = requests.get(url)
        return r.status_code

    def http_request_header(url):
        r = requests.get(url)
        return r.headers

if __name__ == "__main__":
    pass

"""
import json
r = requests.post("http://httpbin.org/post", data=json.dumps(data))
print(r.json()['data'])
# '{"key1": "value1", "key2": "value2"}'

data = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.json()['form'])
# {'key1': 'value1', 'key2': 'value2'}

headers = {'user-agent':'test'}
r = requests.get("http://httpbin.org/get", headers=headers)
print(r.json()['headers']['User-Agent'])
# 'test'

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
# 'http://httpbin.org/get?key1=value1&key2=value2'

import requests
from PIL import Image
from io import BytesIO

r = requests.get('http://httpbin.org/image/png')
image = Image.open(BytesIO(r.content))
image.save("test.png")

r = requests.get("http://httpbin.org/get")
print(r.json())
# {'url': 'http://httpbin.org/get', 'origin': 'x.x.x.x', 'headers': {'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'Accept': '*/*', 'User-Agent': 'python-requests/2.18.4', 'Connection': 'close'}, 'args': {}}

print(r.json()["url"])
# 'http://httpbin.org/get'<Paste>

r = requests.get("http://httpbin.org/get")
print(r.text)
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.4"
#
},
#   "origin": "118.103.21.193",
#   "url": "http://httpbin.org/get"
#
}
"""
