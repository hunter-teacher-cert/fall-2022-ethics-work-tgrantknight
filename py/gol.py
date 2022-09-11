# gol.py
# Taylor Grant-Knight
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

import random

# create_board
def create_board(rows, cols):
  return [['-']*cols for _ in range(rows)]


# print_board
def print_board(board):
  rows = len(board)
  cols = len(board[0])

  for row in range(0,rows):
    for col in range(0,cols):
      print(board[row][col] + " ", end = ' ')
    print()


# count_neighbors
def count_neighbors(board, row, col):
  rows = len(board)
  cols = len(board[0])
  neighbor_count = 0

  for i in range(0, rows):
    for j in range(0, cols):
      if( \
        not(i == row and j == col) \
        and (i <= row+1 and i >= row-1) \
        and (j <= col+1 and j >= col-1) ):
          if(board[i][j] == "X"):
            neighbor_count = neighbor_count + 1
  
  return neighbor_count


# get_next_gen_cell
def get_next_gen_cell(board, row, col):

  cell = board[row][col]
  neighbors = count_neighbors(board, row, col)
  newCell = "-"

  if(cell == "X"):
    if(neighbors == 2 or neighbors == 3):
      newCell = "X"
    else:
      newCell = "-"

  else:
    if(neighbors == 3):
      newCell = "X"
    else:
      newCell = "-"

  return newCell


# generate_next_board
def generate_next_board(board):

  rows = len(board)
  cols = len(board[0])

  nextBoard = create_board(rows, cols)

  for row in range(0,rows):
    for col in range(0,rows):
      cell = get_next_gen_cell(board,row,col)
      nextBoard[row][col] = cell

  return nextBoard

# main
board = \
  [ \
    ['-','-','X','-','X'], \
    ['-','X','X','-','-'], \
    ['-','-','X','X','X'], \
    ['-','-','-','-','X'], \
    ['X','-','-','-','X'], \
  ]
print_board(board)
for i in range(10):
  print()
  board = generate_next_board(board)
  print_board(board)
