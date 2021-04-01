
from Cryptodome.Cipher import DES   # pip install pycryptodomex
import binascii
# 这是密钥
key = b'abcdefgh'
# 需要去生成一个DES对象
des = DES.new(key, DES.MODE_ECB)
# 需要加密的数据
text = 'python spider!'
text = text + (8 - (len(text) % 8)) * '='
# 加密的过程
encrypto_text = des.encrypt(text.encode())
print(encrypto_text)
print(binascii.b2a_hex(encrypto_text))

#解密的过程
decrypt_text = des.decrypt(encrypto_text)
print(decrypt_text)