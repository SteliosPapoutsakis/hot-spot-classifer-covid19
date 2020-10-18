from parse_utils import parse_county_adj
from county_relations import *

import numpy as np

# load coo_matrix from Scipy.sparse module
from scipy.sparse import coo_matrix

counties = []



counties = parse_county_adj('./data/california_counties.txt') 
#Retrieve other information

sorted_counties = sorted(counties, key=lambda c: c.name)
county_key = create_county_key(counties)

adjlists = create_adj_lists(sorted_counties, county_key)

properties_matrix = create_properties_matrix(sorted_counties)

'''
Final Results
'''
print('Adjacency List:\n', adjlists, '\n\n')
print('Properties Matrix:\n', properties_matrix, '\n\n')