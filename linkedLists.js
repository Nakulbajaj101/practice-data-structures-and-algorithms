// 10 -> 6 -> 2

class linkedLists {
    constructor(value){
        this.head = {value: value,
            next: null
        };
        this.tail = this.head;
        this.length = 1;
    }

    append(value){
        const newNode = {
            value: value,
            next: null
        }

        this.tail.next = newNode;
        this.tail = newNode;
        this.length ++;
    }

    prepend(value){
        //{v: 2, next: {} }
        const newNode = {
            value: value,
            next: null
        };
        newNode.next = this.head;
        this.head = newNode;
        this.length ++;
    }

    insert(index, value){
        if (index >= this.length){
            this.append(value);
        }
        else {
            const newNode = {
                value: value,
                next: null
            }

            const leadNode = this.traverse(index-1);
            const pointerNode = leadNode.next;
            newNode.next = pointerNode;
            leadNode.next = newNode;
            this.length ++;
            return this.head;
        }
    }

    delete(index){
        const leadNode = this.traverse(index-1);
        const pointerNode = leadNode.next.next;
        leadNode.next = pointerNode;
        this.length -- ;
        return this.head;
    }

    traverse(index){
        let currentNode = this.head;
        let i = 0;
        while (i < index){
            currentNode = currentNode.next;
            i ++;
        }

        return currentNode;
    }



    printList(){
        let linkList = [];
        let currentNode = this.head.next;
        linkList.push(this.head.value);
        while (currentNode.next != null){
            linkList.push(currentNode.value);
            currentNode = currentNode.next;
        }
        linkList.push(currentNode.value);
        return linkList;
    }

    reverse(){
        if (!this.head.next){
            return this.head
        }
        else {
            let first = this.head;
            this.tail = this.head;
            let second = first.next; //this.head.next
            while (second){
                let temp = second.next;
                second.next = first; //  {this.head}
                first = second;
                second = temp;
            }
            this.head.next = null;
            this.head = first;
            return this.head;
        }
    }
}

const ll = new linkedLists(10);
// console.log(ll);
ll.append(6);
ll.append(2);
ll.prepend(1);
console.log(ll.insert(2,2));
//console.log(ll.insert(2,3));
console.log(ll.printList());
console.log(ll.delete(2));
console.log(ll.printList());
// console.log(ll.head.next);
// console.log(ll.list);
// console.log(ll.insert(3, 10));
// console.log(ll.list);
console.log(ll.reverse())
console.log(ll.printList());