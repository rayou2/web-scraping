import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://wildlifetrip.org/africa-savanna-animals/')
page

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

description = soup.find_all('h2')

animal = []
for t in description: 
    print (t.text)
    data = t.text
    animal.append(data)

#check number of items
len(animal)
animal

## put this together into a dataframe
df = pd.DataFrame({'animals':animal})

df.to_csv('data/animal_list')