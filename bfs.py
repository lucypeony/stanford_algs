from collections import deque 

def bfs(Graph,root):
	INFINITY = 100000
	dis={}
	parent={}
	
	for node in list(Graph.keys()):
		dis[node] = INFINITY
		parent[node] = -1  
		
	queue = deque([])
	#queue.append()
	#queue.popleft()
	
	dis[root] = 0 
	queue.append(root)
	
	while len(queue)!= 0 :
		current = queue.popleft()
		
		for n in Graph[current]:
			if dis[n] == INFINITY:
				dis[n] = dis[current] + 1 
				parent[n] = current
				queue.append(n)
	print(parent)
	
	
	

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
bfs(my_graph,root)
