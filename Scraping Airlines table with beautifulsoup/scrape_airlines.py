from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

wiki_url = 'https://en.wikipedia.org/wiki/List_of_airline_codes'
response = requests.get(wiki_url)
soup = BeautifulSoup(response.content, "html.parser")

airlines_table = soup.find_all('table')

# Coverting data into pandas dataframe
data = pd.read_html(str(airlines_table))
df = pd.DataFrame(data[0])

airlines = df['Airline']
list_of_airlines = airlines.to_list()

with open('airlines.txt', 'w', encoding= 'utf-8') as f:
    for item in tqdm(list_of_airlines):
        f.write("{}\n".format(item))