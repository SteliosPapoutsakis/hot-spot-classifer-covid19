import numpy as np
# load coo_matrix from Scipy.sparse module
from scipy.sparse import coo_matrix
'''
# of Deaths
# of Cases
# New Cases per Day (last 30 days)
# New Deaths per Day (last 30 days)
'''


class County:
    def __init__(self, name, id, state):
        self.name = name
        self.id = id
        self.state = state
        self.neighbors = []
        self.numDeaths = 0
        self.numCases = 0
        self.newCases = [0] * 30
        self.newDeaths = [0] * 30
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_neighbors(self, county_key):
        adjlist = []
        for n in self.neighbors:
            index = county_key[n.id][0]
            adjlist.append(index)
        return adjlist

    def return_tuple(self):
        result = (
              self.numCases
            , self.numDeaths)
        for i in range(len(self.newCases)):
            result = result + (self.newCases[i], self.newDeaths[i])

        return result
    

def create_county_key(counties):
    alphabetical_counties = sorted(counties, key=lambda x: x.name)
    county_key = {}
    for i in range(len(alphabetical_counties)):
        county_id = alphabetical_counties[i].id
        county_key[county_id] = (i, alphabetical_counties[i])
    
    #print(county_key)
    return county_key

def create_adj_lists(sorted_counties, county_key):
    adjlists = {}
    #Create adj list
    for count in range(len(sorted_counties)):
        #print(counties[count].id)
        adjlists[count] = sorted_counties[count].get_neighbors(county_key)

    return adjlists

def create_properties_matrix(sorted_counties):
    #Create tuple of information
    properties = []
    for county in sorted_counties:
        properties.append(county.return_tuple())
        #print(county.return_tuple())

    properties_matrix = np.array(properties)
    return coo_matrix(properties_matrix)
