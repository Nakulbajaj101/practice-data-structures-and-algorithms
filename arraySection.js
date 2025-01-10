function reverse(str) {
  if (!str || typeof str !== "string" || str.length < 2) {
    console.log(`Please provide a valid string as ${str} is not valid`);
    return null;
  } else {
    const strSplit = str.split("");
    var reverseStr = "";
    for (let i = 0; i < strSplit.length; i++) {
      reverseStr = reverseStr + strSplit[strSplit.length - 1 - i];
    }
    return reverseStr;
  }
}

console.log("My name is Nakul");
console.log(reverse("My name is Nakul"));
console.log(reverse(1));
console.log(reverse("N"));

function reverse2(str) {
  if (!str || typeof str !== "string" || str.length < 2) {
    console.log(`Please provide a valid string as ${str} is not valid`);
    return null;
  } else {
    const stringLength = str.length;
    let totalItems = [];
    for (i = stringLength; i >= 0; i--) {
      totalItems.push(str[i - 1]);
    }
    return totalItems.join("");
  }
}

function reverse3(str) {
  return str.split("").reverse().join("");
}

const reverse4 = (str) => str.split("").reverse().join("");
const reverse5 = (str) => [...str].reverse().join("");

console.log(reverse2("My name is Nakul"));
console.log(reverse3("My name is Nakul"));
console.log(reverse4("My name is Nakul"));
console.log(reverse5("My name is Nakul"));
console.log(reverse2(1));
console.log(reverse2(""));

function mergeSortedArrays(arr1, arr2) {
  if (typeof arr1 !== "object" && typeof arr2 !== "object") {
    console.log("Error");
    return null;
  } else {
    if (!arr1 && arr2) {
      return arr2.sort();
    } else if (arr1 && !arr2) {
      return arr1.sort();
    } else {
      const sortedArray = [];
      arr1.sort();
      arr2.sort();
      let item1 = arr1[0];
      let item2 = arr2[0];
      let i = 1;
      let j = 1;
      while (item1 || item2) {
        console.log(item1, item2, i, j);
        if (!item2 || item1 <= item2) {
          sortedArray.push(item1);
          item1 = arr1[i];
          i++;
        } else {
          sortedArray.push(item2);
          item2 = arr2[j];
          j++;
        }
      }
      return sortedArray;
    }
  }
}

function mergeSortedArrays2(arr1, arr2) {
  return arr1.concat(arr2);
}

console.log(mergeSortedArrays([1, 8, 0], [2, 7, 6]));
console.log(mergeSortedArrays2([1, 2], ["nakul", "is"]));
