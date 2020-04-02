import random

class Node:
    def __init__(self, value=None, edges=None):
        self.val = value
        if edges is None:
            self.edges = {}
        else:
            self.edges = edges


class Graph:
    def __init__(self):
        self.Nodes = {}

    def addNode(self, nodeVal):
        self.Nodes[nodeVal] = Node(nodeVal)

    def addUndirectedEdge(self, first, second):
        if first.val in self.Nodes:
            self.Nodes[first.val].edges[second.val] = second
        if second.val in self.Nodes:
            self.Nodes[second.val].edges[first.val] = first

    def removeUndirectedEdge(self, first, second):
        if first.val in self.Nodes:
            del self.Nodes[first.val].edges[second.val]
        if second.val in self.Nodes:
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
    prev = None
    for i in range(n):
        g.addNode(i)
        if prev is not None:
            g.addUndirectedEdge(g.Nodes[i], g.Nodes[prev])
        prev = i
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
    l = []
    q = []
    for i in graph.Nodes.values():
        if i not in visited:
            q.append(i)
            visited.add(i)
            BFTRecHelper(visited, q, l)
    return l

def BFTRecHelper(visited, q, l):
    if len(q) == 0:
        return
    cur = q.pop(0)
    l.append(cur)
    for i in cur.edges.values():
        if i not in visited:
            q.append(i)
            visited.add(i)
    BFTRecHelper(visited, q, l)

def BFTIter(graph):
    if graph is None:
        return None
    if len(graph.Nodes) == 0:
        return []
    l = []
    q = []
    visited = set()
    for i in graph.Nodes.values():
        if i not in visited:
            q.append(i)
            visited.add(i)
            cur = q.pop(0)
            while cur:
                l.append(cur)
                for j in cur.edges.values():
                    if j not in visited:
                        q.append(j)
                        visited.add(j)
                if len(q) > 0:
                    cur = q.pop(0)
                else:
                    cur = None
    return l

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

n = 10000
g = createLinkedList(n)
temp = BFTIterLinkedList(g)
if temp is not None:
    for i in temp:
        print(i.val)

