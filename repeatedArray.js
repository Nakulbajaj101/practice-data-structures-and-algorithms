const recurringValueArray = (arr) => {
    let obj = {};
    if (arr && arr.length > 1){
        obj[arr[0]] = true;
        for (let i = 1; i < arr.length; i++){
            if (obj[arr[i]]){
                return arr[i];
            }
            else {
                obj[arr[i]] = true;
            }
        }
    }
    return undefined;
}

console.log(recurringValueArray([1]));
console.log(recurringValueArray([1,2,3,4,5]));
console.log(recurringValueArray([1,5, 4, 1]));
console.log(recurringValueArray([1, 2, 5,5 ,4,2]));
