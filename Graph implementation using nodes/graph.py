# -*- coding: utf-8 -*-

from collections import OrderedDict

class Node:

    def __init__(self, key):
        self.id = key
        self.connectedTo = OrderedDict()  

class Graph:

    def __init__(self):
        self.nodes = OrderedDict()  

    def addNode(self, key):
        newNode = Node(key)
        self.nodes[key] = newNode
        return newNode

    def addEdge(self, fromNode, toNode, weight=0):
        if fromNode not in self.nodes:
            self.addNode(fromNode)
        if toNode not in self.nodes:
            self.addNode(toNode)
        self.nodes[fromNode].connectedTo[self.nodes[toNode]] = weight   
        
    def __iter__(self):
        return iter(self.nodes.values())
    
g = Graph()
for i in range(5):
    g.addNode('V'+str(i+1))

g.addEdge('V1','V2',7)
g.addEdge('V1','V3',5)
g.addEdge('V4','V5',4)    

for node in g:
    print(node.id + " connected to " + str([(x.id,node.connectedTo[x]) for x in node.connectedTo]))
    
    
    
