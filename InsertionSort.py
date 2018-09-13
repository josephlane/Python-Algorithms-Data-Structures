# Insertion Sort has a running time of O(n^2)
# This approach is good for small or nearly sorted
# data sources

alist= [1, 4, 3, 5, 6, 2]

def insertionSort(alist):
    for i in range(1, len(alist)):
        tmp = alist[i]
        k = i
        while k > 0 and alist[k - 1] > tmp:
            alist[k] = alist[k-1]
            k -= 1
        alist[k] = tmp
        print alist
        #print " ". join(map(str, alist))

insertionSort(alist)

