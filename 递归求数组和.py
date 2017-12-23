#递归方法求数组的和
def sumlist(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sumlist(arr[1:])

print(sumlist([2,3,4,6,7]))

