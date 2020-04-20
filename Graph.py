import random
from Node import Node
from GraphInterface import GraphInterface


class Graph(GraphInterface):
    def __init__(self):
        self.Nodes = {}

    def addNode(self, nodeVal):
        self.Nodes[nodeVal] = Node(nodeVal)

    def addUndirectedEdge(self, first, second):
        if first.val in self.Nodes and second.val in self.Nodes:
            self.Nodes[first.val].edges[second.val] = second
            self.Nodes[second.val].edges[first.val] = first

    def removeUndirectedEdge(self, first, second):
        if first.val in self.Nodes and second.val in self.Nodes:
            del self.Nodes[first.val].edges[second.val]
            del self.Nodes[second.val].edges[first.val]

    def getAllNodes(self):
        return set(self.Nodes.values())


def createRandomUnweightedGraphIter(n):
    g = Graph()
    for i in range(n):
        g.addNode(i)
    for i in range(n):
        for j in random.sample(range(n), random.randint(0, n-1)):
            if j > i:
                g.addUndirectedEdge(g.Nodes[i], g.Nodes[j])
    return g


def createLinkedList(n):
    g = Graph()
    if n > 0:
        g.addNode(0)
        for i in range(1, n):
            g.addNode(i)
            g.addUndirectedEdge(g.Nodes[i], g.Nodes[i-1])
    return g


def DFSRec(start, end):
    if start == end:
        return [start]
    return DFSRecHelper(start, end, set())


def DFSRecHelper(cur, end, visited):
    if cur is None:
        return None
    if cur == end:
        return [end]
    visited.add(cur)
    temp = None
    for i in cur.edges.values():
        if i not in visited:
            temp = DFSRecHelper(i, end, visited)
        if temp is not None:
            temp = [cur] + temp
            return temp
    return None


def DFSIter(start, end):
    if start == end:
        return [start]
    visited = set()
    path = []
    cur = start
    while cur:
        if cur == end:
            path.append(cur)
            break
        visited.add(cur)
        change = False
        for i in cur.edges.values():
            if i not in visited:
                path.append(cur)
                cur = i
                change = True
                break
        if not change:
            if len(path) > 0:
                cur = path.pop()
            else:
                return None
    return path


def BFTRec(graph):
    if graph is None:
        return None
    if len(graph.Nodes) == 0:
        return []
    visited = set()
    traversallist = []
    traversalqueue = []
    for i in graph.Nodes.values():
        if i not in visited:
            traversalqueue.append(i)
            visited.add(i)
            BFTRecHelper(visited, traversalqueue, traversallist)
    return traversallist


def BFTRecHelper(visited, traversalqueue, traversallist):
    if len(traversalqueue) == 0:
        return
    cur = traversalqueue.pop(0)
    traversallist.append(cur)
    for i in cur.edges.values():
        if i not in visited:
            traversalqueue.append(i)
            visited.add(i)
    BFTRecHelper(visited, traversalqueue, traversallist)


def BFTIter(graph):
    if graph is None:
        return None
    if len(graph.Nodes) == 0:
        return []
    returnlist = []
    traversalqueue = []
    visited = set()
    for i in graph.Nodes.values():
        if i not in visited:
            traversalqueue.append(i)
            visited.add(i)
            while len(traversalqueue) > 0:
                cur = traversalqueue.pop(0)
                returnlist.append(cur)
                for j in cur.edges.values():
                    if j not in visited:
                        traversalqueue.append(j)
                        visited.add(j)
    return returnlist


def BFTRecLinkedList(graph):
    if graph is None:
        return None
    if len(graph.Nodes) == 0:
        return []
    return BFTRecLinkedListHelper(graph.Nodes[0])


def BFTRecLinkedListHelper(cur):
    if len(cur.edges) == 1:
        if cur.val == 0:
            return [cur] + BFTRecLinkedListHelper(cur.edges[1])
        return [cur]
    return [cur] + BFTRecLinkedListHelper(cur.edges[cur.val + 1])


def BFTIterLinkedList(graph):
    return graph.Nodes.values()


n = 10
n1 = 10000
g = createRandomUnweightedGraphIter(n)
g1 = createLinkedList(n)
#  g2 = createLinkedList(n1)

temp = DFSRec(g.Nodes[0], g.Nodes[n-1])
if temp is not None:
    for i in temp:
        print(i.val, end='')
print()

temp = DFSIter(g.Nodes[0], g.Nodes[n-1])
if temp is not None:
    for i in temp:
        print(i.val, end='')
print()

temp = BFTRec(g)
if temp is not None:
    for i in temp:
        print(i.val, end='')
print()

temp = BFTIter(g)
if temp is not None:
    for i in temp:
        print(i.val, end='')
print()

# temp = BFTRecLinkedList(g2)
# if temp is not None:
#     for i in temp:
#         print(i.val, end='')
print()

temp = BFTIterLinkedList(g1)
if temp is not None:
    for i in temp:
        print(i.val, end='')
print()
