class Graph(object):
    links = {}
    items = {}
    
    def __init__(self):
        pass
    
    def addItem(self, name, item):
        # Raise exception if already exists
        self.items[name] = item
        self.links[name] = []
    
    def addLink(self, item1, item2):
        self.links[item1].append(item2);
        self.links[item2].append(item1);
    
    def getItemLinks(self, name):
        return self.links[name] 
        
    def listItems(self):
        return self.items
    
    def getItem(self, name):
        return self.items[name]
    
class Queue(object):
    def __init__(self):
        self.data = []
    
    def append(self, item):
        self.data.append(item)
    
    def extend(self, items):
        self.data.extend(items)
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def pop(self):
        return self.data.pop(0)
        
class Stack(object):
    def __init__(self):
        self.data = []
    
    def append(self, item):
        self.data.append(item)
    
    def extend(self, items):
        self.data.extend(items)
    
    def isEmpty(self):
        return len(self.data) == 0
        
    def pop(self):
        return self.data.pop()
        
class PriorityQueue(object):
    def __init__(self, selectionMethod):
        self.data = []
        self.selectionMethod = selectionMethod
    
    def append(self, item):
        self.data.append(item)
    
    def extend(self, items):
        self.data.extend(items)
        
    def isEmpty(self):
        return len(self.data) == 0
        
    def pop(self):
        item = min(self.data, key=self.selectionMethod)
        self.data.remove(item)
        return item