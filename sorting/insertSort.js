const arr = [6,1,3,5,4,10,-1,150, 11, -2, 150]

function insertSort(arr){
    const length = arr.length;

    for (let i = 0; i < length; i++){
        if (arr[i] < arr[0]){
            let small = arr[i];
            arr[i] = arr[0];
            arr[0] = small;
        }
        else {
            for (let j = i+1; j < length; j++){
                if (arr[j] < arr[i]){
                    let small = arr[j];
                    arr[j] = arr[i];
                    arr[i] = small;
                }
            }
        }
    }
    return arr;
}

console.log(insertSort(arr));