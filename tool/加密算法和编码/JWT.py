import base64
import json
import hmac
import hashlib
# import jwt

# 参考博客 https://www.jianshu.com/p/af8360b83a9f

# 头部
head = {
  'typ': 'JWT',
  'alg': 'HS256'
}

# 载荷
playload = {
  "sub": "1234567890",
  "name": "John Doe",
  "admin": True
}
# *******************************生成JWT**************************
# 头部b64编码
_head = base64.b64encode(json.dumps(head).encode())
print("_head",_head)

# 载荷b64编码
_playload = base64.b64encode(json.dumps(playload).encode())
print("_palyload",_playload)


# hmac 获取摘要
temp = _head+b"."+_playload
secret_key = "arvin".encode()
signature = base64.b64encode(hmac.new(secret_key, temp, digestmod=hashlib.sha256).digest())  # 这就是所谓的HAMC-SHA256算法？
# hmac 本身是一套算法（这套算法要用到一个哈希算法，可以指定，代码中指定的是 sha256）
# sha256全称：Secure Hash Algorithm 2(sha256是一个哈希算法)
#对于任意长度的消息，SHA256都会产生一个256bit长的哈希值，称作消息摘要。
#这个摘要相当于是个长度为32个字节的数组，通常用一个长度为64的十六进制字符串来表示
print('摘要',signature)
print(signature.decode())
my_jwt = (temp+b'.'+signature).decode()
print(my_jwt)
# *******************************验证JWT**************************
head_playload = (my_jwt.split('.')[0]+'.'+my_jwt.split('.')[1]).encode()

signature2 = base64.b64encode(hmac.new(secret_key, head_playload, digestmod=hashlib.sha256).digest())
print('signature',signature)
print('signature2',signature2)
print('两个签名是否相等',signature==signature2)