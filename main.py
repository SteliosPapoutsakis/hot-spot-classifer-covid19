<<<<<<< HEAD
from parse_utils import *
=======
from parse_utils import parse_county_adj, get_county_info
from county_relations import County, create_county_key
from parse_utils import parse_county_adj
>>>>>>> 580e5407c50770f46f0d4c26688bcff4d6537aed
from county_relations import *

import numpy as np

# load coo_matrix from Scipy.sparse module
from scipy.sparse import coo_matrix

counties = []



counties = parse_county_adj('./data/california_counties.txt') 


counties = sorted(counties, key=lambda c: c.name)

get_county_info("data\california_cases_filtered.csv", counties)

'''for county in counties:
    print("""
    Name: {}, 
    Cases: {}, 
    Deaths: {}, 
    Cases/day: {}, 
    Deaths/day: {}""".format(county.name, county.numCases, county.numDeaths, 
    county.newCases, county.newDeaths))'''

#Retrieve other information
counties = parse_labels('./data/hotspot_info.csv', counties)

county_key = create_county_key(counties)

adjlists = create_adj_lists(counties, county_key)

properties_matrix = create_properties_matrix(counties)
labels_matrix = create_labels_matrix(counties)

'''
Final Results
'''
print('Adjacency List:\n', adjlists, '\n\n')
print('Properties Matrix:\n', properties_matrix, '\n\n')
print('Labels Matrix:\n', labels_matrix, '\n\n')