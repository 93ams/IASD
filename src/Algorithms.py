from Structures import Stack, Queue, PriorityQueue
from Node import *

# Tree Search Algorithms
def treeSearch(problem, ds):
    ds.append(Node(problem.initial))
    while not ds.isEmpty():
        node = ds.pop()
        if problem.isGoal(node.state):
            return node
        ds.extend(node.expand(problem))
    return None

def dfs(problem):
    return treeSearch(problem, Stack())
        
def bfs(problem):
    return treeSearch(problem, Queue())

def uniform(problem):
    return treeSearch(problem, PriorityQueue(problem.chooseSucessor))

def dls(problem, limit):
    def r_dls(node, problem, limit):
        cut = False
        if problem.isGoal(node.state):
            return node
        if node.depth == limit:
            return 'cut'
        for successor in node.expand(problem):
            res = r_dls(successor, problem, limit)
            if res == 'cut':
                cut = True
            elif res != None:
                return res

        if cut:
            return 'cut'
        return None
        
    return r_dls(Node(problem.initial), problem, limit)

def ids(problem):
    for depth in xrange(float('inf')):
        result = dls(problem, depth)
        if result is not 'cut':
            return result

# Graph Search Algorithms
def graphSearch(problem, ds):
    visited = []
    ds.append(Node(problem.initial))
    while not ds.isEmpty():
        node = ds.pop()
        if problem.isGoal(node.state):
            return node
        # Verify if visited
        if not next((item for item in visited if node.compareTo(item)), None):
            # Add to visited nodes
            visited.append(node)
            ds.extend(node.expand(problem))
    return None

def graph_dfs(problem):
    return graphSearch(problem, Stack())

def graph_bfs(problem):
    return graphSearch(problem, Queue())
    
def graph_uniform(problem):
    return graphSearch(problem, PriorityQueue(problem.chooseSucessor))
    
