def merge(initial, helper, low, middle, high):
    pass

def merge_sorter(initial, helper, low, high):
    if low < high:
        middle = (low + high) // 2
        merge_sorter(initial,  helper, low, middle)
        merge_sorter(initial, helper, middle+1, high)
        merge(initial, helper, low, middle, high)


def merge(initial, helper, low, middle, high):
    #copy to helper
    helper[low:high+1] = initial[low:high+1]
    #merge but sorted to initial
    helper_left = low
    helper_right = middle +1
    current = low
    while (helper_left <= middle) and (helper_right <= high):
        if helper[helper_left] < helper[helper_right]:
            initial[current] = helper[helper_left]
            helper_left +=1
        else:
            initial[current] = helper[helper_right]
            helper_right +=1
        current +=1
    #copy the remaining left side ( the right side is there anyay
    remaining = middle - helper_left +1
    initial[current: current + remaining] = helper[helper_left:helper_left + remaining]


def merge_sort(initial):
    helper = [None]*len(initial)
    merge_sorter(initial, helper, 0, len(initial)-1)
    return initial



initial = [2,4,1,6,7]
print(initial)
print(merge_sort(initial))
print(initial)