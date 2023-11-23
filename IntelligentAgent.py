import random
from BaseAI import BaseAI
import time
import copy
import numpy as np


class IntelligentAgent(BaseAI):
    def getMove(self, grid):

        return self.decision((None,grid))[0]
    #following sudo code from class
    def maximize(self, grid, a, b, depth, time_x):
        timer = time.process_time() - time_x
        #we return if no more move or the time is up of certain depth is reached 
        if self.terminal_test(grid[1]) or timer >= .2 or depth >= 6:
            return (None, self.eval(grid[1]))

        (max_child, max_utility) = (None, float('-inf'))
        # get avilable moves Returns a list of available moves, along with moved grids which genrates the children
        for child in grid[1].getAvailableMoves():
            (_, utility) = self.minimize(child, a, b, depth + 1, time_x)

            if utility > max_utility:
                (max_child, max_utility) = (child, utility)

            if max_utility >= b:
                break

            if max_utility > a :
                a = max_utility

        return (max_child, max_utility)

    #imprevising the sudo code from class to incluse the probabilities (ie. Expectiminimax)
    def minimize( self, grid, a, b, depth, time_y):
        timer = time.process_time() - time_y
        if self.terminal_test(grid[1]) or timer >= .2:
            return (None, self.eval(grid[1]))
        
        (min_child, min_utility) = (None, float('inf'))
        
        # Returns a list of empty cells
        empty_cells = grid[1].getAvailableCells()
        
        for child in empty_cells:
            child_one = copy.deepcopy(grid)
            #insert number with probability
            child_one[1].map[child[0]][child[1]] = 2 if random.random() < .9 else 4

            
            (_,utility) = self.maximize(child_one, a, b,depth +1 , time_y)#probability

            if utility < min_utility:
                (min_child,min_utility) = (child_one, utility)

            if min_utility <= a:
                break
            if min_utility < b:
                b = min_utility

        return (min_child, min_utility)


    def decision(self,grid):
        (child, _) = self.maximize(grid,float('-inf') , float('inf'), 0, time.process_time())
        return child

     #if were able to make a move return true or false
    def terminal_test(self, grid):
        if grid.canMove():
            return False
        return True
    
    #def probability(grid):
        #return grid[1].map[child[0]][child[1]] = 2 if random.random() < .9 else 4
    #this has all the heuristics 
    
    def eval(self,grid):
        mon_score = self.monotonicity(grid)
        empty = self.empty_spaces(grid)
        smooth = self.smoothness(grid)
        weight = self.weight_probability(grid)
        #snakey = self.snake(grid)
   
        return  350*empty + mon_score + weight - smooth #snakey + weight

    #following the sudo code in the paper efaidnbmnnnibpcajpcglclefindmkaj/https://theresamigler.files.wordpress.com/2020/03/2048.pdf
    def monotonicity(self, grid):
        best = -1
        for i in range(3):
            current = 0
            for row in range(3):
                for col in range(2):
                    if grid.map[row][col] >= grid.map[row][col+1]:
                        current +=1
            for col in range(3):
                for row in range(2):
                    if grid.map[row][col] >= grid.map[row+1][col]:
                        current+=1
            if current > best:
                best = current 
            #rotate the board 90 deg
            #print("b4")
            #print(grid.map)
            m = np.array(grid.map)
            grid.map = np.rot90(m)
            #print("after")
            #print(grid.map)
        return best

    def empty_spaces(self, grid):
        empty_cells = grid.getAvailableCells()
        length = len(empty_cells)
        return length

    def smoothness(self, grid):
        distance = 0  
        for row in range(3):
                for col in range(3):
                    distance += abs(grid.map[row][col] - grid.map[row][col+1])
    
                    distance += abs(grid.map[row][col] - grid.map[row+1][col])
                       
                    distance += abs(grid.map[row][col] - grid.map[row -1][col])
                        
                    distance += abs(grid.map[row][col] - grid.map[row][col-1])
                        
        return distance
    
    def snake(self, grid):
        snake1 = self.sum_of_board( np.array(grid.map) * np.array([[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12], [16, 15, 14, 13]]))
        snake2 = self.sum_of_board(np.array(grid.map) * np.array([[4, 3, 2, 1], [5, 6, 7, 8], [12, 11, 10, 9], [13, 14, 15, 16]]))
        snake3 = self.sum_of_board(np.array(grid.map) * np.array([[16, 15, 14, 13], [9, 10, 11, 12], [8, 7, 6, 5], [1, 2, 3, 4]]))
        snake4 = self.sum_of_board(np.array(grid.map) * np.array([[13, 14, 15, 16], [12, 11, 10, 9], [5, 6, 7, 8], [4, 3, 2, 1]]))
       
        return max(snake1, snake2, snake3, snake4)
    
    def sum_of_board(self,grid):
        addy = 0 
        for i in range(4):
            for j in range(4):
                addy += grid[i][j]
        return addy

    def weight_probability(self, grid):
        '''WEIGHT_MATRIX = [
            [.135, .121, .102, .0999],
            [.0997, .088, .076, .0724],
            [.0606, .0562, .0371, .0161],
            [.0125, .0099, .0057, .0033]
            ]'''

        # weight matrix from the paper SOLUTION STRATEGIES FOR A GAME
        WEIGHT_MATRIX = [
          [ 135, 121, 102, 99],
          [72, 76, 88, 99],
          [60, 56 ,37, 16], 
          [12, 9, 5, 3]]

        '''WEIGHT_MATRIX = [
          [ 6, 5, 4, 3],
          [5, 4, 3, 2],
          [4, 3 ,27, 1], 
          [3, 2, 1, 0]]'''
        
        result = 0
        for i in range(4):
            for j in range(4):
                result += grid.map[i][j] * WEIGHT_MATRIX[i][j]

        return result



        


