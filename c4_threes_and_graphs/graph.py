# Graph = a collection of nodes with edges betwwen(some) of them

from typing import List

class GNode:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children if children is not None else []
        self.visited = False


class Graph:
    def __init__(self):
        self.nodes: List[GNode] = []

    def dfs(self, root):
        print(root.name)
        root.visited = True
        for node in root.children:
            if not node.visited:
                self.dfs(node)

a = GNode(name="a")
b = GNode(name="b")
c = GNode(name="c")
d = GNode(name="d")
e = GNode(name="e")
f = GNode(name="f")
a.children = [b,c]
b.children = [a,e,f]
c.children = [d,e]

gr = Graph()
gr.nodes = [a,b,c,d,e,f]
gr.dfs(gr.nodes[0])

