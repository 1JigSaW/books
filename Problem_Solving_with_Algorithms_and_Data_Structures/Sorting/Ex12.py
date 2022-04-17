def selectionSort(alist):
    min_el = 1
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        positionOfMin=len(alist)-1
        for location in range(min_el,fillslot+1):
            if alist[location]<alist[positionOfMin]:
                positionOfMin = location

        temp = alist[min_el]
        alist[min_el] = alist[positionOfMin]
        alist[positionOfMin] = temp

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)