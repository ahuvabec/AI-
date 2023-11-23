#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys
import heapq
import copy

ROW = "ABCDEFGHI"
COL = "123456789"
ROW1 = "ABC"
ROW2 ="DEF"
ROW3 ="GHI"
COL1 = "123"
COL2 = "456"
COL3 = "789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


#def Order_Domain_values(var,assisnment,csp): #LCV


#def INFERENCE(csp, var, value) # INFERENCE is where FC is implemented

def csp(board,index,x):
    row = index[0]
    col = index[1]
    value = True
    #check the col
    for r in ROW:
        #print("checking col")
        if board[r + col] == x:
            return False
   #check the row
    for c in COL:
        #print("checking row")
        if board[row + c] == x:
            print("here2")
            return False
    
    #check 3x3
    if (row == 'A') or (row == 'B') or ( row == 'C'):
        #print("cheking s1")
        if int(col) <= 3:
            for r in ROW1:
                for c in COL1:
                    if board[r + c] == x:
                        #print("here4")
                        return False
        elif int(col) <= 6:
            for r in ROW1:
                for c in COL2:
                    if board[r + c] == x:
                        #print("here5")
                        return False
        else:
            for r in ROW1:
                for c in COL3:
                    if board[r + c] == x:
                        return False
    elif (row == 'D') or (row == 'E') or ( row == 'F'):
        if int(col) <= 3:
           for r in ROW2:
                for c in COL1:
                    if board[r + c] == x:
                        return False
        elif int(col) <= 6:
            for r in ROW2:
                for c in COL2:
                    if board[r + c] == x:
                        #print("here9")
                        return False
        else:
            for r in ROW2:
                for c in COL3:
                    if board[r + c] == x:
                        #print("here10")
                        return False     
    else:
        #print("checking s3")
        if int(col) <= 3:
            for r in ROW3:
                for c in COL1:
                    if board[r + c] == x:
                        #print("here11")
                        return False
        elif int(col) <= 6:
            for r in ROW3:
                for c in COL2:
                    if board[r + c] == x:
                        #print("here12")
                        return False
        else:
            for r in ROW3:
                for c in COL3:
                    if board[r + c] == x:
                        #print("here13")
                        return False 
    return True

def check_all_pos(board):
    for r in ROW:
        for c in COL:
            if csp(board,r,c) == False:
                value = False
    return value

def genarate_domain(board):#returns domain
      #generates domain
    domain = dict()
    for r in ROW:
        for c in COL:
            domain[r+c] = {1,2,3,4,5,6,7,8,9}

    return domain


def update(board, domain):  #returns updated domain
    #itarate through the cols and remove values from domain
    new_domain = copy.deepcopy(domain)
    
    for c in COL:
        for r in ROW:
             if board[r+c] > 0:
                for j in ROW:
                    # check if value of board[r+c] is s till in domain[j+c] then remove it
                    if board[r+c] in new_domain[j+c]:
                        new_domain[j+c].remove(int(board[r+c]))

                    
    #iterate through rows
    for r in ROW:
        for c in COL:
            if board[r+c]>0:
                for k in COL:
                    if board[r+c] in new_domain[r+k]:
                        new_domain[r+k].remove(int(board[r+c]))

   
    #iterate through 3x3
    for r in ROW1:
        for c in COL1:
            if board[r+c]>0:
                for k in ROW1:
                    for j in COL1:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))


    for r in ROW1:
        for c in COL2:
            if board[r+c]>0:
                for k in ROW1:
                    for j in COL2:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))


    for r in ROW1:
        for c in COL3:
            if board[r+c]>0:
                for k in ROW1:
                    for j in COL3:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))

    
    for r in ROW2:
        for c in COL1:
            if board[r+c]>0:
                for k in ROW2:
                    for j in COL1:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))


    for r in ROW2:
        for c in COL2:
            if board[r+c]>0:
                for k in ROW2:
                    for j in COL2:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))
    

    for r in ROW2:
        for c in COL3:
            if board[r+c]>0:
                for k in ROW2:
                    for j in COL3:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))


    for r in ROW3:
        for c in COL1:
            if board[r+c]>0:
                for k in ROW3:
                    for j in COL1:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))

    
    for r in ROW3:
        for c in COL2:
            if board[r+c]>0:
                for k in ROW3:
                    for j in COL2:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))

    
    for r in ROW3:
        for c in COL3:
            if board[r+c]>0:
                for k in ROW3:
                    for j in COL3:
                        if board[r+c] in new_domain[k+j]:
                            new_domain[k+j].remove(int(board[r+c]))
  

    return new_domain
  
    
def is_solved(board):
    for r in ROW: 
        for c in COL:
            if (board[r+c] == 0):
                return False
             #and check each index is possible 
            if (csp(r,c,board[r+c])):
                return True
 
    return True   

def backtracking(board):
    return (backtrack(board))

def backtrack(board):

    #generate a domain
    domain = genarate_domain(board)
    
    #update domain 
    domain = update(board,domain)
    #print("domain updated")
    
    empty_spots = []

    for keys in board.keys():
        if board.get(keys) == 0:
            if len(domain[keys])==0:
                return None

            heapq.heappush(empty_spots,(len(domain[keys]),keys))
   
    if len(empty_spots) == 0:
       return board
        
    indx = heapq.heappop(empty_spots)[1]
    
    for val in domain[indx]:
        

        if csp(board,indx,val)== True:
            board[indx] = val
            #print("assignment is conssisten")
            result = backtrack(board)
            if result != None:
                return result
            board[indx] = 0
            #if assignment fails we reset
 
    return None
 
   
                           
if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)
        print_board(solved_board)
        
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')
        
     
    else:
        # Running sudoku solver for boards in sudokus_start.txt $python3 sudoku.py

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}

            # Print starting board. TODO: Comment this out when timing runs.
            print_board(board)

            # Solve with backtracking
            solved_board = backtracking(board)

            # Print solved board. TODO: Comment this out when timing runs.
            print_board(solved_board)

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

        print("Finishing all boards in file.")