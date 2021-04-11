


arr = [3,2,1,4,9,6]


def func(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

if __name__ == '__main__':
    func(arr)


"""
复杂度O（n^2）

"""