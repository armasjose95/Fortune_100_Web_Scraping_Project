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
