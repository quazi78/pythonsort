class Sortstuff(object):

  def sortlist(self, x):
#lets get the length of the list
    len = x.__len__()

#a one item list or a 0 item list should match no matter what so just return it
    if len <= 1:
      return x

#iterate over the list and move items if they are out of place
    swapped = True

    while swapped == True:
      swapped = False
      for i in range(len - 1):
        if x[i] > x[i+1]:
          temp = x[i]
          x[i] = x[i+1]
          x[i+1] = temp
          swapped = True

    return x

