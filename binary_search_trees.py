import json
class Node:
    def __init__(self, value):
        self.node = {
            "value": value,
            "left": None,
            "right": None
        }

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value=value).node
        if self.root is None:
            self.root = node
            return self.root
        else:
            current_node = self.root
            while current_node is not None:
                if value < current_node["value"]:
                    if current_node["left"] is None:
                        current_node["left"] = node
                        return current_node
                    else:
                        current_node = current_node["left"]
                elif value > current_node["value"]:
                    if current_node["right"] is None:
                        current_node["right"] = node
                        return current_node
                    else:
                        current_node = current_node["right"]

                else:
                    return None
                
    def lookup(self, value):
        if self.root is None:
            return None
        else:
            iteration = 1
            current_node = self.root
            while (current_node is not None):
                print(iteration)
                if value < current_node["value"]:
                    if current_node["left"] is not None:
                        if current_node["left"]["value"] == value:
                            return current_node["left"]
                        else:
                            current_node = current_node["left"]
                elif value > current_node["value"]:
                    if current_node["right"] is not None:
                        if current_node["right"]["value"] == value:
                            return current_node["right"]
                        else:
                            current_node = current_node["right"]
                else:
                    return current_node
                iteration += 1
    
    def remove(self, value):
        if self.root is None:
            return None
        else:
            current_node = self.root
            parent_node = None
            while True:
                if value == current_node["value"]:
                    if current_node["right"] is None:
                        if parent_node is None:
                            self.root = current_node["left"]
                        else:
                            if value < parent_node["value"]:
                                parent_node["left"] = current_node["left"]
                            else:
                                parent_node["right"] = current_node["left"]
                    elif current_node["left"] is None:
                        if parent_node is None:
                            self.root = current_node["right"]
                        else:
                            if value < parent_node["value"]:
                                parent_node["left"] = current_node["right"]
                            else:
                                parent_node["right"] = current_node["right"]

                    else:
                        next_node = current_node["left"]
                        next_node_parent = current_node
                        while next_node["right"]:
                            next_node_parent = next_node
                            next_node = next_node["right"]
                        current_node["value"] = next_node["value"]
                        next_node_parent["right"] = None
                    
                    return current_node
                
                elif value > current_node["value"]:
                    if current_node["right"]:
                        parent_node = current_node
                        current_node = current_node["right"]
                    else:
                        return None
                else:
                    if current_node["left"]:
                        parent_node = current_node
                        current_node = current_node["left"]
                    else:
                        return None


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(9)
    bst.insert(14)
    bst.insert(17)
    bst.insert(12)
    bst.insert(16)
    # bst.insert(1)
    print(json.dumps(bst.root, indent=4))
    # print(json.dumps(bst.lookup(10), indent=4))
    # print(json.dumps(bst.lookup(5), indent=4))
    bst.remove(10)
    print(json.dumps(bst.root, indent=4))

   
                
