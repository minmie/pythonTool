


def gen():
    for i in range(100,1,-1):
        a=yield i
        print(a)

if __name__ == '__main__':
    # print(gen)
    g = gen()
    # print(g)
    g2 = (i for i in range(100))
    # print(g2)
    print(next(g))
    print(next(g))
    # print(g.send(3))
