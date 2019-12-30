# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C - > D -> E -> C [the same C as earlier]
# Output: C
# Hints: #50, #69, #83, #90

#Solution: keep a set of the adresse of the objects. If we point to an object in the set ... that is the element
from single_linked_list import LLNode

def find_loop(head):
    nodes_set = set()
    if head.next is None:
        return None
    while head.next is not None and head not in nodes_set:
        nodes_set.add(head)
        head = head.next
    return head

tail_node = LLNode(9)
cycle_head = LLNode(6, LLNode(7,LLNode(8, tail_node)))
head = LLNode(3,LLNode(4,LLNode(5,cycle_head)))
tail_node.next = cycle_head


found_head = find_loop(head)
print(found_head)
print(cycle_head)

found_head = find_loop(cycle_head)
print(found_head)
print(cycle_head)