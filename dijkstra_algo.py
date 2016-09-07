# -*- coding: utf-8 -*-
"""
Dijkstra's Algorithm 
Created on Wed Sep  7 19:45:33 2016

@author: Lucy
"""

def dijkstra_basic(graph,s):
    #A[] : store shortest path , to minimise the a[v]+l[v,w]
    A={}
    X =set(s)
    Y =set(graph.keys())
    Y = Y - X
    A[s] = 0 
    for v in X : 
        v_nodes=graph[v]
        temp_len =  10000
        for v_nodes_temp in v_nodes: 
            w,w_len=v_nodes_temp[0],v_nodes_temp[1]
            if 
    
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