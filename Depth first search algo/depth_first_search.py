# -*- coding: utf-8 -*-

from collections import OrderedDict
         

class Node:

    def __init__(self, key):
        self.id = key
        self.connectedTo = OrderedDict()  
        self.status = 'univisited'
        
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
        return self.nodes
    
    def __iter__(self):
        return iter(self.nodes.values())
        
g = Graph()
g.addEdge('A','B')
g.addEdge('A','D')
g.addEdge('B','E')
g.addEdge('C','E')
g.addEdge('C','F')
g.addEdge('D','B')
g.addEdge('E','D')
g.addEdge('F','F')

def dfs(G):
    
    visited = []
        
    for vertex in G:
        
        if vertex.status == 'univisited':
            visited.append(vertex) 
            vertex.status = 'visited'
            dfsVisit(G, vertex, visited)
            
    return visited

def dfsVisit(G,node=None, visited=None):
    if visited == None:
        visited = []
    for adjV in node.connectedTo:
        adjV.status = 'visiting'
        print("Checking adjacent vertices")
        print('Vertex: '+node.id + " | " + "Status: "+node.status)
        print("Adj V :"+adjV.id)
        if adjV not in visited:
            print('Vertex: '+adjV.id + " | " + "Status: "+adjV.status)
            visited.append(adjV) 
            adjV.status = 'visited'
            dfsVisit(G, adjV, visited)
        else:
            print("Already visited")
    
    return visited

v = dfs(g)
print("\n\nDFS path from first to last node")
for i in v:
    print(i.id,end=" ")
    

    
