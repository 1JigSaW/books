def binarySearch(Array, N, key):
    L = 0
    R = N
    while(L < R):
        mid = (L + R)//2
        if (Array[mid] <= key):
            L = mid + 1
        else:
            R = mid
    return L
    
def binaryInsertionSort(Array):
    for i in range (1,len(Array)):
        key = Array[i]
        pos = binarySearch(Array, i, key)
        
        j = i
        
        while(j > pos):
            Array[j] = Array[j-1]
            j = j-1
        
        Array[pos] = key
        print("The array after",i,"iterations =", *Array)