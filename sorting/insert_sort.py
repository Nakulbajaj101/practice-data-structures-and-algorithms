arr = [6,1,3,5,4,10,-1,150]

def insert_sort(arr):
    length = len(arr)
    for i in range(0, length):
        if arr[i] < arr[0]:
            small = arr[i]
            arr[i] = arr[0]
            arr[0] = small
        else:
            for j in range(i+1, length):
                if arr[i] > arr[j]:
                    small = arr[j]
                    arr[j] = arr[i]
                    arr[i] = small
    return arr


insert_sort(arr)