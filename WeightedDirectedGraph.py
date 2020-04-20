import random
import math
from Node import Node
from GraphInterface import GraphInterface


class WeightedDirectedGraph(GraphInterface):
    def __init__(self):
        self.Nodes = {}

    def addNode(self, nodeVal):
        self.Nodes[nodeVal] = Node(nodeVal)

    def addDirectedEdge(self, first, second, edgeWeight):
        if first.val in self.Nodes and second.val in self.Nodes:
            self.Nodes[first.val].edges[second.val] = [second, edgeWeight]

    def removeDirectedEdge(self, first, second):
        if first.val in self.Nodes:
            del self.Nodes[first.val].edges[second.val]

    def getAllNodes(self):
        s = set()
        for i in self.Nodes.values():
            s.add(i[0])
        return s


def createRandomCompleteWeightedGraph(n):
    MAXWEIGHT = 10000
    g = WeightedDirectedGraph()
    for i in range(n):
        g.addNode(i)
    for i in range(n):
        n1 = g.Nodes[i]
        for j in range(i+1, n):
            n2 = g.Nodes[j]
            g.addDirectedEdge(n1, n2, random.randint(0, MAXWEIGHT))
            g.addDirectedEdge(n2, n1, random.randint(0, MAXWEIGHT))


def createLinkedList(n):
    MAXWEIGHT = 10000
    g = WeightedDirectedGraph()
    if n > 0:
        g.addNode(0)
        for i in range(n-1):
            g.addNode(i+1)
            g.addDirectedEdge(g.Nodes[i], g.Nodes[i+1], random.randint(0, MAXWEIGHT))


def dijkstras(start):
    if start is None:
        return None
    finished = {}
    d = {}
    min = math.inf
    for i in start.edges.values():
        if i[1] < math.inf:
            #  do something
            


