import rsa  # pip install rsa
import binascii
key = rsa.newkeys(3000)#生成随机秘钥
privateKey = key[1]#私钥
publicKey = key[0]#公钥
message ='sanxi Now is better than never.'
print('Before encrypted:',message)
message = message.encode() # 转化为字节
# 加密过程
cryptedMessage = rsa.encrypt(message, publicKey)
print('After encrypted:\n',cryptedMessage)
print(binascii.b2a_hex(cryptedMessage))
# 解密过程
message = rsa.decrypt(cryptedMessage, privateKey)
message = message.decode()
print('After decrypted:',message)