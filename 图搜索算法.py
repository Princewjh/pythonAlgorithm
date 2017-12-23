from collections import deque
#创建一个图
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#判断此人是否为销售商
def person_is_seller(name):
	return name[-1] == 'm'

#图搜索算法
def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []#该列表存储已经检查过得元素
	while search_queue: #图不为空
		person = search_queue.popleft() #检查队列中第一个元素
		if not person in searched:
			if person_is_seller(person):
				print(person + "is a mango seller!")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)#将该元素加入已寻找列表
	print("not Found!")
	return False

search("you")


