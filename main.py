<<<<<<< HEAD
from parse_utils import parse_county_adj, get_county_info
from county_relations import County, create_county_key
=======
from parse_utils import parse_county_adj
from county_relations import *

import numpy as np

# load coo_matrix from Scipy.sparse module
from scipy.sparse import coo_matrix
>>>>>>> 2edaed87348366f2446b073139b4ea70798ccc0f

counties = []



counties = parse_county_adj('./data/california_counties.txt') 
get_county_info("data\california_cases_filtered.csv", counties)

for county in counties:
    print("""
    Name: {}, 
    Cases: {}, 
    Deaths: {}, 
    Cases/day: {}, 
    Deaths/day: {}""".format(county.name, county.numCases, county.numDeaths, 
    county.newcases, county.newdeaths))

#Retrieve other information

sorted_counties = sorted(counties, key=lambda c: c.name)
county_key = create_county_key(counties)
<<<<<<< HEAD
adjlists = {}
#Create adj list
for count in range(len(sorted_counties)):
    # print(counties[count].name)
    adjlists[count] = sorted_counties[count].get_neighbors(county_key)
    # print(count, ' ', adjlists[count])



#Create tuple of information
# properties = []
# for 



=======
>>>>>>> 2edaed87348366f2446b073139b4ea70798ccc0f

adjlists = create_adj_lists(sorted_counties, county_key)

properties_matrix = create_properties_matrix(sorted_counties)

'''
Final Results
'''
print('Adjacency List:\n', adjlists, '\n\n')
print('Properties Matrix:\n', properties_matrix, '\n\n')