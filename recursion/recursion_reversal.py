def reverse(val: str):
    if len(val) <= 1:
        if len(val) == 1:
            return val
        else:
            return None
    return val[-1] + reverse(val[:-1])


print(reverse("Nakul"))