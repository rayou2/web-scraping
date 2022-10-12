import pandas as pd
import requests
from bs4 import BeautifulSoup

page2 = requests.get('https://en.wikipedia.org/wiki/Asian_cuisine')
page2

# Create a BeautifulSoup object
soup = BeautifulSoup(page2.text, 'html.parser')

culture = soup.find_all('span',class_='mw-headline')

cuisine= []
for t in culture: 
    print (t.text)
    data = t.text
    cuisine.append(data)

#check number of items
len(cuisine)
cuisine

## put this together into a dataframe
df = pd.DataFrame({'cuisine':cuisine})

df.to_csv('data/cuisine_list')