import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup)

soup.find_all('table')[1]


soup.find_all('table', class_='wikitable sortable')

# wikitable sortable jquery-tablesorter

table = soup.find_all('table')[1]
print(table)


world_titles = table.find_all('th')
world_titles
# Taking the text from the list of headers(<th>)and looping through to get each header
# need to strip() now because you can't strip a list
world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)
# ['Rank', 'Name', 'Industry', 'Revenue (USD millions)', 'Revenue growth', 'Employees', 'Headquarters']


# enter titles into pandas data frame
df = pd.DataFrame(columns=world_table_titles)
df
# imported pandas
# headers are now printed


# start pulling in data for each column
# they come in with their headers, so will need to get rid of them
column_data = table.find_all('tr')

# need to loop through because this is a list
# as it gets looped through I'm finding all and looking for the td tags(individual data(row data))
# then I'm taking each piece of data & getting out the text & stripping it to clean it
# now in a list for each individual row
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]


# how many roles are in this data frame
# then take the length and use it when I put in this new info
# checking length of our data frame each time it's looping through
# and then I'm going to put the info in the next position by appending it to our empty data frame
length = len(df)
df.loc[length] = individual_row_data
df
# export this into a CSV
df.to_csv(r'/Users/josearmas/Desktop/Fortune_100_Web_Scraping_Project\Companies.csv', index=False)
