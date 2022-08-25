# any imports
from array import *

class sub:
  def common_substring(self,list_a: list, list_b: list):
    a,b,longest_substring = list_a.upper(),list_b.upper(),0

    if len(a) == 0 or len(b) == 0:
      return longest_substring

    # 2d array 
    arr = [[0 for x in range(len(a))] for y in range(len(b))] 
    for i in range(len(a)):
      for x in range(len(b)):
        if a[i] == b[x]:
          if i == 0 or x == 0:
            arr[i].pop(x)
            arr[i].insert(x,1)
          else:
            arr[i][x] = arr[i - 1][x - 1] + 1

          if arr[i][x] > longest_substring:
            longest_substring = arr[i][x]
    return longest_substring
  def longest_substring(self,list_a: list):
    pass
    

# a = "ABABACCLO"
# b = "BABABCCFJI"
# v = sub().common_substring(a,b)
# print(str(v))

