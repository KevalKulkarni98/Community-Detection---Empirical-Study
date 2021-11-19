import networkx as nx
import os
import sys 

dg = nx.read_gml(os.path.join(sys.path[0], "dolphins.gml"))
print("*****************Dolphins*****************")
print(nx.info(dg))
print("Avg path length : ", nx.average_shortest_path_length(dg))
average = nx.average_clustering(dg)
print("Avg clustering coefficient : ", average)
print("*******************************************")



print("*****************Karate*****************")
kg = nx.read_gml(os.path.join(sys.path[0], "karate.gml"), label='id')
print(nx.info(kg))
print("Avg path length : ", nx.average_shortest_path_length(kg))
average = nx.average_clustering(kg)
print("Avg clustering coefficient : ", average)
print("*******************************************")


print("*****************Jazz*****************")
f = open(os.path.join(sys.path[0], "jazz.net"),"r")
lines = f.readlines()
f.close()
nf = open(os.path.join(sys.path[0], "jazz.net"),"w")
for i in lines:
    if i != lines[0] and i != lines[1] and i != lines[2]:
        nf.write(i)
nf.close()
jg = nx.read_weighted_edgelist(os.path.join(sys.path[0], "jazz.net"))
print(nx.info(jg))
print("Avg path length : ", nx.average_shortest_path_length(jg))
average = nx.average_clustering(jg)
print("Avg clustering coefficient : ", average)
print("*******************************************")
