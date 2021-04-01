import base64

text = '你好 世界！'.encode()
a=base64.b64encode(text)
print('编码后的数据',a)

b = base64.b64decode(a)
print('解码后的数据',b.decode())