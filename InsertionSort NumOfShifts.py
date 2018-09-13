#alist= [1, 4, 3, 5, 6, 2]
#alist = [2, 1, 3, 1, 2]
#alist = [1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]
alist = [10, 9, 8,7 ,6 ,5 ,4 ,3 ,2 ,1]

def insertionSort(alist):
    n = 0
    for i in range(1, len(alist)):
        tmp = alist[i]
        k = i
        while k > 0 and alist[k - 1] > tmp:
            alist[k] = alist[k-1]
            n+=1
            k -= 1
        alist[k] = tmp
    print n

insertionSort(alist)
