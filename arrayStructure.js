class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
  }

  pop() {
    delete this.data[this.length - 1];
    this.length--;
    return this.data[this.length - 1];
  }

  shift(index) {
    for (let i = index; i < this.length; i++) {
      this.data[i] = this.data[i + 1];
    }
    this.pop();
  }

  delete(index) {
    delete this.data[index];
    this.shift(index);
  }
}

var myArray = new MyArray();

console.log(myArray.length);
console.log(myArray.get(0));

myArray.push(2);
myArray.push(4);
console.log(myArray.length);
console.log(myArray.get(0));
console.log(myArray.data);

myArray.pop();
console.log(myArray.data);
myArray.push(10);
myArray.push(20);
myArray.push('nakul');
console.log(myArray.data);
console.log(myArray.length);

myArray.delete(1);
console.log(myArray.length);
console.log(myArray.data);

