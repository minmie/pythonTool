# 这是一个自定义了一个open（）方法，并实现了上下文管理
class File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()

# 使用上下文
with File('out.txt', 'w') as f:
    print("writing")
    f.write('hello, python')