#import networkx as nx

#G = nx.Graph()

class DayValue:
    def __init__(self, newcases, newdeaths):
        self.newcases = newcases
        self.newdeaths = newdeaths

class County:
    def __init__(self, name, id, state):
        self.name = name
        self.id = id
        self.state = state
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

