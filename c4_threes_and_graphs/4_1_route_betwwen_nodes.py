# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

#Solution - any traversal
from c4_threes_and_graphs.graph import GNode, Graph

def conected(graph, node_start, node_end):
    graph.dfs(node_start)
    return node_end.visited

a = GNode(name="a")
b = GNode(name="b")
c = GNode(name="c")
d = GNode(name="d")
e = GNode(name="e")
f = GNode(name="f")
g = GNode(name="g")
a.children = [b,c]
b.children = [a,e,f]
c.children = [d,e]

gr = Graph()
gr.nodes = [a,b,c,d,e,f,g]

print(conected(gr, a, f))
print(conected(gr, a, g))


