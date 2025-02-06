const bubbleSort = (arr => {
    const length = arr.length;
    for (let i = 0; i < length; i++){
        for (let j = i; j < length; j++){
            if (arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr
})
const arr = [1,5,2,13,4];
console.log(bubbleSort(arr));