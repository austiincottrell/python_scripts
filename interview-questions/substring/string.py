# any imports
from array import *

class sub:
  def common_substring(self, string_1: str, string_2: str) -> int:
    a,b,longest_substring = string_1.upper(),string_2.upper(),0

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
  def longest_substring(self, string_1: str) -> int:
    charSet,left,result = set(),0,0

    for right in range(len(string_1)):
      while string_1[right] in charSet:
        charSet.remove(string_1[left])
        left += 1
      charSet.add(string_1[right])
      result = max(result, right - left + 1)

    return result



a = "ABABACCLO"
b = "BABABCCFJI"
v = sub().common_substring(a,b)
print(str(v))
## should be 4

a = "abcdabccbbfjkilo"
v = sub().longest_substring(a)
print(str(v))
## should be 7