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


def calc_powerlaw(G,kmin):
    ddist = zen.degree.ddist(G,normalize=False)
    cdist = zen.degree.cddist(G,inverse=True)
    k = numpy.arange(len(ddist))
    #print ddist
    plt.figure(figsize=(8,12))
    plt.subplot(211)
    plt.bar(k,ddist, width=1.0, bottom=0, color='b')
        
    plt.subplot(212)
    plt.loglog(k,cdist)
        
    N=0
    M=0
    calc = 0
    for i in range(kmin,len(ddist)):
        if(ddist[i]>0):
            N = N + ddist[i]
            M = int(ddist[i])
            for j in range(0,M):
                calc = calc + log((i/(kmin-0.5)))
        
    alpha = 1+N*pow(calc,-1) # calculate using formula!
    print '%1.2f' % alpha
        
    plt.show()



## Visualize
G = zen.io.gml.read('bible.gml')
calc_powerlaw(G,3)
