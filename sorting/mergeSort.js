function mergeSort(arr){
    const length = arr.length;
    if (length <= 2){
        if (length === 1){
            return arr;
        }
        else {
            if (arr[0] > arr[1]){
                return [arr[1], arr[0]]
            }
            else{
                return arr
            }
        }
    }
    else {
        const middleIndex = Math.floor(length/2);
        const arr1 = arr.slice(0,middleIndex);
        const arr2 = arr.slice(middleIndex,length);
        return merge(mergeSort(arr1), mergeSort(arr2));
    }
}

function merge(arr1, arr2){
    let leftIndex = 0;
    let rightIndex = 0;
    let result = [];
    while (leftIndex < arr1.length && rightIndex < arr2.length){
        if (arr1[leftIndex] < arr2[rightIndex]){
            result.push(arr1[leftIndex]);
            leftIndex ++;
        }
        else{
            result.push(arr2[rightIndex]);
            rightIndex ++;
        }
    }
    if (leftIndex < arr1.length){
        result = result.concat(arr1.slice(leftIndex, arr1.length));
        result.concat(arr1.slice(leftIndex, arr1.length));
    }
    else if (rightIndex < arr2.length){
        result = result.concat(arr2.slice(rightIndex, arr2.length));
    }
    else{
        return result;
    }
    return result;
}

let arr = [10, 6, 5, 11, 4, 20, 30, 25]
console.log(mergeSort(arr));
