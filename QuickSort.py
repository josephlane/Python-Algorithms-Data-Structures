
def quick_sort(array, low, high):
    #base case
    if low >= high:
        return
    mid = partition(array, low, high)
    quick_sort(array, low, mid-1)
    quick_sort(array, mid+1, high)
    return array

def partition(array, low, high):
    #get mid point of array
    mid = (low + high) / 2
    #swap mid and high
    array[mid], array[high] = array[high], array[mid]
    i = low

    #divide and conquer
    for j in range(low, high):
        if array[j] <= array[high]:
            #swap current item
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i

if __name__ == "__main__":
    a = [1,4,-20,9,-100, 3]
    result = quick_sort(a, 0, len(a)-1)
    print result
