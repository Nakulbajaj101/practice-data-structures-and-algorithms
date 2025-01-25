class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Queque {
    constructor(){
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    peek(){
        return this.first;
    }

    enqueue(value){
        if (! this.first){
            const newNode = new Node(value);
            this.first = newNode;
            this.last = newNode;
            this.length ++;
            return this.last;
        }
        else {
            const newNode = new Node(value);
            this.last.next = newNode;
            this.last = newNode;
            this.length ++;
            return this.last;
        }
    }

    dequeue(){
        if (! this.first){
            return null
        }
        else if (this.first === this.last) {
            this.last = null;
            this.first = null;
            this.length --;
            return this;
        }
        else {
            const headPointer = this.first.next;
            this.first = headPointer;
            this.last = null;
            this.length --;
            return this;
        }
    }
}

let q = new Queque();
console.log(q.peek());
console.log(q.enqueue(2));
// console.log(q.first, q.last);
console.log(q.enqueue(3));
console.log(q.first, q.last);
console.log(q.dequeue());
console.log(q.first, q.last);
console.log(q.dequeue());
console.log(q.first, q.last);


