# AI
COMSW 4701 taught by Professor Ansaf Salleb-Aouissi 

This course is a graduate-level introduction to Artificial Intelligence. We learned the fundamental concepts of AI and how to apply them to the design and implementation of intelligent agents.

Topics include:
1) Introduction to AI, definition, history of AI, Turing test
2) Intelligent agents, uninformed search
3) Heuristic search, greedy search, A* algorithm, stochastic search
4) Adversarial search, game playing
5) Constraint satisfaction problems
6) Logical agents: propositional logic and first order logic
7) Machine Learning: basic concepts, linear models, K nearest neighbors, overfitting
8) Machine Learning: perceptron, neural networks, naive Bayes, decision trees, ensemble models, and unsupervised learning
9) Probabilistic reasoning and Bayesian networks
10) AI applications: healthcare, natural language processing, vision, etc. (time-permitting).
11) AI and Ethics

Homework 1: 
  
  The N-puzzle game consists of a board holding N = m^2 − 1 distinct movable tiles, plus one empty space. There is
one tile for each number in the set {0, 1,..., m2 − 1}. In this assignment, we will represent the blank space with the
number 0 and focus on the m = 3 case (8-puzzle).
In this combinatorial search problem, the aim is to get from any initial board state to the configuration with all
tiles arranged in ascending order {0, 1,..., m^2 − 1} – this is your goal state. The search space is the set of all possible
states reachable from the initial state. Each move consists of swapping the empty space with a component in one of
the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}. Give each move a cost of one. Thus, the total cost of a path will
be equal to the number of moves made.

In my solution I implement 3 algorithms; bfs (Breadth-First Search), dfs (Depth-First Search) and ast (A-Star Search) with the Manhattan priority function heuristic.

Homework 2:
  
  My implementation of a Sudoku solver. Here I implement a backtracking search using the minimum remaining value heuristic, and I apply forward checking to reduce the variables' domains.

Homework 3:
  
  My implementation of an adversarial search agent to play the 2048-puzzle game.
  The following was implemented in the solution: expectiminimax algorithm, alpha-beta pruning, multiple heuristic functions, and heuristic weights.

Homework 4:
  
  My implementation of two small and separate machine learning algorithms, the Perceptron and Linear Regression. 
    
