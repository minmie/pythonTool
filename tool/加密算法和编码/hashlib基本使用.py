import hashlib

# MD5
string = 'hello world'
hl = hashlib.md5()
hl.update(string.encode())
print('MD5加密前为 ：' + string)
print('MD5加密后为 ：' + hl.hexdigest())


# sha256 基本使用
x1 = hashlib.sha256()
x1.update(b"asd")
print("x_1 = " + x1.hexdigest())

x2 = hashlib.sha256()
x2.update("asd".encode())
print("x_2 = " + x2.hexdigest())

x3 = hashlib.sha256()
x3.update(b"a")
x3.update(b"s")
x3.update(b"d")
print("x_3 = " + x3.hexdigest())

x4 = hashlib.sha256(b"asd").hexdigest()
print("y_1 = " + x4)
z = hashlib.new("sha256")
z.update(b"asd")

