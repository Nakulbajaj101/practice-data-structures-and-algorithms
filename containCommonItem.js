// When two arrays contain common elements
// should return true
// else return false

function containsCommonItem(arr1, arr2) {
  const obj = {};
  arr1.forEach((element1) => {
    if (!obj[element1]) {
      obj[element1] = true;
    }
  });
  console.log(obj);
  if (arr2 && arr2.constructor === Array) {
    arr2.forEach((element2) => {
      if (obj[element2]) {
        console.log(element2);
        return true;
      }
    });
  }
  return false;
}

function containsCommonItem2(arr1, arr2) {
  return arr1.some((item) => arr2.includes(item));
}

containsCommonItem(["xy", "yz", 1, 3, "hz"], [0, 2, 2]);
const myNewItem = containsCommonItem2(["xy", "yz", 1, 3, "hz"], [0, 2, 3]);
console.log(myNewItem);
