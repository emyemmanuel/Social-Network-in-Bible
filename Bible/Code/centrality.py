import zen
import numpy
from numpy import *
import numpy.linalg as la
import matplotlib.pyplot as plt

G = zen.io.gml.read('bible.gml')
A = G.matrix()
N = G.num_nodes

# prints the top five (num) nodes according to the centrality vector v
# v takes the form: v[nidx] is the centrality of node with index nidx
def print_top(G,v, num=10):
	idx_list = [(i,v[i]) for i in range(len(v))]
	idx_list = sorted(idx_list, key = lambda x: x[1], reverse=True)
	for i in range(min(num,len(idx_list))):
		nidx, score = idx_list[i]
		print '  %i. %s (%1.4f)' % (i+1,G.node_object(nidx),score)
		#print '  %i. %s' % (i+1,G.node_object(idx))

# returns the index of the maximum of the array
# if two or more indices have the same max value, the first index is returned
def index_of_max(v):
	return numpy.where(v == max(v))[0]
	
print '\n============================================='
# Degree Centrality
print '\nDegree Centrality:'
vd=[]
for i in range(N):
	w = 0
	list_neighbors = G.neighbors_(i)
	for j in range (len(list_neighbors)):
		w = w + G.weight(G.node_object(i),G.node_object(list_neighbors[j]))
	vd.append(w)
print_top(G,vd)

print '\n============================================='
# Eigenvector Centrality
print '\nEigenvector Centrality:'
ev1 = zen.algorithms.centrality.eigenvector_centrality_(G, weighted=True)
print_top(G,ev1)
k, v = la.eig(A)
k1_idx = index_of_max(k)

print '\n============================================='
# Betweenness Centrality
print '\nBetweenness Centrality:'
bc = zen.algorithms.centrality.betweenness_centrality_(G)
print_top(G,bc)

print '\n============================================='
# Diameter
print '\nDiameter of the Network:'

print zen.diameter(G)