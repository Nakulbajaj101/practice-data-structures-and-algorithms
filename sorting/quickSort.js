function quickSort(arr){
    if (!arr){
        return undefined;
    }
    const length = arr.length;
    if (length <= 2){
        if (length === 2){
            if (arr[0] > arr[1]){
                return [arr[1], arr[0]]
            }
            else {
                return arr;
            }
        }
        return arr;
    }
    else {
        const result = leftRightArrays(arr, length);
        return merge(quickSort(result[0]), quickSort(result[1]));
    }
   
}

function leftRightArrays(arr, length){
    const pivot_idx = Math.floor(length/2);
    const pivot = arr[pivot_idx];
    let leftArr = [];
    let rightArr = [];
    for (let i = 0; i < length; i++){
        if (arr[i] <= pivot){
            leftArr.push(arr[i]);
        }
        else {
            rightArr.push(arr[i]);
        }
    }
    if (leftArr.length < 1 || rightArr.length < 1){
        leftArr = arr.slice(0, pivot_idx);
        rightArr = arr.slice(pivot_idx, length);
    }
    return [leftArr, rightArr]
}

function merge(arr1, arr2){
    let leftIdx = 0;
    let rightIdx = 0;
    let result = [];
    while (leftIdx < arr1.length && rightIdx < arr2.length){
        if (arr1[leftIdx] < arr2[rightIdx]){
            result.push(arr1[leftIdx]);
            leftIdx ++;
        }
        else {
            result.push(arr2[rightIdx]);
            rightIdx ++;
        }
    }
    if (leftIdx < arr1.length){
        result = result.concat(arr1.slice(leftIdx, arr1.length))
    }
    else if (rightIdx < arr2.length){
        result = result.concat(arr2.slice(rightIdx, arr2.length))
    }
    else{
        return result;
    }
    return result;
}

let array1 = [7,3,4,7,10,12,2,5]
let array2 = [10, 6, 5, 11, 4, 20, 30, 25]
let array3 = [1,2,4,6,8,20,9,21,100]
console.log(quickSort(array1));
console.log(quickSort(array2));
console.log(quickSort(array3));