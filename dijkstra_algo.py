# -*- coding: utf-8 -*-
"""
Dijkstra's Algorithm 
Created on Wed Sep  7 19:45:33 2016
@author: Lucy
"""

def dijkstra_basic(graph,s):
	#constants 
	INFINITE = 1000000

    #A[] : store shortest path , to minimise the a[v]+l[v,w]
    A={}
    X =set(s)
    Y =set(graph.keys())
	
	for node in Y : 
		A[node] = INFINITE
	
	
	
    Y = Y - X
    A[s] = 0 
	
    while not empty(Y):
		w = NULL 
		for node in X : 
			v_w_len = INFINITE
			for node_v_pair in graph[node]:
				if node_v_pair[0] in Y:
					v_w_len_temp = node_v_pair[1] + A[node]
					if v_w_len_temp < v_w_len : 
						v_w_len = v_w_len_temp
						w = node_v_pair[0]
		X = X + w
		Y = Y - w
		A[w] =v_w_len
    
    pass
    
def dijkstra_heap():
    pass
    
    
#main 

#read the file 
my_file = open('dijkstraData.txt')
my_graph = {}

count = 1
for line in my_file:
    temp = line.split()
    temp_lst=[]
    for vertex_temp in temp : 
        vertex = vertex_temp.split(',')
        if len(vertex) == 2:
            temp_lst.append(vertex)
    my_graph[count]=temp_lst
    count = count + 1
#print(my_graph)

s=1
shortest_path = dijkstra_basic(my_graph,s)
