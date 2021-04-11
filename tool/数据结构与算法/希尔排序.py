def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap,n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == '__main__':
    l1=[5,1,2,6,4,5,11,8,9]

    shell_sort(l1)
    print(l1)