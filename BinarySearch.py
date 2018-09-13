import math

def binary_search(array, start, end, value):

    if start > end:
        return False

    mid = (int(start) + int(end)) / 2

    if value == array[mid]:
        return True
    
    if value < array[mid]:
        return binary_search(array, start, mid, value)
    else:
        return binary_search(array, mid+1, end, value)

    #return False


a = []
start = 0
end = len(a) - 1

print binary_search(a, start, end, 2)
