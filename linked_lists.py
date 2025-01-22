class Node:
    def __init__(self, value):
        self.value = value
        self.next = self.create_node()
    
    def create_node(self):
        node = {
            "value": self.value,
            "next": None,
        }

        return node


class LinkedLists:
    def __init__(self, value):
        self.value = value
        self.head = {"value": self.value, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = Node(value)
        end_node = node.next

        self.tail["next"] = end_node
        self.tail = end_node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        new_node = node.next
        new_node["next"] = self.head
        self.head = new_node
        self.length +=1

    def print_list(self):
        current_node = self.head
        linked_list = []
        while current_node["next"] != None:
            linked_list.append(current_node["value"])
            current_node = current_node["next"]
        linked_list.append(current_node["value"])
        return linked_list
    
    def traverse(self, index):
        current_node = self.head
        counter = 0
        while (counter != index):
            current_node = current_node["next"]
            counter +=1
        return current_node
    
    def remove(self, index):
        lead_node = self.traverse(index-1)
        pointer_node = lead_node["next"]
        new_node = pointer_node["next"]
        lead_node["next"] = new_node
        self.length -= 1
        return self.head

    
    def insert(self, value, index):
        if index >= self.length:
            self.append(value)
        elif index < 1:
            self.prepend(value)
        else:
            node = Node(value)
            new_node = node.next
            lead_node = self.traverse(index-1)
            pre_node = lead_node["next"]
            new_node["next"] = pre_node
            lead_node["next"] = new_node
            self.length += 1
            return self.head
        
    def reverse(self):
        if not self.head["next"]:
            return self.head
        else:
            first = self.head
            self.tail = self.head
            second =  first["next"]

            while second is not None:
                temp  = second["next"]
                second["next"] = first
                first = second
                second = temp

            self.head["next"] = None
            self.head = first
            return self.head

ll = LinkedLists(1)
ll.append(2)
ll.append(3)
# ll.prepend(0)
# print(ll.head)
# print(ll.print_list())
# print(ll.insert(1, 2))
# print(ll.insert(5, 3))
# print(ll.remove(1))
print(ll.reverse())
print(ll.print_list())
print(ll.tail)