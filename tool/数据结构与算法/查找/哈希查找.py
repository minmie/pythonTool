
class HashTable:

    def __init__(self,length):
        """

        :param length:  表长度
        """
        self.length = length
        self.table = [None for _ in range(length)]
        self.maxPrimeNumber=self.max_prime_number()

    def hash(self,value,di=0):
        return (value+di)%self.maxPrimeNumber

    def max_prime_number(self):
        num = self.length
        while True:
            if self.is_prime_mumber(num):
                print('最大素数是:',num)
                return num
            else:
                num -=1


    def is_prime_mumber(self,num):
        mid = num//2
        while mid>1:
            if num%mid==0:
                return False
            mid -=1
        return True



    def insert(self,value):
        key = value
        di = 0
        while True:
            index = self.hash(key,di)
            print('index',index)
            print(self.table[index])
            if self.table[index] is None:
                self.table.insert(index,value)
                break
            else:
                key = index
                di +=1

    def search(self,value):
        key = value
        di = 0

        while True :
            index = self.hash(key, di)
            ret = self.table[index]
            if ret is  None:
                return -1
            elif ret == value:
                return index
            else:
                key = index
                di += 1


if __name__ == '__main__':
    # 建表
    hTable = HashTable(length=12)
    print(hTable.maxPrimeNumber)
    hTable.insert(47)
    hTable.insert(26)
    hTable.insert(60)
    hTable.insert(69)
    print(hTable.table)
    #查找

    print(hTable.search(69))
    print(hTable.search(60))
    print(hTable.search(660))