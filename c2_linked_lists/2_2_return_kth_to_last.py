# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

#Solution : usualy recursive

from single_linked_list import LLNode

def is_nth(node, k):
    if node.next is None:
        return (None,1)
    else:
        order = is_nth(node.next,k)
        if order[1] < k:
            return (order[0], order[1]+1)
        else:
            if order[1] ==k:
                return (node.data, k)
            else:
                return(order[0], k)

head = LLNode(4)
head.add_data(5)
head.add_data(6)
head.add_data(6)
head.add_data(7)
head.add_data(8)
print(head.list())
print(is_nth(head, 4))
