from __future__ import division
from __future__ import print_function
import sys
import math
import time
import timeit
import queue 
import numpy as np
from collections import deque
from queue import PriorityQueue
import heapq
import resource 


## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        if self is None: return other is None
        elif other is None: return self is None
        else: return self.config == other.config



    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. 
        [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)
        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []
        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)
        #add max depth 
   
    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3*i : 3*(i+1)])
    
    def move_up(self):

        """ 
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        new_list = self.config[:]
        n = self.n
        index_val = self.blank_index
       
        if index_val < n :
            return None
         
         
        else:
            temp = 0
            temp = new_list[index_val - n]
            new_list[index_val - self.n] = 0
            new_list[index_val] = temp 
            """""
                print("org config")
                print(self.config)
                print("new list - up")
                print(new_list)
            """
            return PuzzleState(new_list,n, self, "up", cost = self.cost+1)
     
        
    

    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """

        new_list = self.config[:]
        n = self.n
        index_val = self.blank_index
       
        if index_val >= (n*n-n) :
            return None
         
        else:
            temp = 0
            temp = new_list[index_val + self.n]
            new_list[index_val + self.n] = 0
            new_list[index_val] = temp 
            cost = self.cost+1
            """""
                print("org config")
                print(self.config)
                print("new list - down")
                print(new_list)
            """""
            return PuzzleState(new_list, n, self, "down", cost)
        
        
    
       
      
    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        new_list = self.config[:]
        n = self.n
        index_val = self.blank_index
        
        if index_val % n == 0:
            return None
        
        else:
            temp = 0
            temp = new_list[index_val - 1 ]
            new_list[index_val - 1] = 0
            new_list[index_val] = temp 
            # print(new_list + "3")
            cost = self.cost+1
            """""
                print("org config")
                print(self.config)
                print("new list - left")
                print(new_list)
            """
            return PuzzleState(new_list, n,self,"left", cost)
        
        

       
    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        new_list = self.config[:]
        n = self.n
        index_val = self.blank_index
        if index_val in [2,5,8]:
            return None
         
        else:
            temp = 0
            temp = new_list[index_val + 1 ]
            new_list[index_val + 1] = 0
            new_list[index_val] = temp 
            cost = self.cost+1
            """""
                print("org config")
                print(self.config)
                print("new list - right")
                print(new_list)
            """
            return PuzzleState(new_list,n, self, "right", cost)
     
      
    def expand(self):
        """ Generate the child nodes of this node """
        
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children
        
        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]
        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children

# Function that Writes to output.txt
### Students need to change the method to have the corresponding parameters

def writeOutput(path_to_goal, cost_of_path, nodes_expanded, search_depth, max_search_depth, running_time, max_ram_usage,):
    path = list(reversed(path_to_goal))
    f = open('output.txt', 'w')
    f.write('path_to_goal: ')
    f.write(str(path))
    f.write('\n')
    f.write('cost_of_path: ')
    f.write(str(cost_of_path))
    f.write('\n')
    f.write('nodes_expanded: ')
    f.write(str(nodes_expanded))
    f.write('\n')
    f.write('search_depth: ')
    f.write(str(search_depth))
    f.write('\n')
    f.write('max_search_depth: ')
    f.write(str(max_search_depth))
    f.write('\n')
    f.write('running_time: ')
    f.write(str(running_time))
    f.write('\n')
    f.write('max_ram_usage: ')
    f.write(str(max_ram_usage))

   
def bfs_search(PuzzleState):
    """BFS search"""
    bfs_start_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start = timeit.default_timer()
    frontier_obj = deque([PuzzleState])
    frontier_config = set(tuple(PuzzleState.config))
    explored = set() 
    nodes_expand = 0
    path = []
    max_depth = 0
    
    while len(frontier_obj)!=0:
        State = frontier_obj.pop() 
        explored.add(tuple(State.config))

        if test_goal(State):
            search_depth = State.cost
            while State.action != "Initial":
                path.append(State.action)
                State = State.parent

            bfs_ram = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - bfs_start_ram)/(2**20)
            stop = timeit.default_timer()
            time = stop - start
            writeOutput(path, len(path), nodes_expand, search_depth, max_depth, time, bfs_ram)

            return
        
        result = State.expand()
        nodes_expand += 1 
        for children in result:
            if (tuple(children.config) not in frontier_config) and (tuple(children.config) not in explored):
                    frontier_obj.appendleft(children)
                    frontier_config.add(tuple(children.config))
                    current_cost = children.cost 
                    if current_cost > max_depth: max_depth = max(current_cost, max_depth)

        
    return False
    
