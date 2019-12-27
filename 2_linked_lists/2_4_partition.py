# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# Hints: #3, #24

#solution -> use a smaller and a bigger list and the reunite them . keeping both head and tail would be great

from single_linked_list import LLNode
def partition(head, element_data):
    smaller_head = None
    bigger_head = None
    current = head
    while current is not None:
        if current.data < element_data:
            #add element in the smaller list
            if smaller_head is None:
                smaller_head = LLNode(current.data)
                smaller_tail = smaller_head
            else:
                smaller_tail.add_data(current.data)
                smaller_tail = smaller_tail.next

        else:
            # add element to the bigger list
            bigger_head = LLNode(current.data, bigger_head)
        current = current.next
    #merge the two lists
    smaller_tail.next = bigger_head
    print(smaller_head.list())
    return smaller_head

head = LLNode(7,LLNode(4,LLNode(5,LLNode(2,LLNode(7,LLNode(3))))))
print(head.list())
partition_head = partition(head, 6)


