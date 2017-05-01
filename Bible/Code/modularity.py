import zen
import matplotlib.pyplot as plt
import numpy
from numpy import *


G = zen.io.gml.read('bible.gml')
c = {
	'people': ['god','aaron','abel','abraham','absalom','adam','ahab','amos','balaam','baruch','bathsheba','belshazzar','benjamin','bilhah','boaz','cain',
'cyrus',
'daniel',
'darius',
'david',
'deborah',
'delilah',
'eli',
'elijah',
'elisha',
'enoch',
'esau',
'esther',
'eve',
'ezra',
'gideon',
'goliath',
'hagar',
'haggai',
'ham',
'hannah',
'heber',
'hiram',
'isaac',
'isaiah',
'ishmael',
'jacob',
'japheth',
'jehoiachin',
'jeremiah',
'jeroboam',
'jesse',
'jezebel',
'joab',
'job',
'joel',
'jonah',
'jonathan',
'joseph',
'joshua',
'josiah',
'judah',
'laban',
'leah',
'levi',
'lot',
'manasseh',
'micah',
'michal',
'miriam',
'moab',
'mordecai',
'moses',
'naomi',
'nathan',
'nebuchadnezzar',
'nehemiah',
'noah',
'rachel',
'rahab',
'rebekah',
'rehoboam',
'reuben',
'ruth',
'samuel',
'samson',
'sarah',
'satan',
'saul',
'sennacherib',
'seth',
'shalmaneser',
'shem',
'solomon',
'zechariah',
'zephaniah',
'zerubbabel',
'zilpah',
'zipporah'
],
	'places': ['bashan','beersheba','bethel','carmel','dan','gerizim','gibeah','gilead','gilgal','jabesh','jerusalem','megiddo','mizpah','samaria',
'shechem','shiloh'] 
}

print '\nModularity:'	
print zen.algorithms.modularity(G,c)

print '\nSize of the Largest Component:'
print len(zen.algorithms.components(G))

N = len(G.nodes())

max_weight = 0
nodes = []
for u,v in G.edges_iter():
	weight = G.weight(u,v)
	if(weight>max_weight):
		max_weight = weight
		nodes.insert(0,u)
		nodes.insert(1,v)

print '\nMaximum Weight:'
print max_weight
print '\nBetween Nodes:'
print nodes[0]
print nodes[1]
