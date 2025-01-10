import time
from typing import List

nemo = ['nemo', 'ksmk', 'jsjjsk', 'nem']*21000


def find_memo(arr: List) -> None:
  t0 = time.time()
  for i in range(len(arr)):
    if arr[i] == 'nemo':
      print('Found Nemo!')
  t1 = time.time()
  print(f'Call to find Nemo took {round((t1-t0)/1000, 4)} seconds')


find_memo(nemo)
