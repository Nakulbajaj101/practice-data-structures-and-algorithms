const selectionSort = (arr => {
    const length = arr.length;
    for (let i = 0; i < length; i++){
        let minimum = i;
        for (let j = i; j < length; j++){
            if (arr[i] > arr[j]){
                minimum = j;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    return arr;
})

const arr = [1,5,2,13,4,18,3,0,100];
console.log(selectionSort(arr));