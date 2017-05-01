import zen
import matplotlib.pyplot as plt
import numpy

G = zen.io.gml.read('bible.gml')

total_degree=0
neighbor_degree=0

n = G.num_nodes
for u in G.nodes_iter():
	total_degree += G.degree(u)
	neighbor_degree += G.degree(u)**2
	
	
print 'Average Degree of Network'
k=total_degree/n

print k

print 'Average Degree of Neighbors'
k2 = neighbor_degree/n
print k2/k