ON_EARTH = -1
PREPARING = -2
ON_SPACE = -3
LAUNCH_NR = "LaunchNr"
LAUNCH = "Launch"
WEIGHT = "Weight"
PREPARE = "Prepare"

class Problem(object):
    def __init__(self, graph, launches):
        self.graph = graph
        self.launches = launches
        self.initial = self.__getInitialState()
        
    def __getInitialState(self):
        items = self.graph.listItems()
        initial = {}
        initial[LAUNCH_NR] = 0
        initial[WEIGHT] = 0
        for item in items.keys():
            initial[item] = ON_EARTH
        return initial
        
    def isGoal(self, state):
        for item in state.values():
            if item > -3 and item < 0:
                return False
        return True
    
    def chooseSucessor(self, item):
        return item.cost
        
    def getActions(self, state):
        actions = []
        for name, status in state.items():
            if status == ON_EARTH:
                actions.append(PREPARE+name)
        actions.append(LAUNCH)
        return actions
    
    def applyAction(self, state, action):
        # Check if state is valid
        if not self.__validate(state):
            return  None
        # Launch Action
        if action == LAUNCH:
            # Ensure imutability
            newState = {}
            for name, status in state.items():
                # If there are parts to be sent they go to space
                if status == PREPARING:
                    newState[name] = ON_SPACE
                # If not they stay the same
                else:
                    newState[name] = status
            # Flush the launch weight
            newState[WEIGHT] = 0
            # And increment the launch nr
            newState[LAUNCH_NR] = state[LAUNCH_NR] + 1
            return newState
        # Prepare a part to flight
        elif action[0:len(PREPARE)] == PREPARE:
            name = action[len(PREPARE):]
            # Get part weight
            weight = self.graph.getItem(name)
            # Check if it fits
            if self.__validatePrepare(state, name, weight):
                # Ensure imutability
                newState = state.copy()
                # Mark part as preparing
                newState[name] = PREPARING
                # Increment launch weight
                newState[WEIGHT] += weight
                return newState
    
    def getPathCost(self, cost, state1, action, state2):
        # Get starting launch
        launch = self.launches[state1[LAUNCH_NR]]
        if action == LAUNCH:
            # Add launch fixed cost only if any part is preparing
            if PREPARING in state1.values():
                return cost + launch.fixed_cost
        elif action[0:len(PREPARE)] == PREPARE:
            # Add launch variable cost according to the part's weight
            name = action[len(PREPARE):]
            weight = self.graph.getItem(name)
            return cost + weight * launch.variable_cost
        # No action
        return cost
        
    def __validate(self, state):
        # Check if there are any launches left
        if state[LAUNCH_NR] >= len(self.launches):
            return False
        return True
    
    def __validatePrepare(self, state, name, weight):
        # Weight sum of the parts have to be lesser than the launch max weight
        current_launch = self.launches[state[LAUNCH_NR]]
        if state[WEIGHT] + weight > current_launch.max_payload:
            return False
        # All the parts in space have to be connected
        # Get part links
        links = self.graph.getItemLinks(name)
        
        # Chek if there is any part in space
        if ON_SPACE in state.values():
            # Check if part got a link with a part that is in space
            for item, status in state.items():
                if (status == ON_SPACE or status == PREPARING) and item in links:
                    return True
        # If no part is in space, all of the preparing parts have to be connected
        elif PREPARING in state.values():
            for item, status in state.items():
                if status == PREPARING and item in links:
                    return True
        # If no part is preparing, any part can go
        else:
            return True
        # Invalid action
        return False
    
    