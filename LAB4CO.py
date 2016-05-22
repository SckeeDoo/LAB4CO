#!usr/bin/env python
from multiprocessing import Queue

from queue import PriorityQueue

class State(object):
    def __init__ (self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = 0
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
        
        def GetDistance(self):
            pass
        def GenerateChildren(self):
            pass

class StateString(State):
    def __init__(self, value, start = 0, goal = 0):
        super(StateString, self).__init__(value, parent, start, goal)
        self.dist = self.GetDistance()

    def GetDistance(self):
        if slef.value == self.goal:
            return 0
        distance = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            distance += abs (i - self.value.index(letter))
        return distance

    def GenerateChildren(self):
        if not self.children:
            for i in xrange(len(self.goal) - 1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = StateString(val, self)
                self.children.append(child)

class AStarAlgorithm(object):
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.PriorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = StateString(self.start, 0, self.start, self.goal)
        count = 0
        self.PriorityQueue.put((0, count, startState))
        while(not self.path and sel.PriorityQueue.qsize()):
            closestChild = self.PriorityQueue.get()[2]
            closestChild.GenerateChildren()
            slef.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.distance:
                        self.path = child.path
                        break
                    self.PriorityQueue.put((child.distance, count, child))
        if not self.path:
            print ("Goal of " + self.goal + "is not possible")
        return self.path

start = "anaconda"
goal = "anaconda"
print ("processing...")
a = AStarAlgorithm(start, goal) 
a.Solve()
for i in xrange(len(a.path)):
    print (a.path[i])   