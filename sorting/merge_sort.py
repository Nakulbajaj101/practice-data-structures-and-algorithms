def selection_sort(arr):
    length = len(arr)
    for i in range(0, length):
        minimum = i
        for j in range(i, length):
            if arr[i] > arr[j]:
                minimum = j
                temp = arr[i]
                arr[i] = arr[minimum]
                arr[minimum] = temp
    return arr

def merge_sort1(arr):
    length = len(arr)
    if length <= 2:
        if length == 1:
            return [arr[0]]
        else:
            return [min(arr), max(arr)]
    else:
        middle_index = int(length/2)
        return selection_sort(merge_sort1(arr[0:middle_index]) + merge_sort1(arr[middle_index:]))

def merge_sort(arr):
    length = len(arr)
    if length <= 2:
        if length == 1:
            return [arr[0]]
        else:
            return [min(arr), max(arr)]
    else:
        middle_index = int(length/2)
        return merge(merge_sort(arr[0:middle_index]), merge_sort(arr[middle_index:]))

def merge(arr1, arr2):
    left_index = 0
    right_index = 0
    updated_arr = []
    while left_index < len(arr1) and right_index < len(arr2):
        if arr1[left_index] < arr2[right_index]:
            updated_arr.append(arr1[left_index])
            left_index += 1
        else:
            updated_arr.append(arr2[right_index])
            right_index += 1
    
    if left_index < len(arr1):
        updated_arr = updated_arr + arr1[left_index:]
    elif right_index < len(arr2):
        updated_arr = updated_arr + arr2[right_index:]
    else:
        updated_arr
    return updated_arr


if __name__ == "__main__":
    arr = [10, 6, 5, 11, 4, 20, 30, 25]
    print(merge_sort1(arr))
    print(merge_sort(arr))
