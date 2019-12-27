# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e- >f

# Solution -is actually a trick - you move the elements to the left (the data, not the real nodes)

from single_linked_list import LLNode

def delete_midddle_node(node):
    current = node
    while current.next.next is not None:
        current.data = current.next.data
        current = current.next
    current.next = None

head = LLNode(3)
head.add_data(4)
node_c = LLNode(5)
head.add(node_c)
head.add_data(6)
head.add_data(7)
print(head.list())
delete_midddle_node(node_c)
print(head.list())
