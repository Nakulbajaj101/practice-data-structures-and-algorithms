
function findFactorialRecursion(value){
    if (value <= 2){
        if (value !== 0){
            return value;
        }
        else {
            return 1;
        }
    }
    return findFactorialRecursion(value-1) * value;
}

function findFactorialIteration(value){
    if (value <= 2){
        if (value !== 0){
            return value;
        }
        else {
            return 1;
        }
    }
    let result = 1;
    for (let i = value; i >= 2; i--){
        result = result * i;
    }
    return result;
}

let tests = [5,4,3,2,1,0]

for (let i = 0; i < tests.length; i++ ){
    console.log(tests[i]);
    console.log(findFactorialIteration(tests[i]));
    console.log(findFactorialRecursion(tests[i]));
    console.log(`Next one is ${tests[i+1]}\n`);
}


