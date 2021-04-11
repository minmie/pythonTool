# print(0 and 1)
# print(1 or False)
# print(1 and False)
# print(0 and 2 or 1 or 4)
# print(0 or False and 1)

class A:
    def __init__(self):
        self.a=1
        self.b=2
    def _f1(self):
        print(111)

    def __f2(self):
        print(222)

a=A()