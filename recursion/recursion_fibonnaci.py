def fib_rec(val: int):
    # 0, 1, 1, 2, 3, 5, 8, 13

    if val < 2:
        return val
    
    else:
        return fib_rec(val-1) + fib_rec(val-2)


def fib_iter(val: int):
    if val < 2:
        return val
    else:
        arr = [0,1]
        for i in range(2, val+1):
            if i <= val:
                arr.append(arr[i-1] + arr[i-2])
        return arr[val]

for i in range(1,8):
    print(f"iteration result of {i}")
    print(fib_iter(i))
    print(f"recursive result of {i}")
    print(fib_rec(i))
    print()
  

