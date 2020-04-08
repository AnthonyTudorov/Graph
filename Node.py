class Node:
    def __init__(self, value=None, edges=None):
        self.val = value
        if edges is None:
            self.edges = {}
        else:
            self.edges = edges
