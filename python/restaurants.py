import requests
from bs4 import BeautifulSoup

url = 'https://fr.wikipedia.org/wiki/Liste_de_cha%C3%AEnes_de_restaurants'

r = requests.get(url)
data = []
if(r.ok):
      s = BeautifulSoup(r.text, 'html.parser')
      tbody = s.findAll('tbody')
      # print(tbody[0].text)
      tr = tbody[0].findAll('tr')
      i = 1

      while i < len(tr):
            tds = tr[i].findAll('td')
            name = tds[0].text
            realName = name.split('\n')[0];

            created = tds[4].text
            realCreated = created.split('\n')[0]

            places = tds[5].text
            splitPlaces = places.split()
            realPlaces = ""
            for j in range(len(splitPlaces)):
                  realPlaces += splitPlaces[j] + " "

            print (places)
            print (realPlaces)
            print('======')
            data.append(realName + " : créé en " + realCreated + ", nombre de restaurants : " + realPlaces + "\n")
            # print(name + " : créé en " + created + ", nombre de restaurants : " + nplaces)
            i += 1

      with open('restaurants.txt', 'w') as file:
            for d in data:
                  file.write(d + '\n');
else:
      print('error')