# -*- coding: utf-8 -*-
"""
To compute the Strongly Connected Components(SCCs)

Created on Sun Sep  4 05:44:32 2016

@author: Lucy
"""
#from collections import deque

#finishing time of each v in V 
f = {}

#leaders dictionary 
leader = {}

#number of nodes that are
t = 0
#current source vertex
s = -1

explored ={}

def DFS(G,i):
    global explored
    explored[i] = True
    leader[i] = s
    #for each arc (i,j) in G 
    if i in G:    
        for j in G[i]:
            #print(j,'and ',G[i])
            #print(explored)
            if not explored[j]:
                DFS(G,j)
    global t
    t = t + 1
    #print(i)
    f[i]=t
    
def DFS_LOOP(G,node_list):
    global explored
    explored ={}
    for i in node_list:
        explored[i] = False
    #print('inside dfs loop :',node_list)
    for i in node_list:
        #print(i)
        #print("node_list",node_list)
        #print('explored: ',explored)
        if not explored[i]: 
            global s
            s = i
            DFS(G,i)
    

def graph_reverse(my_graph):
    reverse_g={}
    for x in list(my_graph.keys()):
        for y in my_graph[x]:
            
            if y in reverse_g:
                reverse_g[y].append(x)
            else: 
                reverse_g[y] = []
                reverse_g[y].append(x)
    return reverse_g

def SCC(G):
    G_rev = graph_reverse(G)
    key_list = list(G.keys())
    
    my_node_list = key_list[::]
    #turn key list into node list
    for x in key_list : 
        my_node_list.extend(G[x])
    node_list=set(my_node_list)
    print("new node list",node_list)
    #print(G_rev)
    print("first turn loop ")
    DFS_LOOP(G_rev,node_list)
    print("second turn loop")
    print('f dict',f)
    f_node_list=sorted(f,key=f.get, reverse=True)
    

    print("f node list :",f_node_list)
    DFS_LOOP(G,f_node_list)
    
    #calculate the SCCs
    print(leader)
    
    #calculate SCCs
    scc={}
    for x in node_list:
        if leader[x] in scc : 
            scc[leader[x]] = scc[leader[x]]+1
        else:
            scc[leader[x]] = 1
    print(scc)
    print("SCC len : ",len(scc))
    print(sorted(list(scc.values())))
    

#data1
graph1 = {
    1:[2],
    2:[3],
    3:[1],
    4:[3],
    5:[4,6],
    6:[4,7],
    7:[9],
    8:[7,9]
    }

#data from file 
my_graph={}
my_file = open("SCC.txt")
for line in my_file: 
    x,y = [int(i) for i in line.split()]
    if x not in my_graph :
        temp=[]
        temp.append(y)
        my_graph[x]=temp
    else:
        my_graph[x].append(y)

    #print(my_graph)


SCC(my_graph)


