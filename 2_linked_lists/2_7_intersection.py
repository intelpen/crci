# 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

# Solution: verify all node from first with all node from second
# Observation: If single linked list, if one node is the same, all the rest of the list is the same - kind as like a Y
# Then Short Solution - verify if tails are the same element >---* then the 2 list are identical

from single_linked_list import LLNode

def tail(head):
    while head.next is not None:
        head = head.next
    return head

def intersect(head_first, head_second):
    tail_first = tail(head_first)
    tail_second = tail(head_second)
    return tail_first == tail_second

common_head = LLNode(1, LLNode(2, LLNode(3, LLNode(4, LLNode(5)))))
head_first = LLNode(2, common_head)
head_second = LLNode(10,LLNode(5))
print(common_head.list())
print(intersect(head_first, head_second))