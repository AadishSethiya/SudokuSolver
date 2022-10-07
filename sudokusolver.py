from random import randint, sample
import numpy as np

def findNextLoc(sudoku):
    #finds the location of next index in 9x9 sudoku matrix with 0 as element
    for col in range(9):
        for row in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return None, None       #returns none if no such index is found

def isCorrect(sudoku, row, col, val):
    #Checks if the value val is a valid entry at the location (row,col)
    for i in range(9):      #it is not valid if there is a same value in the given row
        if sudoku[row][i] == val:
            return False

    for i in range(9):      #it is not valid if there is a same value in the given column
        if sudoku[i][col] == val:
            return False

    row_sec = (row//3)      #represents the section of row to which the given row falls in
    col_sec = (col//3)      #represents the section of column to which the given column falls in
    for i in range(row_sec*3, row_sec*3 + 3):       #is not a valid entry if the section of box with that index has an other index with same value
        for j in range(col_sec*3, col_sec*3 + 3):
            if sudoku[i][j] == val:
                return False

    return True

def Sudoku(sudoku):
    #solves the sudoku puzzle
    row , col = findNextLoc(sudoku)

    num_list = range(1,10)

    if row == None and col == None:
        return True

    num_list = sample(num_list,len(num_list))       #shuffling all the entries in the num_list

    for val in num_list:
        if isCorrect(sudoku, row, col, val):        #if the entry is valid, input the entry
            sudoku[row][col] = val

            if Sudoku(sudoku):      #recursively check for the further entries and return true if the sudoku is solved
                return True
            
        sudoku[row][col] = 0        #if the sudoku is not solved replace the entry with other entries in num_list

    return False    

def num_soln(sudoku):
    #checks if the number of solutions of a given sudoku puzzle exceeds 1
    row , col = findNextLoc(sudoku)

    num_list = range(1,10)

    count = 0
    
    if row == None and col == None:
        return 0 

    num_list = sample(num_list,len(num_list))


    for val in num_list:
        if isCorrect(sudoku, row, col, val):
            sudoku[row][col] = val

            s_copy = np.copy(sudoku)

            if Sudoku(s_copy):      #if sudoku is solved, increase the number of solutions by 1
                count += 1
                if count>1:     #return if the number of solutions exceed 1
                    return count
            
        sudoku[row][col] = 0

    return count

def generator():
    #function to generate sudoku puzzle using an already valid sudoku puzzle
    sudoku = np.zeros((9,9))     
    Sudoku(sudoku)      #creating a valid sudoku puzzle
    list_non_zeros = [(i,j) for i in range(9) for j in range(9)]        #contains all the indices which have non zero entries
    iterate = 3     #variable used to break the while loop to reduce the time complexity of the function
    while iterate>0 and len(list_non_zeros) >= 17:      #a given sudoku puzzle needs to have a minimum of 17 entries to have a unique solution
        row,col = list_non_zeros.pop(randint(0,len(list_non_zeros) - 1))    #randomly taking an index out of list_non_zeros
        num = sudoku[row][col]
        sudoku[row][col] = 0        
        s_copy = np.copy(sudoku)
        count = num_soln(s_copy)       
        if(count > 1):          #if the number of solutions of the sudoku matrix is more than 1 after removing an entry, we put that entry back in the index and check for other entries in the puzzle
            sudoku[row][col] = num
            iterate -= 1
    return sudoku