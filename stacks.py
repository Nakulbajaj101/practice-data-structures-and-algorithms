class Node:
    def __init__(self, value):
        self.node = {
            "value": value,
            "next": None 
        }

    def get(self):
        return self.node

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if not self.top:
            return None
        else:
            return self.top["value"]


    def push(self, value):
        new_node = Node(value=value).get()
        if not self.top:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node["next"] = self.top
            self.top = new_node
        self.length += 1
        return self.top

    def pop(self):
        if self.length == 0:
            return None
        else:
            if self.length == 1:
                self.top = None
                self.bottom = None
            else:
                head_pointer = self.top["next"]
                self.top = head_pointer
            self.length -= 1
            return self.top

if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(10)
    s.push("google")

    print(s.peek())
    s.pop()
    s.pop()
    s.push("facebook")

    print(s.top, s.bottom, s.length)