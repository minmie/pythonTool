# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time
from urllib import parse
import requests

secret_id = "abc"
secret_key = "123"

msg="abc"
start_time = time.time()
hmac_str = hmac.new(secret_key.encode("utf8"), msg.encode("utf8"), hashlib.sha256)
print(hmac_str.hexdigest())
end_time = time.time()
print(str(base64.b64encode(hmac_str.digest())))
print(parse.urlencode({"sig":str(base64.b64encode(hmac_str.digest()))}))
print("加密用时：",end_time-start_time)
