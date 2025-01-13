class hashTables{
    constructor(size){
        this.size = new Array(size);
    }

    _hash(str){
        let hashedValue = 0
        if (str && str.length){
            for (let i = 0; i < str.length; i++){
                hashedValue = (hashedValue + str.charCodeAt(i) * i) % this.size.length
                }
        }
        return hashedValue;        
    }

    get(key){
        const location =  this._hash(key);
        if (this.size[location]){
            return this.size[location][1];
        }
        return undefined;
    }

    set(key, value){
        const location = this._hash(key);
        if (!this.size[location]) {
            this.size[location] = [key, value]
        }
        
        return this.size[location];
    }

    get keys(){
        let keys = [];
        for (let i = 0; i < this.size.length; i++){
            if (this.size[i]){
                keys.push(this.size[i][0])
            }
        }
        return keys;
    }
}

var ht = new hashTables(100);
console.log(ht.set("Nakul", "hello"));
console.log(ht.set("Hombre", "weon"));
console.log(ht.get("Nakul"));
console.log(ht.keys);

