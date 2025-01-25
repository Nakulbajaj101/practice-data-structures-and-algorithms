class Node:
    def __init__(self, value):
        self.node = {
            "value": value,
            "next": None
        }


class Queues:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            return None
        else:
            return self.first
        
    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node.node
            self.last = node.node
        else:
            self.last["next"] = node.node
            self.last = node.node
        self.length += 1
        return self.last
    
    def dequeue(self):
        if self.length == 0:
            return None
        if self.length > 1:
            head_pointer = self.first["next"]
            self.first = head_pointer
        else:
            self.first = None
            self.last = None
        self.length -= 1

        return self.first
    
if __name__ == "__main__":
    q = Queues()
    q.enqueue(2)
    q.enqueue(10)
    q.enqueue("google")
    print(q.peek())
    q.dequeue()
    q.dequeue()
    q.enqueue("facebook")

    print(q.first, q.last, q.length)
    q.dequeue()
    q.dequeue()
    print(q.first, q.last, q.length)

