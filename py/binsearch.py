# binsearch.py
# Taylor Grant-Knight
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

import math

# def binSearch
def bin_search(list, target):
  return bin_search_rec(list, target, 0, len(list)-1)

# def binSearchRec
def bin_search_rec(list, target, lo_pos, hi_pos):
  target_pos = -1
  mid_pos = math.floor((lo_pos + hi_pos)/2)

  if(lo_pos > hi_pos):
    return target_pos

  if(list[mid_pos] == target):
    target_pos = mid_pos
  elif(list[mid_pos] > target):
    target_pos = bin_search_rec(list, target, lo_pos, mid_pos-1)
  elif(list[mid_pos] < target):
    target_pos = bin_search_rec(list, target, mid_pos+1, hi_pos)
  else:
    print("error")

  return target_pos

# Main method content here:
test_list = [1,1,2,3,5,5,6,6,7,9]
print(bin_search(test_list, 7))