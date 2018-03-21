import random
import requests
from bs4 import BeautifulSoup
r = requests.get('https://jbzd.pl')
soup = BeautifulSoup(r.text, 'html.parser')
urls = soup.findAll("img", class_="resource-image")
draw_url = urls[random.randint(0, len(urls) - 1)].attrs['src']
print(draw_url)
