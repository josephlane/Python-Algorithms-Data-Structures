def bubblesort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                
    return list
    
                
def selectionsort(list):
    for passnum in range(len(list)-1,0,-1):
        max = 0
        for i in range(1,passnum+1):
            if list[max] < list[i]:
                max = i
        list[passnum], list[max] = list[max], list[passnum]
    return list

def insertionsort(list):
    for i in range(len(list)):
        elt = list[i] 
        j = i 
        while j > 0 and list[j-1] > elt:
            list[j] = list[j-1]
            j = j - 1
        list[j] = elt
    return list

def merge(list1, list2):
    list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list.append(list1[i])
            i = i + 1
        else:
            list.append(list2[j])
            j = j + 1
            
    if i < len(list1):
        list.extend(list1[i:])
    elif j < len(list2):
        list.extend(list2[j:])
        
    return list

def mergesort(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) / 2
    
    left = list[:mid]
    right = list[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
