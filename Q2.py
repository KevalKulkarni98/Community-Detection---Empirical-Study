import networkx as netx
import os
import sys 

dg = netx.read_gml(os.path.join(sys.path[0], "dolphins.gml"))
print("*****************Dolphins*****************")
print(netx.info(dg))
print("Average path length : ", netx.average_shortest_path_length(dg))
average = netx.average_clustering(dg)
print("Average clustering coefficient : ", average)
print("*******************************************")



print("*****************Karate*****************")
kg = netx.read_gml(os.path.join(sys.path[0], "karate.gml"), label='id')
print(netx.info(kg))
print("Average path length : ", netx.average_shortest_path_length(kg))
average = netx.average_clustering(kg)
print("Average clustering coefficient : ", average)
print("*******************************************")


print("*****************Jazz*****************")
f = open(os.path.join(sys.path[0], "jazz.net"),"r")
lines = f.readlines()
f.close()
jg = netx.read_weighted_edgelist(os.path.join(sys.path[0], "jazz.net"))
print(netx.info(jg))
print("Average path length : ", netx.average_shortest_path_length(jg))
average = netx.average_clustering(jg)
print("Average clustering coefficient : ", average)
print("*******************************************")
