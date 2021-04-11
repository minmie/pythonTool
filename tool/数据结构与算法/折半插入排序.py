
def half_insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        x=alist[i]
        low=0
        high=i-1
        while low <= high:
            mid=(low+high)//2
            if x<alist[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i-1,low-1,-1):
            alist[j+1] = alist[j]
        alist[low] = x

if __name__ == '__main__':
    a= [3,2,1,33,22,55,32,54,75,35,895,4]
    # a= [3,2,1,33]
    # a= [3,22,1]
    half_insert_sort(a)
    print(a)
    # for i in range(0,0):
    #     print(i)