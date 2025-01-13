import random
class HashTable:
    def __init__(self, size: int = 2000):
        self.obj = [[0]*2 for i in range(size)]
     
    def __hash(self, key: str=""):
        if key:
            address = 0
            for i in key:
                random.seed(42)
                address += (address + int((ord(i)/5)) +  random.randint(1, 3)) % len(self.obj)
            
            return address
    
    def set(self, key, value):
        location  = self.__hash(key)
        if self.obj[location] == [0,0]:
            self.obj[location] = [key, value]
        else:
            print("location already exists, and want to avoid collision")
        return self.obj[location]

    def get(self, key):
        location  = self.__hash(key)
        data = self.obj[location]
        if data != [0,0]:
            if isinstance(data[0], str):
                return data[1]
            else:
                index = 0
                for i in data:
                    if i[index][0] == key:
                        return i[index][1]
                    index += 1
        else:
            return None
        
    def keys(self):
        return [i[0] for i in self.obj if i != [0, 0]]

if __name__ == "__main__":
    ht = HashTable()
    ht.set("Nakul", "yo")
    ht.set("Evelyn", "why")
    ht.set("Amigo", "weon")
    ht.set("Amigo", "weon")
    print(ht.get("Amigo"))
    print(ht.get("Nipun"))
    print(ht.keys())
    
