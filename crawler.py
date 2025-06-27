import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the page
req = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
webpage = req.text

# Save the page as HTML
with open("filename.html", "wb") as f:
    f.write(webpage.encode('utf-8'))

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(webpage, 'html.parser')

# Get all <p> tags with no class
paragraphs = soup.find_all('p', attrs={"class": False})

# Extract links with titles from all paragraphs
data = {"title": [], "href": []}
for p in paragraphs:
    for link in p.find_all('a', attrs={"title": True}):
        data["title"].append(link["title"])
        data["href"].append(link["href"])

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("Sample_data.csv", index=False, encoding='utf-8')      
