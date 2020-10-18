

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
        self.numDeaths = 0
        self.numCases = 0
    

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_neighbors(self, county_key):
        adjlist = []
        for n in self.neighbors:
            index = county_key[n.id][0]
            adjlist.append(index)
        return adjlist

    '''def return_tuple:
        return (name, )
        '''
    

def create_county_key(counties):
    alphabetical_counties = sorted(counties, key=lambda x: x.name)
    county_key = {}
    for i in range(len(alphabetical_counties)):
        county_id = alphabetical_counties[i].id
        county_key[county_id] = (i, alphabetical_counties[i])
    
    print(county_key)
    return county_key
