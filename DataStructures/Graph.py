class DirectedGraph():
    """
    A class representing the Directed Graph data structure.

    - Constructor parameters:

    - Attributes:
    
    - Behaviours:

    """
    def __init__(self, map:dict = None) -> None:
        if map is None:
            self.AdjLists = dict()          # Adjacency Lists
            self.V = dict()                 # Number of Vertices
            self.AdjMat = list()            # Adjacency Matrix
        # TO BE IMPLEMENTED:
        # elif type(map) is type(dict()):
        #     self.AdjLists = addAllEdges(map)
        #     self.V = len(map)
        #     self.AdjMat = createMatrix(map)
    
    def updateNodeList(self, from_node, to_node, weight):
        self.AdjLists.get(from_node).append([to_node, weight])
        self.V.update({to_node:(len(self.V) + 1)})
    
    # TO BE COMPLETED:
    def addEdge(self, from_node, to_node, weight=1):
        if len(self.V) == 0:
            self.AdjLists.update({from_node:[[to_node, weight]]})
            self.V.update({from_node:1, to_node:2})
            self.AdjMat.append([]*len(self.V))
            self.AdjMat.append([]*len(self.V))
        else:
            if from_node in self.AdjLists.keys():
                self.updateNodeList(from_node, to_node, weight)
            else:
                self.AdjLists.update({from_node:[[to_node, weight]]})

# Test
if __name__ == "__main__":
    g = DirectedGraph()
    g.addEdge("A","B")
    g.addEdge("A","C",2)
    g.addEdge("D","A")
    print(g.AdjLists)
    print(g.AdjMat)