from collections import deque
def dfs(Graph, root):
	INFINITY=100000
	dis={}
	for node in list(Graph.keys()):
		dis[node] = INFINITY
		
	stack = deque([])
	dis[root]=0
	stack.append(root)
	
	while len(stack) != 0 : 
		current = stack.pop()
		#dis[current]=1
		print(current)
		for x in Graph[current]:
			if dis[x]==INFINITY:
				stack.append(x)
				dis[x]=dis[current]+1
			
	print(dis)
		
	
	
	

#main program 
# the graph 
my_graph = {
	1:[2,3,4],
	2:[1,5,6],
	3:[1],
	4:[1,7,8],
	5:[2,9,10],
	6:[2],
	7:[4,11,12],
	8:[4],
	9:[5],
	10:[5],
	11:[7],
	12:[7]
	}

root = 1	
dfs(my_graph,root)
