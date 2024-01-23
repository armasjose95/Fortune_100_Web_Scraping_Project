# Import the necessary libraries.
import pandas as pd  # for data manipulation and analysis
from bs4 import BeautifulSoup  # for web scraping
import requests  # for making HTTP requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)  # retrieve the HTML content of the page,
# create a BeautifulSoup object to parse the HTML.
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

# Locate the correct table that has the data I need

table = soup.find('table', class_='wikitable sortable')


world_titles = table.find_all('th')
"""world_titles #printing
Taking the text from the list of headers(<th>)and looping through to get each header
need to strip() now because you can't strip a list"""
world_table_titles = [title.text.strip() for title in world_titles]
# print(world_table_titles)
# ['Rank', 'Name', 'Industry', 'Revenue (USD millions)', 'Revenue growth', 'Employees', 'Headquarters']


# Create an empty list to store rows of data
data_rows = []

"""Start pulling in data for each column.
Columns come in with their headers, so will need to get rid of them, so we start at [1:]
Need to loop through because this is a list.
As it gets looped through I'm finding all the td tags(individual data from each row's set of data)).
Extract the text content & strip the whitespaces to clean it.
Store the data for that row in individual_row_data. 
Append individual_row_data to the data_rows list."""
for row in table.find_all('tr')[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    data_rows.append(individual_row_data)


"""Used the pd.DataFrame constructor to create a DataFrame directly from the list of rows (data_rows). 
This constructor takes care of automatically determining the length of the DataFrame based on the length of the input data.
The data_rows list contains the rows of data extracted from the HTML table, and world_table_titles is the list of column headers."""
df = pd.DataFrame(data_rows, columns=world_table_titles)


# export this into a CSV
df.to_csv(
    r'/Users/josearmas/Desktop/Fortune_100_Web_Scraping_Project.csv', index=False)
