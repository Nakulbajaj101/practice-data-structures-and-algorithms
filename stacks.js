class Node {
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor(){
        this.top = null;
        this.length = 0;
        this.botton = null;
    }

    peek(){
        if (this.top){
            return this.top.value;
        }
    }

    push(value){
        const node = new Node(value);
        if (this.length === 0){
            this.top = node;
            this.bottom = node;
            this.length ++;
        }
        else
        {
            const holdingPointer = this.top;
            this.top = node;
            this.top.next = holdingPointer;
            this.length ++; 
        }
        return this.top;
    }

    pop(){
        if (!this.top){
            return null;
        }
        else 
        { 
            if (this.length > 0){
            const holdingPointer = this.top;
            this.top = this.top.next;
            }

            if  (this.top === this.bottom){
                this.bottom = null;
            }
            this.length --; 
            return this.top;
        }
    }
}

let stack = new Stack();
stack.push(2);
stack.push(3);
stack.pop();
stack.pop();
console.log(stack.top, stack.bottom);
console.log(stack.length)