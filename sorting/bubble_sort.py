arr = [1,5,2,13,4]

def bubble_sort(arr: list):
    counter = 0
    while (counter < len(arr) - 1):
        for i in range(counter, len(arr)-1):
            if arr[i] > arr[i+1]:
                lower = arr[i+1]
                higher = arr[i]
                arr[i+1] = higher
                arr[i] = lower
        counter += 1
            
    return arr

def bubble_sort2(arr):
    arr_length = len(arr)

    for i in range(0, arr_length-1):
        for j in range(i, arr_length-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


print(bubble_sort(arr))
print(bubble_sort2(arr))
