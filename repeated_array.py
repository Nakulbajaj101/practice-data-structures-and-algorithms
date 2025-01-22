from typing import List
arr = [1,2,1,2]

#(O(n)^2)
def repeated_array(arr: List[int]):

    if isinstance(arr, List) and arr and len(arr) > 1:
        repeated = []
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    repeated.append(j)
        if repeated:
            return arr[min(repeated)]
    return None

#(O(n))
def repeated_array2(arr: List):
    if isinstance(arr, List) and arr and len(arr) > 1:
        obj = {}
        obj[arr[0]] = True
        for i in range(1, len(arr)):
            try:
                if obj[arr[i]]:
                    return arr[i]
            except KeyError:
                obj[arr[i]] = True
    return None




if __name__ == "__main__":
    print(repeated_array(arr))
    print(repeated_array(arr = [1,2,3,4]))
    print(repeated_array(arr=[1,2,3,5,2]))

    print(repeated_array2(arr))
    print(repeated_array2(arr = [1,2,3,4]))
    print(repeated_array2(arr=[1,2,3,5,2]))
    print(repeated_array([1]))
    print(repeated_array([1, 'n', 2, 'n']))
    print(repeated_array([1, 'n', 2,2, 'n']))
    print(repeated_array([1, 'n', 5,5, 2,2, 1, 'n']))
    print(repeated_array([1, 'n', 'n', 5,5, 2,2, 1, 'n']))
    print(repeated_array2([1, 'n', 2,2, 'n']))

