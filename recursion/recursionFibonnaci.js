function fibonacciByIteration(value){
    //0,1,1,2,3,5,8,13,21
    if (value < 2){
        return value;
    }
    let arr = [0,1];
    for (let i = 2; i < value+1; i++){
        arr.push(arr[i-1] + arr[i-2]);
    }
    return arr[value];
}



function fibonacciByRecursion(value){
    if (value < 2){
        return value;
    }
    return fibonacciByRecursion(value-1) + fibonacciByRecursion(value-2);
}

console.log(fibonacciByIteration(8));
console.log(fibonacciByRecursion(8));