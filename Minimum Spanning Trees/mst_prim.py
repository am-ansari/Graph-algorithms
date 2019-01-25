# -*- coding: utf-8 -*-
class Node:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  
        
class Graph:

    def __init__(self):
        self.nodes = {}

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
        self.nodes[toNode].connectedTo[self.nodes[fromNode]] = weight
    
    def getNode(self, key):
        return self.nodes[key]
    
    def getWeight(self,fromNode, toNode):
        return self.nodes[fromNode].connectedTo[self.nodes[toNode]]
    
    def __iter__(self):
        return iter(self.nodes.values())
    
    def __len__(self):
        return len(self.nodes.keys())
    
def genMST(G,start):
    mstG=Graph()
    startV = G.getNode(start)
    visited = []
    visited.append(startV)
    while len(visited) <= len(G):
        minEdge, minWt = extractMin(G,visited)
        if minEdge[0] == minEdge[1]:
            break
        visited.append(minEdge[1])
        mstG.addEdge(minEdge[0].id,minEdge[1].id,minWt)  
    return mstG

def extractMin(G,visited):
    wtDict = {}
    minWt = 999999
    for vert in G:
        minV = vert
        if vert in visited:
            parent = vert
            for adjV in parent.connectedTo:
                if parent.connectedTo[adjV] < minWt and adjV not in visited:
                    minWt = parent.connectedTo[adjV]
                    minV = adjV         
            wtDict[(parent,minV)] = minWt
    
    return min(wtDict, key=wtDict.get), min(wtDict.values())        

def printMst(graph):
    visited = set()
    minWt = 0
    print("Edge    Weight")
    print("-"*14)
    for vert in graph.nodes.values():
        visited.add(vert)
        for adjV in vert.connectedTo:
            if adjV not in visited:
                visited.add(adjV)
                print(str(vert.id) + " -- " + str(adjV.id),end = "   ")
                print(str(graph.getWeight(vert.id,adjV.id)))
                minWt += graph.getWeight(vert.id,adjV.id)
    print("-"*14)
    print("Min Wt   ",end = "")
    print(str(minWt))            
                
                
if __name__ == "__main__":
    
    g = Graph()
    g.addEdge('A','B',4)
    g.addEdge('A','H',8)
    g.addEdge('B','H',11)
    g.addEdge('B','C',8)
    g.addEdge('C','I',2)
    g.addEdge('C','F',4)
    g.addEdge('C','D',7)
    g.addEdge('D','E',9)
    g.addEdge('D','F',14)
    g.addEdge('E','F',10)
    g.addEdge('G','F',2)
    g.addEdge('G','H',1)
    g.addEdge('I','H',7)
    g.addEdge('I','G',6)
                   
    mstGraph = genMST(g,'A')  
    
    printMst(mstGraph)
    
