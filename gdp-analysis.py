import csv

def get_highest_gdp(data, year):
    highest_gdp = float(data[0][year])
    for row in data:
        val = float(row[year])
        if val > highest_gdp:
            highest_gdp = val
    return highest_gdp 
    
def get_lowest_gdp(data, year):
    lowest_gdp = float("inf")
    for row in data:
        val = float(row[year])
        if val < lowest_gdp:
            lowest_gdp = val 
    return lowest_gdp

# return the GDP of the specified state and year 

def get_state_gdp(data, state, year):
    for row in data: 
        if row['GeoName'] == state:
            return row[year]
        
   
# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(get_highest_gdp(list_data, '2020'))
# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(get_lowest_gdp(list_data,'2020'))
# get GDP for Kansas in 2020 
print(get_state_gdp(list_data, 'California', '2020'))




# pseudo code 
# loop through every row
    # for row in data:
        # state_gdp = row[state]
        # val = float(row[year])
        # if the state exists in this line
        # if state in data:
            # search year in the data
            # for year in data: 
                # set variable to gdp value 
                #val = state_gdp
            # return state_gdp
