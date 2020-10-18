from parse_utils import parse_county_adj
from county_relations import County, create_county_key

counties = []

counties = parse_county_adj('./data/california_counties.txt') 

#sory by alphabetical
create_county_key(counties)