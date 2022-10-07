import numpy as np
from sudokusolver import *

def expandLine(line):
    return line[0]+line[5:9].join([line[1:5]*(2)]*3)+line[9:13]

if __name__ == "__main__":

    print("Welcome to Sudoku Solver")
    
    while True:
        num = 0
        num = int(input("0.If you want to add a sudoku problem, press 0 \n1.If you want a pre-generated a sudoku puzzle press 1 \n"))
        
        sudoku = np.zeros((9,9))

        line0  = expandLine("╔═══╤═══╦═══╗")
        line1  = expandLine("║ . │ . ║ . ║")
        line2  = expandLine("╟───┼───╫───╢")
        line3  = expandLine("╠═══╪═══╬═══╣")
        line4  = expandLine("╚═══╧═══╩═══╝")
        symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if num == 0:
            for i in range(9):
                for j in range(9):
                    sudoku[i][j] = int(input(f"Enter the value at ({i+1},{j+1}) location: "))
            print("Your entered puzzle is: \n")
            nums   = [ [""]+[symbol[int(n)] for n in row] for row in sudoku ]
            print(line0)
            for r in range(1,10):
                print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
                print([line2,line3,line4][(r%9==0)+(r%3==0)])
        elif num == 1:
            sudoku = generator()
            print("Generated puzzle is: \n")
            nums   = [ [""]+[symbol[int(n)] for n in row] for row in sudoku ]
            print(line0)
            for r in range(1,10):
                print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
                print([line2,line3,line4][(r%9==0)+(r%3==0)])
        else:
            print("Invalid Input")
            break

        num = 0
        t = -1
        num = int(input("0.If you want to add or generate other puzzle, press 0 \n1.If you want to see the solved sudoku, press 1 \n2.If you want to solve the puzzle, press 2 \n"))
        if num == 2:
            ins = []
            for i in range(9):
                for j in range(9):
                    if sudoku[i][j] == 0:
                        ins.append((i,j))

            s_copy = np.copy(sudoku)
            Sudoku(s_copy)
            m = 0
            while len(ins) >= 0:
                if len(ins) >0:
                    row, col = input('Specify the position you want to input number to("row col" format where row and col are between 1 to 9): ').split()
                    row = int(row) - 1
                    col = int(col) - 1
                    if sudoku[row][col] != 0:
                        print("Place already filled, Try again")
                        continue 
                    val = int(input("Specify the value you want to enter: "))
                    if s_copy[row][col] == val:
                        sudoku[row][col] = val
                        ins.remove((row,col))
                        print("Your solution: \n")
                        nums   = [ [""]+[symbol[int(n)] for n in row] for row in sudoku ]
                        print(line0)
                        for r in range(1,10):
                            print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
                            print([line2,line3,line4][(r%9==0)+(r%3==0)])
                    else:
                        print("Incorrect value, try again")
                        continue
                else:
                    print("Yay, you solved it!!")
                    break
                m = int(input("0.If you want to continue solving, press 0 \n1.If you want to generate a new puzzle or see solution, press 1 \n"))
                if m == 0:
                    continue
                elif m == 1:
                    t = int(input("0.If you want to add or generate other puzzle, press 0 \n1.If you want to see the solved sudoku, press 1 \n"))
                    break

        if num == 0 or t == 0:
            continue
        elif num == 1 or t == 1:
            Sudoku(sudoku)
            nums   = [ [""]+[symbol[int(n)] for n in row] for row in sudoku ]
            print(line0)
            for r in range(1,10):
                print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
                print([line2,line3,line4][(r%9==0)+(r%3==0)])
        else:
            print("Invalid Input")
            break

        num = 0
        num = int(input("0.If you want to add another puzzle, press 0 \n1.If you want to exit, press 1 \n"))
        if num == 0:
            continue
        else:
            break

    print("Thank you!")