arr = [1,5,2,13,4, 18, 3, 0, 100]

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

if __name__ == "__main__":
    print(selection_sort(arr=arr))
