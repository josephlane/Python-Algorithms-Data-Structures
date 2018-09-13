def BubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                #swap
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

if __name__ == '__main__':
    a = [24, 0, -10, 33, 21, -19]
    res = BubbleSort(a)
    print res
