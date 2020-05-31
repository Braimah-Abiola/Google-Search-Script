import requests
import bs4
import sys
import webbrowser

# Print text while downloading the Google page
print("Googling...")
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:])) 
res.raise_for_status()

# Retrieve top search result links. 
soup = bs4.BeautifulSoup(res.text)

# Open Browser Tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems)) 

for i in range(numOpen):    
    webbrowser.open('http://google.com' + linkElems[i].get('href'))