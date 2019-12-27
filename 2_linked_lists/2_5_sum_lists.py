# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 - > 1 -> 2. That is, 912.

# Solution : do a naturall pass and keep a carrier

from single_linked_list import LLNode

def sum_lists(head1, head2):
    sum_head = None
    carrier = 0
    while head1 is not None and head2 is not None:
        carrier = carrier + head1.data + head2.data
        data = carrier % 10
        carrier = carrier // 10
        if sum_head is None:
            sum_head = LLNode(data)
            sum_tail = sum_head
        else:
            sum_head.add_data(data)
        head1 = head1.next
        head2 = head2.next
    # longer

    longer_head = head1 if head1 is not None else head2

    while longer_head is not None:
        carrier = carrier + longer_head.data
        data = carrier % 10
        carrier = carrier // 10
        if sum_head is None:
            sum_head = LLNode(data)
            sum_tail = sum_head
        else:
            sum_head.add(data)
    return sum_head

head1 = LLNode(7,LLNode(1,LLNode(6)))
print(head1.list())
head2 = LLNode(5,LLNode(9,LLNode(2)))
print(head2.list())
sum_head = sum_lists(head1,head2)
print(sum_head.list())

