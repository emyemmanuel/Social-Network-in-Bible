import zen
import matplotlib.pyplot as plt  	# if matplotlib doesn't work comment this line out
plt.ioff()# if matplotlib doesn't work comment this line out

import numpy
from numpy import *
import sys
sys.path.append('../zend3js/')
import d3js
from time import sleep
import random
from numpy import *
from numpy.linalg import eig,norm


def index_of_min(v):
    return numpy.where(v == min(v))[0]

def index_of_max(v):
    return numpy.where(v == min(v))[0]

## HELPER FUNCTIONS =======================================
def RGBToHTMLColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple
        # that's it! '%02x' means zero-padded, 2-digit hex values
    return hexcolor

def HTMLColorToRGB(colorstring):
    """ convert #RRGGBB to an (R, G, B) tuple """
    colorstring = colorstring.strip()
    if colorstring[0] == '#': colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)

def color_interp(color1,color2,v,m=0,M=1):
    c1 = array(HTMLColorToRGB(color1))
    c2 = array(HTMLColorToRGB(color2))
    if v > M:
        c = tuple(c2)
    elif v < m:
        c = tuple(c1)
    else:
            #c = tuple( c1 + (c2-c1)/(M-m)*(v-m) ) # linear interpolation of color
        c = tuple( c1 + (c2-c1)*(1 - exp(-2*(v-m)/(M-m))) ) # logistic interpolation of color
    return RGBToHTMLColor(c)

def color_by_value(d3,G,x,color1='#77BEF5',color2='#F57878'):
    d3.set_interactive(False)
    m = min(x)
    M = max(x)
    for i in G.nodes_iter_():
        d3.stylize_node_(i, d3js.node_style(fill=color_interp(color1,color2,x[i])))
    d3.update()
    d3.set_interactive(True)




def propagate(G,d3,x,steps,slp=0.5,keep_highlights=False,update_at_end=False):
    interactive = d3.interactive
    d3.set_interactive(False)
    A = G.matrix().T  # adjacency matrix of the network G
    d3.highlight_nodes_(list(where(x>0)[0]))
    d3.update()
    sleep(slp)
    cum_highlighted = sign(x)
    for i in range(steps): # the brains
        x = sign(dot(A,x)) # the brains
        cum_highlighted = sign(cum_highlighted+x)
        if not update_at_end:
            if not keep_highlights:
                d3.clear_highlights()
            d3.highlight_nodes_(list(where(x>0)[0]))
            d3.update()
            sleep(slp)
        if update_at_end:
            if not keep_highlights:
                d3.clear_highlights()
                d3.highlight_nodes_(list(where(x>0)[0]))
            else:
                d3.highlight_nodes_(list(where(cum_highlighted>0)[0]))
            d3.update()
        d3.set_interactive(interactive)
        if keep_highlights:
            return cum_highlighted
        else:
            return x



## Visualize
G = zen.io.gml.read('bible.gml')
d3 = d3js.D3jsRenderer(G, event_delay=0.1, interactive=False, autolaunch=True)

y=zeros(G.num_nodes)
y[1] = 1

propagate(G,d3,y,10,slp = 1)

#d3 = d3js.D3jsRenderer(G, event_delay=0.1, interactive=False, autolaunch=False)
d3.update()
sleep(1)
'''
dt = 0.05 # the "infintesimal" size steps we take to integrate
T = 6 # the end of the simulation time
time = linspace(0,T,int(T/dt)) # the array of time points spaced by dt




N = G.num_nodes
x = zeros(G.num_nodes) # the state vector
x[0] = 1
color_by_value(d3,G,x) # this colors the network according to the value of x
A = G.matrix()
c = 1
D = zeros((N,N))
for i in range(N):
    D[i][i] = G.degree_(i)

L = D - A

k, v = eig(L)
v1 = numpy.abs(v)
k1_idx = index_of_min(k)
equi = v1[:,k1_idx]
mag = numpy.linalg.norm(equi)
equinorm = equi/mag
distance = []
print 'simulating diffusion...'
for i,t in enumerate(time):
    # at each time point update the value of x
    x = x - c*numpy.dot(L,x)*dt
    color_by_value(d3,G,x)
    sleep(0.1)
    mag_x = numpy.linalg.norm(x)
    x_norm = x/mag_x
    dist = numpy.sqrt(numpy.sum((x_norm - equinorm)**2))
    distance.append(dist)

plt.figure()
plt.plot(time,distance) # replace xvalue and yvalue with what you want to plot
plt.xlabel('t')
plt.ylabel('normalized euclidean distance') # change this label
plt.show()

'''


d3.stop_server()
