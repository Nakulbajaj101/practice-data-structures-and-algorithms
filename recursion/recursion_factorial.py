def recursion_factorial(val:int) -> int:
    """Recursive function to produce factorial"""

    if val <= 2:
        if val <= 1:
            return 1
        else:
            return val
    
    else:
        return recursion_factorial(val-1) * val
    

def iteration_factorial(val: int) -> int:
    """Iterative function"""

    if val <= 2:
        if val <= 1:
            return 1
        else:
            return val
    else:
        result = 1
        for i in range(2, val+1):
            result = result * i
        return result
    
for i in range(1,6):
    print(f"iteration result of {i}")
    print(iteration_factorial(i))
    print(f"recursive result of {i}")
    print(iteration_factorial(i))
    print()
  