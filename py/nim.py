# nim.py
# Taylor Grant-Knight
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

import random

# print_bag
def print_bag(stones):
  if (stones == 1):
    print("There is 1 stone in the bag")
  else:
    print("There are " + str(stones) + " stones in the bag")

  
# num_stones_phrase
def num_stones_phrase(stones):
  return "1 stone" if stones == 1 else (str(stones) + " stones")

  
# computer_turn
def computer_turn(stones):
  print("Computer turn")
  stones_taken = 0

  if (stones <= 3):
    stones_taken = stones
  else:
    stones_taken = random.randint(1,3)

  print("The computer took " \
        + num_stones_phrase(stones) \
        + " from the bag.")

  return stones - stones_taken


# player_turn
def player_turn(stones):
  
  stones_taken = 0

  print("Player turn")

  while (stones_taken > 3 or stones_taken < 1 or (stones - stones_taken < 0)):
    stones_taken = int(input("How many stones would you like to remove? (1-3)"))
    if (stones_taken > 3 or stones_taken < 1):
      print("You can only remove 1-3 stones during your turn.")
    if (stones - stones_taken < 0):
      print("There aren't enough stones left! Try again.")

  return stones - stones_taken


# main
print("Welcome to the game of Nim!")
stones = 12
turn = 1

print_bag(stones)

while(stones > 0):
  print("Turn " + str(turn))

  stones = player_turn(stones)
  print_bag(stones)

  if (stones == 0):
    print("Player wins!")
    break

  stones = computer_turn(stones)
  print_bag(stones)

  if (stones == 0):
    print("Computer wins!")

  turn = turn + 1
  print()
  