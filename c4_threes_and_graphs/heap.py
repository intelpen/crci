# Heap = complete binary tree where each node is smaller than its childrens
# Complete == totally filled other than the righmost elements on the last level

# Operations -
#  - 1.insert(buble up),
#  - 2. Extract Minimum(exchange rootwith  last element then swim up)

# Implementation - the heap is easy to implement with an array because the elemnts are at fixed positions

class Heap():
    def __init__(self):
        self.data = []

    def root_i(self, index_node: int) -> int:
        return (index_node-1) // 2

    def left_child_i(self, index_node: int) -> int:
        return index_node*2+1

    def right_child_i(self, index_node: int) -> int:
        return index_node*2+2

    def swap(self, index_1, index_2):
        aux = self.data[index_1]
        self.data[index_1] = self.data[index_2]
        self.data[index_2] = aux

    def insert(self, element: int) -> int:
        #insert in last position
        self.data.append(element)
        #bubble up
        current = len(self.data) -1
        while self.data[current] < self.data[self.root_i(current)] and current>0:
            self.swap(current, self.root_i(current))
            current = self.root_i(current)

    def extract_min(self):
        #root is min always
        result = self.data[0]
        #move last to root
        self.data[0] = self.data[len(self.data)-1]
        #swimdown root , always swap with minimum element (there is no ordering on the same line)
        current = 0
        while current < len(self.data) // 2 -1 :
            min_son_i = self.left_child_i(current) if self.data[self.left_child_i(current)] < self.data[self.right_child_i(current)] else self.right_child_i(current)
            self.swap(min_son_i, current)
            current = min_son_i
        #remove last
        self.data.pop()
        return result

my_list = [1,2,3,4,5,6,7]
my_heap = Heap()
for element in my_list:
    my_heap.insert(element)
    print(my_heap.data)
print(my_heap.data)

print(my_heap.extract_min())
print(my_heap.data)

print(my_heap.extract_min())
print(my_heap.data)

print(my_heap.extract_min())
print(my_heap.data)

print(my_heap.extract_min())
print(my_heap.data)

print(my_heap.extract_min())
print(my_heap.data)

print(my_heap.extract_min())
print(my_heap.data)








