#alist= [1, 4, 3, 5, 6, 2]
#alist = [2, 1, 3, 1, 2]
#alist = [1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]
alist = [10, 9, 8,7 ,6 ,5 ,4 ,3 ,2 ,1]
blist = [10, 9, 8,7 ,6 ,5 ,4 ,3 ,2 ,1]

def QuickSort(a, start, end):
    if start < end:
        pIndex = Partition(a, start, end)
        QuickSort(a, start, pIndex)
        QuickSort(a, pIndex+1, end)

def Partition(a, start, end):
    s = 0
    pivot = a[end-1]
    pIndex = start
    for i in range(start, end-1):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex+=1
            s+=1
    swap(a, end-1, pIndex)
    #print " ".join(map(str, a))
    return pIndex

def swap(a, i, e):
    temp = a[i]
    a[i] = a[e]
    a[e] = temp
    
def insertionSort(alist):
    for i in range(1, len(alist)):
        tmp = alist[i]
        k = i
        while k > 0 and alist[k - 1] > tmp:
            alist[k] = alist[k-1]
            n+=1
            k -= 1
        alist[k] = tmp
n = insertionSort(alist)
s = QuickSort(blist, 0, len(blist))
print n - s
