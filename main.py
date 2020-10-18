from parse_utils import parse_county_adj, get_county_info
from county_relations import County, create_county_key

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
adjlists = {}
#Create adj list
for count in range(len(sorted_counties)):
    # print(counties[count].name)
    adjlists[count] = sorted_counties[count].get_neighbors(county_key)
    # print(count, ' ', adjlists[count])



#Create tuple of information
# properties = []
# for 






