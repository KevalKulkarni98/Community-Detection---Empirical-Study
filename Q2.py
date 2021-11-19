import networkx as netx
import os
import sys 

dolphingraph = netx.read_gml(os.path.join(sys.path[0], "dolphins.gml"))
print("*****************Dolphins*****************")
print(netx.info(dolphingraph))
print("Average path length : ", netx.average_shortest_path_length(dolphingraph))
average = netx.average_clustering(dolphingraph)
print("Average clustering coefficient : ", average)
print("*******************************************")



print("*****************Karate*****************")
karategraph = netx.read_gml(os.path.join(sys.path[0], "karate.gml"), label='id')
print(netx.info(karategraph))
print("Average path length : ", netx.average_shortest_path_length(karategraph))
average = netx.average_clustering(karategraph)
print("Average clustering coefficient : ", average)
print("*******************************************")


print("*****************Jazz*****************")
f = open(os.path.join(sys.path[0], "jazz.net"),"r")
lines = f.readlines()
f.close()
jazzgraph = netx.read_weighted_edgelist(os.path.join(sys.path[0], "jazz.net"))
print(netx.info(jazzgraph))
print("Average path length : ", netx.average_shortest_path_length(jazzgraph))
average = netx.average_clustering(jazzgraph)
print("Average clustering coefficient : ", average)
print("*******************************************")
