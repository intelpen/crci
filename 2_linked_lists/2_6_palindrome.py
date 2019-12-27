# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

# Solution - double linked list would be great here
# otherwise compare kth with kth from end

#Alternative solution :reverse list and compare with its reverse
from single_linked_list import LLNode

def reverse(head):
    if head.next is None:
        return LLNode(head.data)
    else:
        new_head = reverse(head.next)
        new_head.add_data(head.data)
        return new_head

def palindrom(head):
    reversed_head = reverse(head)
    while head.next is not None:
        if head.data != reversed_head.data:
            return False
        head=  head.next
        reversed_head = reversed_head.next
    return True

head = LLNode(1,LLNode(2,LLNode(3,LLNode(2,LLNode(1)))))

print(reverse(head).list())
print(palindrom(head))

