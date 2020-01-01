# In quick sort we pick a random element and partition the array such that all numbers that are less than the
# partitioning element come before all elements that are greater than it. The partitioning can be performed  through a
# series of swaps

def quicksort(data, left, right):
    partition_index = partition(data, left, right)
    if left < partition_index:
        quicksort(data, left, partition_index-1)
    if partition_index < right:
        quicksort(data, partition_index, right)


def partition(data, left, right ):
    # choose the middle element and weave it to the right position
    pivot = data[(left+right)//2]
    while left < right:
        while data[left] < pivot:
            left +=1
        while data[right] > pivot:
            right -=1
        if left <= right:
            #swap
            temp = data[left]
            data[left]=data[right]
            data[right] = temp
            left +=1
            right -=1
    return left


data = [2,1,5,3,6]
print(data)
quicksort(data, 0, len(data)-1)
print(data)