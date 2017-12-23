#快速排序
def quicksort(array):
    if len(array) < 2:
        return array   #基线条件：为空或只包含一个元素的数组是有序的
    else:
        pivot = array[0]  #递归条件
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,6,7,2,4,6,9,11]))
