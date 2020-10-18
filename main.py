from parse_utils import parse_county_adj
from county_relations import County

counties = []

counties = parse_county_adj('./data/california_counties.txt') 

#sory by alphabetical
sorted_counties = sorted(counties, key=lambda c: c.name)


counties = {}
adjlists = {}
count = 0
#First Create list of all counties
for county in sorted_counties:
    counties[county.id] = (count, county)
    print(county.name, ' ', count)

#Create adj list
count = 0
for county in sorted_counties:
    adjlists[count] = county.get_neighbors(idtoindex)
    print(count, ' ', adjlists[count])
    count = count + 1
