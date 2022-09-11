# gol.py
# Taylor Grant-Knight
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

import random

# create_board
def create_board(rows, cols):
  return [['-']*cols]*rows


# create_start
def create_start(board, life_chance):
  rows = len(board)
  cols = len(board[0])

  for row in range(0,rows):
    for col in range(0,cols):
      num = random.random()
      if(life_chance > random.random()):
        board[row][col] = 'X'
        print(str(num) + ", " + str(row) + ", " + str(col))
      else:
        board[row][col] = '-'
        print(str(num) + ", " + str(row) + ", " + str(col))


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

  print(str(row) + " " + str(col))
  neighbor_count = 0

  row_start = max(row-1,0)
  row_end = min(row+1,rows)
  col_start = max(col-1,0)
  col_end = min(col+1,cols)
  print(str(row_start)+' '+str(row_end)+' '+str(col_start)+' '+str(col_end))

  for i in range(row_start, row_end):
    for j in range(col_start, col_end):
      if( \
        not(i == row and j == col) \
        and (i < rows) \
        and (j > cols) 
      ):
        print(str(i) + ', ' + str(j) + ', ' + board[i][j])
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

  print(str(row) + " " + str(col) + " " + str(neighbors))
  
  return newCell


# generate_next_board
def generate_next_board(board):

  rows = len(board)
  cols = len(board[0])

  nextBoard = create_board(rows, cols)

  for row in range(0,rows):
    for col in range(0,rows):
      nextBoard[row][col] = get_next_gen_cell(board,row,col)

  return nextBoard

# main
board = \
  [ \
    ['-','-','X','-','X'], \
    ['-','X','X','-','X'], \
    ['-','-','X','X','X'], \
    ['-','-','X','-','X'], \
    ['X','-','X','-','X'], \
  ]
print_board(board)
print_board(generate_next_board(board))
