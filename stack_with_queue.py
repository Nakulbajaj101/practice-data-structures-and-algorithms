class Node:
    def __init__(self, value):
        self.node = {
            "value": value,
            "next": None 
        }

    def get(self):
        return self.node

class MyStack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        node = Node(value=value).get()
        if self.empty():
            self.top = node
            self.bottom = node
        else:
            node["next"] = self.top
            self.top = node
        self.length += 1
        return self.top
    
    def peek(self):
        if self.empty():
            return None
        else:
            return self.top
        
    def pop(self):
        if self.empty():
            return None
        if self.length == 1:
            self.top = self.bottom = None
        else:
            next_node = self.top["next"]
            current_head = self.top
            for i in range(self.length - 1):
                if next_node["next"] is None:
                    self.bottom = current_head
                    self.bottom["next"] = None
                else:
                    current_head = current_head["next"]
                    next_node = next_node["next"]
        self.length -= 1
        return self

    def empty(self):
        return self.length == 0
    
if __name__ == "__main__":
    s = MyStack()
    s.push(2)
    s.push(10)
    s.push("google")

    print(s.top, s.bottom, s.length)

    print(s.peek())
    s.pop()
    s.pop()
    s.push("facebook")

    print(s.top, s.bottom, s.length)