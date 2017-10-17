class Node(object):
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state=state
        self.parent=parent
        self.action=action
        self.cost=cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    
    def getPath(self):
        path = []
        node = self
        while node and node.parent:
            path.append(node)
            node = node.parent
        return path[::-1]
        
    def expand(self, problem):
        actions = problem.getActions(self.state)
        nodes = []
        for action in actions:
            newState = problem.applyAction(self.state, action)
            if newState != None:
                cost = problem.getPathCost(self.cost, self.state, action, newState)
                #print cost
                nodes.append(Node(newState, self, action, cost))
        return nodes
        
    def compareTo(self, node):
        for name, value in self.state.items():
            if node.state[name] != value:
                return False
        return True