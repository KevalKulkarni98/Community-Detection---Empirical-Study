import itertools
import time
import networkx as netx
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms.community.quality import modularity
import numpy as np
from sklearn.cluster import SpectralClustering

Graph1 = netx.read_gml("karate.gml", label = 'id')
print("*****************Karate*****************")


k = 10
t1 = time.time()
comp = girvan_newman(Graph1)
t2 = time.time()
max=-1
print("_________________Girvan Newman________________________")
for communities in itertools.islice(comp, k):
    mod=modularity(Graph1, communities)
    if(mod>max):
    	max=mod
    	ans=communities
print(ans)
print('Total Cummunities=',len(ans))
print('Modularity=',modularity(Graph1, ans))
print('Time taken=',t2-t1)
print("_______________________________________________")


t1 = time.time()
c = list(greedy_modularity_communities(Graph1))
t2 = time.time()
print("_________________Modularity Based Clustering_____________________")
for x in c:
    print(sorted(x))

print('Total Cummunities=',len(c))
print('Modularity=',modularity(Graph1, c))
print('Time taken=',t2-t1)
print("_____________________________________________")



adj_mat = netx.to_numpy_matrix(Graph1)
t1 = time.time()
sc = SpectralClustering(4, affinity='precomputed', n_init=100)
sc.fit(adj_mat)
t2 = time.time()
print("____________Spectral Clustering______________")
graphlist = list(Graph1)
labels = sc.labels_

ls = [[] for i in range(4)]

i = 0
for x in labels:
    if(x == 0):
        ls[0].append(graphlist[i])
        i += 1
    elif(x == 1):
        ls[1].append(graphlist[i])
        i += 1
    elif(x == 2):
        ls[2].append(graphlist[i])
        i += 1
    elif(x == 3):
        ls[3].append(graphlist[i])
        i += 1
        
print(ls)
print('Total Cummunities=',len(ls))
print('Modularity=',modularity(Graph1, ls))
print('Time taken=',t2-t1)
print("_____________________________________________")


################################################################


Graph2 = netx.read_weighted_edgelist("jazz.net")
print("*****************Jazz*****************")


k = 10
t1 = time.time()
comp = girvan_newman(Graph2)
t2 = time.time()
max=-1
print("_________________Girvan Newman________________________")
for communities in itertools.islice(comp, k):
    mod=modularity(Graph2, communities)
    if(mod>max):
    	max=mod
    	ans=communities
print(ans)
print('Total Cummunities=',len(ans))
print('Modularity=',modularity(Graph2, ans))
print('Time taken=',t2-t1)
print("_______________________________________________")


t1 = time.time()
c = list(greedy_modularity_communities(Graph2))
t2 = time.time()
print("_________________Modularity Based Clustering_____________________")
for x in c:
    print(sorted(x))

print('Total Cummunities=',len(c))
print('Modularity=',modularity(Graph2, c))
print('Time taken=',t2-t1)
print("_____________________________________________")



adj_mat = netx.to_numpy_matrix(Graph2)
t1 = time.time()
sc = SpectralClustering(4, affinity='precomputed', n_init=100)
sc.fit(adj_mat)
t2 = time.time()
print("____________Spectral Clustering______________")
graphlist = list(Graph2)
labels = sc.labels_

ls = [[] for i in range(4)]

i = 0
for x in labels:
    if(x == 0):
        ls[0].append(graphlist[i])
        i += 1
    elif(x == 1):
        ls[1].append(graphlist[i])
        i += 1
    elif(x == 2):
        ls[2].append(graphlist[i])
        i += 1
    elif(x == 3):
        ls[3].append(graphlist[i])
        i += 1
        
print(ls)
print('Total Cummunities=',len(ls))
print('Modularity=',modularity(Graph2, ls))
print('Time taken=',t2-t1)
print("_____________________________________________")




################################################################
Graph3 = netx.read_gml("dolphins.gml", label = 'id')
print("*****************Dolphins*****************")


k = 10
t1 = time.time()
comp = girvan_newman(Graph3)
t2 = time.time()
max=-1
print("_________________Girvan Newman________________________")
for communities in itertools.islice(comp, k):
    mod=modularity(Graph3, communities)
    if(mod>max):
    	max=mod
    	ans=communities
print(ans)
print('Total Cummunities=',len(ans))
print('Modularity=',modularity(Graph3, ans))
print('Time taken=',t2-t1)
print("_______________________________________________")


t1 = time.time()
c = list(greedy_modularity_communities(Graph3))
t2 = time.time()
print("_________________Modularity Based Clustering_____________________")
for x in c:
    print(sorted(x))

print('Total Cummunities=',len(c))
print('Modularity=',modularity(Graph3, c))
print('Time taken=',t2-t1)
print("_____________________________________________")



adj_mat = netx.to_numpy_matrix(Graph3)
t1 = time.time()
sc = SpectralClustering(4, affinity='precomputed', n_init=100)
sc.fit(adj_mat)
t2 = time.time()
print("____________Spectral Clustering______________")
graphlist = list(Graph3)
labels = sc.labels_

ls = [[] for i in range(4)]

i = 0
for x in labels:
    if(x == 0):
        ls[0].append(graphlist[i])
        i += 1
    elif(x == 1):
        ls[1].append(graphlist[i])
        i += 1
    elif(x == 2):
        ls[2].append(graphlist[i])
        i += 1
    elif(x == 3):
        ls[3].append(graphlist[i])
        i += 1
        
print(ls)
print('Total Cummunities=',len(ls))
print('Modularity=',modularity(Graph3, ls))
print('Time taken=',t2-t1)
print("_____________________________________________")


################################################################
