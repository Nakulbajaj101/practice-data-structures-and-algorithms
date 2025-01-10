from typing import List


def reverse_str(str: str) -> str | None:
  """Function to reverse a string"""

  if not str or len(str) < 2:
    print("Not a valid string")
    return None
  else:
    list = [i for i in str]
    list.reverse()
    return "".join(list)


def reverse_str2(str: str) -> str | None:
  """Function to reverse a string"""

  if not str or len(str) < 2:
    print("Not a valid string")
    return None
  else:
    str_length = len(str)
    reverse_str = []
    for i in range(str_length - 1, -1, -1):
      reverse_str.append(str[i])

    return "".join(reverse_str)


def reverse_str3(string: str) -> str | None:
  """Function to reverse a string"""

  if not str or not isinstance(string, str) or len(string) < 2:
    print("Not a valid string")
    return None
  else:
    return string[::-1]


def merge_sorted_arrays(list_a: List = [], list_b: List = []) -> List | None:
  """Function that takes in two arrays and merges them"""

  if not list_a or not list_b:
    if not list_a and list_b:
      list_b.sort()
      return list_b
    elif not list_b and list_a:
      list_a.sort()
      return list_a
    else:
      return []
  else:
    list_a.extend(list_b)
    list_a.sort()
    return list_a


def check_index_exists(list, index):
  """Check if index exists"""

  try:
    list[index]
  except IndexError:
    return False
  return True


def merge_sorted_arrays2(list_a: List = [], list_b: List = []) -> List | None:
  """Function that takes in two arrays and merges them"""

  if not list_a or not list_b:
    if not list_a and list_b:
      list_b.sort()
      return list_b
    elif not list_b and list_a:
      list_a.sort()
      return list_a
    else:
      return []
  else:
    sorted_array = []
    list_a.sort()
    list_b.sort()
    i = 0
    j = 0
    while i < len(list_a) or j < len(list_b):
      if (check_index_exists(list_a, i)
          and not check_index_exists(list_b, j)) or (check_index_exists(
              list_a, i) and list_a[i] < list_b[j]):
        sorted_array.append(list_a[i])
        i += 1
      else:
        sorted_array.append(list_b[j])
        j += 1
    return sorted_array


if __name__ == "__main__":
  print(reverse_str("Nakul is cool"))
  print(reverse_str2("Nakul is cool"))
  print(reverse_str3("Nakul is cool"))
  print(reverse_str3(123))
  print(merge_sorted_arrays([1, 8, 0], [2, 7, 6]))
  print(merge_sorted_arrays2([1, 8, 0], [2, 7, 6]))
