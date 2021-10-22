import requests
from tkinter import *
from bs4 import BeautifulSoup

url = 'https://www.pokebip.com/pokedex/pokemon'

r = requests.get(url)
data = []

pokeTypes = {
      'Acier' : [0, "#5A8EA2"],
      'Combat' : [0, "#CE416B"],
      'Dragon' : [0, "#0B6DC3"],
      'Eau' : [0, "#5090D6"],
      'Electrik' : [0, "#F4D23C"],
      'Fée' : [0,"#EC8FE6"],
      'Feu' : [0, "#FF9D55"],
      'Glace' : [0, "#73CEC0"],
      'Insecte' : [0, "#91C12F"],
      'Normal' : [0, "#919AA2"],
      'Plante' : [0, "#63BC5A"],
      'poison' : [0, "#AA6BC8"],
      'Psy' : [0, "#FA7179"],
      'Roche' : [0, "#C5B78C"],
      'Sol' : [0, "#D97845"],
      'Spectre' : [0, "#5269AD"],
      'Ténèbres' : [0, "#5A5465"],
      'Vol' : [0, "#8FA9DE"]
}

print(pokeTypes['Acier'][1])

window = Tk()
# label = Label(window, text="hello world")
# label.pack()

canvas = Canvas(window, width=500, height=500)
# ligne1 = canvas.create_line(0,100,200,200, fill="red")
# canvas.pack()

# window.mainloop()

if(r.ok):
      s = BeautifulSoup(r.text, 'html.parser')
      tbody = s.findAll('tbody')[0]
      tr = tbody.findAll('tr')
      print(len(tr))
      for i in range(len(tr)):
            tds = tr[i].findAll('td')
            name = tds[2].find('a').text

            types = tds[3].findAll('img')
            for t in range(len(types)):
                  type = types[t]["alt"]
                  pokeTypes[type][0] += 1
                  print(type)


            # print(name)
            print("===")
      print(pokeTypes)

      x = 0
      y = 20
      for key in pokeTypes:
            print(key)
            canvas.create_rectangle(0, x, pokeTypes[key][0], y, fill=pokeTypes[key][1], outline="")
            x += 20
            y += 20
            
      canvas.pack()
      window.mainloop()
else:
      print('error')
