#选择排序算法

"""
函数说明：找出当前数组中最小元素
Parameter：
   arr - 未排序数组
Returns：
   smallest_index -最小元素索引
"""
def findSmallest(arr):
	smallest = arr[0] #存储最小值
	smallest_index = 0 #存储最小元素的索引
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

#排序函数
"""
函数说明：对数组进行排序
Parameters:
   arr - 未排序数组
Returns:
   newArr - 排序后数组
"""
def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))  #找出最小元素，并加入到新数组中去
	return newArr


print(selectionSort([5,3,6,2,10]))