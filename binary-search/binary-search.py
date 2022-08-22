mylist = [0, 5, 9, 15, 29, 50]
value  = 5

class binary:
  def search(self, mylist: list, value: int):
    lower, upper = 0, (len(mylist)-1)

    while lower <= upper:
      mid = (lower + upper) // 2
      if mylist[mid] == value:
        globals()['pos'] = mid
        return mid
      else:
        if mylist[mid] <= value:
          lower = mid + 1
        else: 
          upper = mid - 1

    return False

v = binary().search(mylist,value)
if v == False:
  print("Position of " + str(value) + " is not found in list")
else:
  print("Position of " + str(value) + " is " + str(v))