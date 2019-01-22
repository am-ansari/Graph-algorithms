# -*- coding: utf-8 -*-

class Vertex(object):
    
    # Each vertex has a key value and a dictionary containing it's connected 
    # vertices
    def __init__(self,key):
        
        self.id = key
        self.edgeTo = {}
    
    # Adding edge to the vertex and storing the weights as dictionary values 
    # in the vertex object    
    def addNeighbor(self,nbrKey,weight=0):
        self.edgeTo[nbrKey] = weight
    
    # Return all the connected vertices     
    def getEdges(self):
        return self.edgeTo.keys()
    
    # Return the key value of the vertex object
    def getId(self):
        return self.id
    
    # Return the weight of the connected edge to the neighbour of the vertex 
    # object
    def getWeight(self,nbrKey):
        return self.edgeTo[nbrKey]
    
class Graph(object):
    
    # Initialize graph object containing empty dictionary for vertices 
    # and initialize vertices count to 0
    def __init__(self):
        self.verticesList = {}
        self.verticesCount = 0
    
    def __contains__(self,key):
        return key in self.verticesList
    
    # Create a new vertex object and add this object to vertices dictionary and
    # increment vertices count by 1; return newly created vertex object    
    def addVertex(self,key):
        newVertex = Vertex(key)
        self.verticesList[key] = newVertex
        self.verticesCount += 1
        return newVertex
    
    # Retrieve vertex object by passing the key value (vertex id)
    def getVertex(self,key):
        if key in self.verticesList:
            return self.verticesList[key]
        else:
            return None
    
    # Create an edge between two vertices and create new vertex objects if any
    # of them is missing
    def addEdge(self,fromVertex,toVertex,weight=0):
        if fromVertex not in self.verticesList:
            newVertex = self.addVertex(fromVertex)
        if toVertex not in self.verticesList:
            newVertex = self.addVertex(toVertex)
            
        # Call the method addNeighbor of Vertex class to create an edge 
        # between the two edges
        self.verticesList[fromVertex].addNeighbor(self.verticesList[toVertex], weight)
    
    # Retrieve all the vertices of the graph object
    def getVertices(self):
        return self.verticesList.keys()
    
    # Written to iterate over graph object values (vertex objects)
    def __iter__(self):
        return iter(self.verticesList.values())
    
g = Graph()

for i in range(10):
    g.addVertex('V'+str(i+1))

#print(g.getVertices())
#print("\n")
#print(g.verticesList)
g.addEdge('V1','V2',7)
g.addEdge('V1','V3',5)
g.addEdge('V4','V5',4)
g.addEdge('V6','V7',9)
g.addEdge('V6','V3',1)
g.addEdge('V6','V8',2)
print("\n")
for vertex in g:
    print (str(vertex.getId()) + " : " + str([(x.id,vertex.getWeight(x)) for x in vertex.getEdges()]))
