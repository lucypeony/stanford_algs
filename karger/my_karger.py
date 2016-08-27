# -*- coding: utf-8 -*-
"""
karger min cut

Created on Sat Aug 27 16:20:26 2016

@author: Lucy
"""
import random 
from random import randint


#loading data from the text files
with open('kargerMinCut.txt') as req_file:
    mincut_data =[]
    for line in req_file:
        line = line.split()
        if line :
            line = [int(i) for i in line]
            mincut_data.append(line)
threshold = 500
min_cut = 100000
for i in range(threshold):
    #extracting edges from the data 
    edgelist =[]
    nodelist =[]
    for every_list in mincut_data:
        nodelist.append(every_list[0])
        temp_list = []
        for temp in range(1, len(every_list)):
            flag = 0
            for ad in edgelist:
                if set(ad) == set(temp_list):
                    flag = 1
            if flag == 0 :
                edgelist.append([every_list[0],every_list[temp]])

           

    
    #print(my_nodelist)
    while(len(nodelist) > 2):
        val = randint(0, (len(edgelist)-1))
        target_edge = edgelist[val]
        replace_with=target_edge[0]
        should_replace=target_edge[1]
        for edge in edgelist:
            if(edge[0] == should_replace):
                edge[0] = replace_with
            if(edge[1] ==should_replace):
                edge[1] == replace_with
        edgelist.remove(target_edge)
        if should_replace in nodelist:        
            nodelist.remove(should_replace)
        for i in range((len(edgelist)-1),-1,-1):
            if edgelist[i][0] == edgelist[i][1]:
                edgelist.remove(edgelist[i])
        
    edge_num = len(edgelist)
    if edge_num < min_cut :
        min_cut = edge_num 
    print(i,edge_num,min_cut)
                
print(min_cut)
