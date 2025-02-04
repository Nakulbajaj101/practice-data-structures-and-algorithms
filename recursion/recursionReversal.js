function reverse(val){
    if (!val){
        return null
    }
    let arr = val.split("");
    if (arr.length == 1){
        return val
    }

    return arr[arr.length - 1] + reverse(val.substring(0, arr.length - 1));
}
const basket = [4,1,2]
basket.sort(function(a,b){
    console.log(a,b)
    console.log("Next")
;    return a-b
});

console.log(basket);

//3, -2, -2, 1

