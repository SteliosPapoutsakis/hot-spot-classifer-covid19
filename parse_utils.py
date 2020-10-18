from county_relations import County
from scipy import sparse
import pickle
import re
import pandas


rx_dict =  {
    'main_county': re.compile(r'"(?P<name>([a-z]|[A-Z]| )+) County, (?P<state>[A-Z]+)"\t+(?P<id>[0-9]+)\t+"(?P<adj_name>([a-z]|[A-Z]| )+) County, (?P<adj_state>[A-Z]+)"\t+(?P<adj_id>[0-9]+)$'),
    'adjacent_county': re.compile(r'\t+"(?P<adj_name>([a-z]|[A-Z]| )+) County, (?P<adj_state>[A-Z]+)"\t+(?P<adj_id>[0-9]+)$')
}

# functions for saving the objects
def save_sparse_matrix(matrix, file_path):
    sparse.save_npz(file_path, matrix)

def save_objects(obj, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)

def parse_line(line):
    '''
    Do A Regex search against all defined patterns and return the key and match the works
    '''
    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    
    #if there are no matches
    return None, None


def parse_county_adj(filepath):
    counties = []

    with open(filepath, 'r') as adjfile:
        line = adjfile.readline()
        county = None
        while line:
            key, match = parse_line(line)
            #print(line)
            if key == 'main_county':
                name = match.group('name')
                id = match.group('id')
                state = match.group('state')

                county = County(name, id, state)
                #print("Created County: ", county.name)

                adj_name = match.group('adj_name')
                adj_id = match.group('adj_id')
                adj_state = match.group('adj_state')

                adj_county = County(adj_name, adj_id, adj_state)
                
                if adj_county.state == 'CA':
                    county.add_neighbor(adj_county)
                #print("Added Ajacent County: ", adj_county.name)

                counties.append(county)
            
            if key == 'adjacent_county':
                adj_name = match.group('adj_name')
                adj_id = match.group('adj_id')
                adj_state = match.group('adj_state')

                
                adj_county = County(adj_name, adj_id, adj_state)
                #print("Added Ajacent County: ", adj_county.name)
                if adj_county.state == 'CA':
                    county.add_neighbor(adj_county)

            line = adjfile.readline()
    return counties

