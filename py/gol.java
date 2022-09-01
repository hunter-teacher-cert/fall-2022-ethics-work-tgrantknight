import java.io.*;
import java.util.*;

/**
 * Conway's Game of Life by Team AreWeSentientYet?
 * First Last
 * collaborators: First Last, First Last
 */

/**
   The Rules of Life:
   Survivals:
   * A living cell with 2 or 3 living neighbours will survive for the next generation.
   Deaths:
   * Each cell with >3 neighbours will die from overpopulation.
   * Every cell with <2 neighbours will die from isolation.
   Births:
   * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.
   NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.
*/

public class CgolPlus
{

  //create, initialize, and return  empty board (all cells dead)
  public static char[][] createNewBoard( int rows, int cols )
  {
    // Assume dead cells are " "
    // Taken directly from Array2DPractice.java 
    char[][] board = new char[rows][cols];
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        board[i][j]='-';
      }
    }
    return board;
  }


  //print the board to the terminal
  public static void printBoard( char[][] board )
  {
    // Directly from Array2DPractice.java
    
    // Need to colect the value for rows and cols
    int rows = board.length;
    int cols = board[0].length;

    // Should use the double traversal from buildBoard
    // Start with a loop through the columns, meaning cap at rows
    for (int i = 0; i < rows; i++){
      // Then loop through each row for the given column
      for (int j = 0; j < cols; j++){
        // Now print each value with a space after
        System.out.print(board[i][j] + " ");
      }
      // Add a new line after each row.
      System.out.println("");    
    }
  }


  //set cell (r,c) to val
  public static void setCell( char[][] board, int r, int c, char val )
  {
    board[r][c] = val;
  }


  //return number of living neigbours of board[r][c]
  public static int countNeighbours( char[][] board, int r, int c )
  {
    // Copied directly from Array2DPractice.java, with modifications
    
    // Start by getting the rows and cols ints
    int rows = board.length;
    int cols = board[0].length;

    // Need a variable to count neighbors
    int neighborCount = 0;

    // Set new start and end points for the for loop
    // to save comp time
    int rStart = Math.max(r-1,0);
    int rEnd = Math.min(r+1,rows);
    int cStart = Math.max(c-1,0);
    int cEnd = Math.max(c+1,cols);

    // Standard loop through each element:
    // Note: a lot of wasted checks
    for (int i = rStart; i < rEnd; i++){
      for (int j = cStart; j < cEnd; j++){
        // Using ifs, check if the cell is in the area
        // and not the square itself
        if (!(i == r && j == c)){
          // Change from 2DArrayPractice: Instead of setting to X, count Xs
          if(board[i][j] == 'X'){
            neighborCount++;
          }
        }
      }
    }
    
    return neighborCount;
  }


  /**
     precond: given a board and a cell
     postcond: return next generation cell state based on CGOL rules
     (alive 'X', dead '-') <-- Changed to '-'
  */
  public static char getNextGenCell( char[][] board,int r, int c )
  {
    // '-' for dead cell makes this more readible

    // Going light on comments here because replit just refreshed w/o saving
    char cell = board[r][c];
    int neighbours = countNeighbours(board,r,c);
    // Set default for newCell as a space to error check
    char newCell = ' ';

    // starts alive
    if (cell == 'X'){
      if (neighbours == 2 || neighbours == 3){
        newCell = 'X';
      } else {
        newCell = '-';
      }

    // otherwise starts dead
    } else {
      if (neighbours == 3) {
        newCell = 'X';
      } else {
        newCell = '-';
      }
    }

    return newCell;
  }


  //generate and return a new board representing next generation
  public static char[][] generateNextBoard( char[][] board )
  {
    // Start with explodeAllChars from yesterday
    // Start with vars for current board rows and cols;
    int rows = board.length;
    int cols = board[0].length;
    
    // Create the next board template;
    char[][] nextBoard = new char[rows][cols];

    // Standard loop through every element:
    for (int i = 0; i < rows; i++){
      for (int j = 0; j < cols; j++){
        // Populate the nextBoard using getNextGenCell for each cell
        setCell(nextBoard,i,j,getNextGenCell(board,i,j));
      }
    }

    return nextBoard;
  }


  // New method to randomize starting conditions
  // Parameters:
  // board is the board to populate
  // double lifeChance is 0.0 to 1.0 and is the chance for it to start with X
  public static void createStart(char[][] board, double lifeChance) {
    // Loop through each cell like usual
    int rows = board.length;
    int cols = board[0].length;

    // Standard loop through every element:
    for (int i = 0; i < rows; i++){
      for (int j = 0; j < cols; j++){
        // Use Math.random and lifeChance to determine which to set as
        if (lifeChance > Math.random()){
          setCell(board,i,j,'X');
        } else {
          setCell(board,i,j,'-');
        }
      }
    }    
  }

  
  // Took from the Animate.java file for animation
  public static void delay(int n){
    try {
      Thread.sleep(n);
    }
    catch(InterruptedException e) {}
  }


  // Make the Gosper glider gun for animation!
  // Requires 40 width
  // Parameters: Board filled with dead cells
  public static void gliderGun(char[][] board){
    // Not sure how to read files, so here is the raw file:
    String[] gliderRaw = new String[9];
    gliderRaw[0] = "........................O";
    gliderRaw[1] = "......................O.O";
    gliderRaw[2] = "............OO......OO............OO";
    gliderRaw[3] = "...........O...O....OO............OO";
    gliderRaw[4] = "OO........O.....O...OO";
    gliderRaw[5] = "OO........O...O.OO....O.O";
    gliderRaw[6] = "..........O.....O.......O";
    gliderRaw[7] = "...........O...O";
    gliderRaw[8] = "............OO";

    // Starting at the top left of the board 0,0
    // Loop through each row, if 0 set 'X'
    // Jagged array, so change cols each time
    // Note: each entry is a string, not an array, so length()
    int rows = gliderRaw.length;
    int cols = gliderRaw[0].length(); // Change in loop

    for (int i = 0; i < rows; i++){
      cols = gliderRaw[i].length();
      for (int j = 0; j < cols; j++){
        if (gliderRaw[i].charAt(j) == 'O'){
          board[i][j] = 'X';
        }
      }
    }
  }
  
  
  

  public static void main( String[] args )
  {
    
    char[][] board;
    board = createNewBoard(25,25);
    //breathe life into some cells:
    createStart(board,0.25);
    //Note: gilderGun requires 40x40 at least
    // gliderGun(board);
    
    System.out.print("\033[2J");
    for(int i = 0; i < 1000; i++){
      //clear screen, place cursor at origin (upper left)
      System.out.print("[0;0H\n");
      //System.out.print("\033[1;1H");
      
      System.out.printf("Gen %d:\n", i);
      printBoard(board);
      board = generateNextBoard(board);
      delay(100);
      //System.out.print("\033[2J");
    }
  }//end main()

}//end class