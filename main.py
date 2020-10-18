from parse_utils import *
from county_relations import *

import numpy as np

# load coo_matrix from Scipy.sparse module
from scipy.sparse import csr_matrix
from scipy import sparse as sp
counties = []



counties = parse_county_adj('./data/california_counties.txt') 


counties = sorted(counties, key=lambda c: c.name)

get_county_info("./data/california_cases_filtered.csv", counties)

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
#print('Adjacency List:\n', adjlists, '\n\n')
#print('Properties Matrix:\n', properties_matrix, '\n\n')
#print('Labels Matrix:\n', labels_matrix, '\n\n')


properties_matrix_training = csr_matrix(properties_matrix[:8][:], dtype=np.float64)
properties_matrix_testing = csr_matrix(properties_matrix[35:][:], dtype=np.float64)
properties_matrix = csr_matrix(properties_matrix[:35],dtype=np.float64)
features = sp.vstack((properties_matrix,properties_matrix_testing)).tolil()
print('Properties Training Matrix\n', properties_matrix_training)
print('Properties Testing Matrix\n', properties_matrix_testing)

labels_matrix_training = labels_matrix[:8][:]
labels_matrix_testing = labels_matrix[-22:][:]
labels_matrix = labels_matrix[:-22][:]

print(len(labels_matrix))
print(len(labels_matrix_training))
#print('Labels Training Matrix\n', labels_matrix_training)
#print('Labels Testing Matrix\n', labels_matrix_testing)

# saving files
save_objects(properties_matrix_training, './gcn/gcn/data/ind.covid.x')
save_objects(properties_matrix_testing, './gcn/gcn/data/ind.covid.tx')
save_objects(properties_matrix, './gcn/gcn/data/ind.covid.allx')

save_objects(labels_matrix_training,'./gcn/gcn/data/ind.covid.y')
save_objects(labels_matrix_testing,'./gcn/gcn/data/ind.covid.ty')
save_objects(labels_matrix,'./gcn/gcn/data/ind.covid.ally')

save_objects(adjlists,'./gcn/gcn/data/ind.covid.graph')



