#构建带有权重的图

graph = {} #整个图为一个字典
graph["start"] = {} # 图的起点，包含了到下一个节点的权重
graph["start"]["a"] = 6
graph["start"]["b"] = 2
#print(graph["start"].keys())#graph["start"]为一个散列表
#print(graph["start"]["a"])#获取从起点到a的权重
#添加其他节点和邻居
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}#终点没有任何邻居
#print(graph)

#建立散列表存储每个节点的开销（从节点开始前往该节点需要的时间）

#python表示无穷大
infinity = float("inf")
#print(infinity)

#创建开销表
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity#不知道的节点，设为无穷大

#创建存储父节点的散列表 用于寻找最短路径
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None#无父节点

#该数组存储处理过得节点
processed = []

"""
函数说明：从costs 中找出当前开销最低的节点

"""
def findLowestCostNode(costs):
	lowest_cost = float("inf") #初始最低节点为无穷大
	lowest_cost_node = None
	for node in costs:   #遍历所有节点
		cost = costs[node]
		if cost < lowest_cost and node not in processed:#当前节点开销更低且没有被处理过
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node	


"""
函数说明：遍历图，找出最短路径
"""
if __name__  == "__main__":
	node = findLowestCostNode(costs)#找到未处理的开销最小节点
	while node is not None : #所有节点被处理后结束
		cost = costs[node]
		neighbors = graph[node]
		for n in neighbors.keys(): #遍历当前所有节点的邻居
			new_cost = cost + neighbors[n]
			if costs[n] > new_cost: #如果经当前节点前往邻居更近
				costs[n] = new_cost #更新该邻居的开销
				parents[n] = node  #同时将该邻居节点的父节点设置为当前节点
		processed.append(node)#当前节点已经处理过
		node = findLowestCostNode(costs) #找出下一个节点

print("到终点的最短路径为", costs["fin"])
print(parents)

