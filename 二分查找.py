#二分查找
def binary_search(list1, item):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list1[mid]
        if guess < item:
            low = mid +1
        elif guess > item:
            high = mid - 1
        else:
            return mid
    return "notFound"

if __name__ == "__main__":
    testlist = [1,3,4,5,7,9]
    print(binary_search(testlist,3))
    print(binary_search(testlist,-1))
