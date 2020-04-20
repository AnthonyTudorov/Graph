import random
from Node import Node
from GraphInterface import GraphInterface


class DirectedGraph(GraphInterface):
    def __init__(self):
        self.Nodes = {}

    def addNode(self, nodeVal):
        self.Nodes[nodeVal] = Node(nodeVal)

    def addDirectedEdge(self, first, second):
        if first.val in self.Nodes and second.val in self.Nodes:
            self.Nodes[first.val].edges[second.val] = second

    def removeDirectedEdge(self, first, second):
        if first.val in self.Nodes:
            del self.Nodes[first.val].edges[second.val]

    def getAllNodes(self):
        return set(self.Nodes.values())


def createRandomDAGIter(n):
    g = DirectedGraph()
    for i in range(n):
        g.addNode(i)
    for i in range(n):
        for j in random.sample(range(n), random.randint(0, n - 1)):
            g.addDirectedEdge(g.Nodes[i], g.Nodes[j])

    # BFT where directed edges are removed to ensure acyclic nature
    q = []
    visited = set()
    for i in g.Nodes.values():
        if i not in visited:
            curcyclevisited = set()
            q.append(i)
            visited.add(i)
            cur = q.pop(0)
            while cur:
                curcyclevisited.add(cur)
                toremove = []
                for j in cur.edges.values():
                    if j not in visited:
                        q.append(j)
                        visited.add(j)
                    if j in curcyclevisited:
                        toremove.append(j)
                for j in toremove:
                    g.removeDirectedEdge(cur, j)
                if len(q) > 0:
                    cur = q.pop(0)
                else:
                    cur = None
    return g


class TopSort:
    def Kahns(g):
        if g is None:
            return None
        if len(g.Nodes) == 0:
            return []

        #  initialize dictionary of [node, number of incoming edges] pairs
        nodedegrees = g.Nodes.copy()
        for i in g.Nodes.values():
            nodedegrees[i.val] = [i, 0]

        #  count incoming edges
        for i in g.Nodes.values():
            for j in i.edges.values():
                nodedegrees[j.val][1] += 1

        kahnsqueue = []
        for i in nodedegrees.values():
            if i[1] == 0:
                kahnsqueue.append(i[0])

        returnlist = []
        while kahnsqueue:
            temp = kahnsqueue.pop(0)
            nodedegrees[temp.val][1] -= 1
            returnlist.append(temp)
            for i in temp.edges.values():
                nodedegrees[i.val][1] -= 1
                if nodedegrees[i.val][1] == 0:
                    kahnsqueue.append(i)
        return returnlist

    def mDFS(g):
        if g is None:
            return None
        if len(g.Nodes) == 0:
            return []
        visited = set()
        path = []
        sorted = []
        cur = g.Nodes[0]
        for i in g.Nodes.values():
            if i not in visited:
                cur = i
                while cur:
                    visited.add(cur)
                    change = False
                    for j in cur.edges.values():
                        if j not in visited:
                            path.append(cur)
                            cur = j
                            change = True
                            break
                    if not change:
                        if len(path) > 0:
                            sorted.append(cur)
                            cur = path.pop()
                        else:
                            sorted.append(cur)
                            cur = None
        return sorted[::-1]


g = createRandomDAGIter(1000)

temp = TopSort.Kahns(g)
if temp is not None:
    for i in temp:
        print(i.val, end='')
print()

temp = TopSort.mDFS(g)
if temp is not None:
    for i in temp:
        print(i.val, end='')
print()
