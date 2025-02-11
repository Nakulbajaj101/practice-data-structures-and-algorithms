def create_left_right_array(arr):
    length_arr = len(arr)
    pivot_idx = length_arr-1
    pivot = arr[pivot_idx]
    arr1 = []
    arr2 = []
    for i in range(0, pivot_idx):
        if arr[i] < pivot:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    arr1.append(pivot)
    if not arr1 or not arr2:
        middle_idx = int(length_arr/2)
        arr1 = arr[0:middle_idx]
        arr2 = arr[middle_idx:]
    return arr1, arr2

def merge(arr1, arr2):
    left_arr_idx = 0
    right_arr_idx = 0
    result = []
    while left_arr_idx < len(arr1) and right_arr_idx < len(arr2):
        if arr1[left_arr_idx] < arr2[right_arr_idx]:
            result.append(arr1[left_arr_idx])
            left_arr_idx += 1
        else:
            result.append(arr2[right_arr_idx])
            right_arr_idx += 1
    result = result + arr1[left_arr_idx:] + arr2[right_arr_idx:]
    return result



def quick_sort(arr):
    if len(arr) <= 2:
        if len(arr) == 2:   
            if arr[0] > arr[1]:
                return [arr[1], arr[0]]
            return arr
        else:
            return arr
    else:
        arr1, arr2 = create_left_right_array(arr)

    return merge(quick_sort(arr1), quick_sort(arr2))




if __name__ == "__main__":
    array1 = [7,3,4,7,10,12,2,5]
    array2 = [10, 6, 5, 11, 4, 20, 30, 25]
    array3 = [1,2,4,6,8,20,9,21,100]
    print(quick_sort(arr=array1))
    print(quick_sort(array2))
    print(quick_sort(array3))