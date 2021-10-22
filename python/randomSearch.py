import requests
import random
from bs4 import BeautifulSoup

words_file = "allworlds.txt"
WORDS = open(words_file).read().splitlines()
word = random.choice(WORDS)
print(word)

url = 'https://www.google.com/search?q=' + word

r = requests.get(url)
data = []
if(r.ok):
      soup = BeautifulSoup(r.text, 'html.parser')
      results = soup.findAll(id="rso")

      print(results)