def dfs_search(PuzzleState):
    """DFS search"""
    dfs_start_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start = timeit.default_timer()
    frontier_obj = deque([PuzzleState])
    frontier_config = set(tuple(PuzzleState.config))
    explored = set() 
    path = []
    nodes_expand = 0
    max_depth = 0

    while len(frontier_obj)!=0:
        State = frontier_obj.popleft() 
        explored.add(tuple(State.config))

        if test_goal(State):
            search_depth = State.cost
            while State.action != "Initial":
                path.append(State.action)
                State = State.parent  
            
            dfs_ram = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - dfs_start_ram)/(2**20)
            stop = timeit.default_timer()
            time = stop - start
            writeOutput(path, len(path), nodes_expand, search_depth, max_depth, time, dfs_ram)   
            
            
              
            return

        result = State.expand()
        nodes_expand += 1
        result.reverse()
        for children in result:
            if (tuple(children.config) not in frontier_config) and (tuple(children.config) not in explored):
                    frontier_obj.appendleft(children) 
                    frontier_config.add(tuple(children.config))
                    current_cost = children.cost 
                    if current_cost > max_depth: max_depth = max(current_cost, max_depth)
    
    return False 
   
def A_star_search(PuzzleState):
    """A * search"""
    A_start_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start = timeit.default_timer()
    frontier = []                           
    heapq.heappush(frontier, tuple([PuzzleState.cost + calculate_total_cost(PuzzleState),PuzzleState]))
    frontier_config = set(tuple(PuzzleState.config))
    explored = set()
    nodes_expand = 0
    path = []
    max_depth = 0
    
    while len(frontier)!=0:
        state = heapq.heappop(frontier)[1]
        explored.add(tuple(state.config))

        if test_goal(state):
            search_depth = state.cost
            while state.action != "Initial":
                path.append(state.action)
                state = state.parent 

            A_ram = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - A_start_ram)/(2**20)
            stop = timeit.default_timer()
            time = stop - start
            writeOutput(path, len(path), nodes_expand, search_depth, max_depth, time, A_ram)
      

            return


        result = state.expand()
        nodes_expand += 1 
        for children in result:
            if (tuple(children.config) not in frontier_config) and (tuple(children.config) not in explored):
                heapq.heappush(frontier,tuple([children.cost + calculate_total_cost(children),children]))
                frontier_config.add(tuple(children.config)) 
                current_cost = children.cost 
                if current_cost > max_depth: max_depth = max(current_cost, max_depth)
    
            elif (tuple(children.config) in frontier_config):
                DecreaseKey(children,frontier)

    return False 

def calculate_total_cost(state):
    """calculate the total estimated cost of a state""" 
    total = 0
    for idx in state.config:
        total += calculate_manhattan_dist(idx,state.config[idx], state.n)

    return total

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    
    col1 = idx%n
    row1 = int(idx/n)
    col2 = value % n
    row2 = int(value/n)

    return (abs(col1-col2)+abs(row1-row2))


def test_goal(PuzzleState):
    """test the state is the goal state or not"""
    goal = [0,1,2,3,4,5,6,7,8]
        
    if goal == (PuzzleState.config):
        return True 

def DecreaseKey(child, frontier):
    #sort through fronteir
    
    for idx in range(len(frontier)):
        if frontier[idx][1].config == child.config:
            if child < frontier[idx][1]:
                frontier[idx] = (child.cost + calculate_total_cost(child), child)
                heapq.heapify(frontier) #corrects value position
    return 

# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    
    if   search_mode == "bfs": bfs_search(hard_state)   
    elif search_mode == "dfs": dfs_search(hard_state)
    elif search_mode == "ast": A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")

    end_time = time.time()
    print("Program completed in %.3f second(s)"%(end_time-start_time))
if __name__ == '__main__':
    main()