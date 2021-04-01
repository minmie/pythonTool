import hashlib
import hmac
# 待加密信息
string = '这是一个测试'

# 创建md5对象， sha系列把md5换成sha系列的名字就可以了
hl = hashlib.md5()
hl.update(string.encode())
print('MD5加密前为 ：' + string)
print('MD5加密后为 ：' + hl.hexdigest())

salt = b"abc"
h = hmac.new(salt, string.encode(), digestmod='MD5') # 相当与把MD5加盐的操作集成到一部当中，虽然最后加密的密文不一样
print(h.hexdigest())

salt = b"abc"
hl = hashlib.md5(salt)
hl.update(string.encode())
print('MD5加盐加密前为 ：' + string)
print('MD5加盐加密后为 ：' + hl.hexdigest())


sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())