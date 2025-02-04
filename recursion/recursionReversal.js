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
