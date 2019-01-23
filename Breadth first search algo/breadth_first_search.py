# -*- coding: utf-8 -*-

from collections import OrderedDict
         

class Node:

    def __init__(self, key):
        self.id = key
        self.connectedTo = OrderedDict()  
        self.status = 'unvisited'
        
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
    
    def getNode(self, key):
        return self.nodes[key]
    
    def __iter__(self):
        return iter(self.nodes.values())
        
g = Graph()
g.addEdge('A','B')
g.addEdge('A','E')
g.addEdge('B','A')
g.addEdge('B','F')
g.addEdge('C','F')
g.addEdge('C','G')
g.addEdge('C','D')
g.addEdge('D','C')
g.addEdge('D','G')
g.addEdge('D','H')
g.addEdge('E','A')
g.addEdge('F','C')
g.addEdge('F','G')
g.addEdge('G','C')
g.addEdge('G','D')
g.addEdge('G','H')
g.addEdge('G','F')
g.addEdge('H','D')
g.addEdge('H','G')

def bfs(G,start):
    startingVertex = G.getNode(start)
    queue = []
    queue.append(startingVertex)
    visited = []
    while queue:
        print("\nQueue: ",end=" ")
        for val in queue:
            print(str(val.id),end=" ")
        print("")    
        currentVertex = queue.pop(0)
        currentVertex.status = 'visiting'
        print("Checking adjacent vertices")
        print('Vertex: '+currentVertex.id + " | " + "Status: "+currentVertex.status)
        for adjV in currentVertex.connectedTo:
            print('Adj Vertex: '+adjV.id + " | " + "Status: "+adjV.status)
            if adjV.status == 'unvisited':
                queue.append(adjV)
                adjV.status = 'visiting'
        currentVertex.status = 'visited'
        visited.append(currentVertex.id)
        
    return visited

startingVertex = 'A'    
path = bfs(g,startingVertex)
print("\n\nBFS path from vertex "+startingVertex)
print(path)


    
