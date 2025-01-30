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
            current_node = self.root
            while (current_node is not None):
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



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(6)
    bst.insert(20)
    bst.insert(170)
    bst.insert(15)
    bst.insert(1)
    print(json.dumps(bst.root, indent=4))
    print(json.dumps(bst.lookup(1), indent=4))
    print(json.dumps(bst.lookup(9), indent=4))
   
                
