import requests
from natsort import natsorted
from bs4 import BeautifulSoup

url = 'https://fr.indeed.com/emplois?q=chauffeur+poids+lourd+%E2%82%AC35%C2%A0000'

r = requests.get(url)
data = []
if(r.ok):
      soup = BeautifulSoup(r.text, 'html.parser')
      salarySpans = soup.findAll("div", {'class' : 'salary-snippet'})
      jobsTitles = soup.findAll("h2", {'class' : 'jobTitle'})

      for i in range(len(salarySpans)):
            print(salarySpans[i].text)
            salarySplit = salarySpans[i].text.split()
            print(salarySplit)

            salary = salarySplit[0] + salarySplit[1]
            if "an" in salarySplit:
                  minSalaryPerYear = salarySplit[0] + salarySplit[1]
                  minSalaryPerMonth = int(minSalaryPerYear) // 12
                  salary = minSalaryPerMonth
                  print("c'est en année")

            if "jour" in salarySplit:
                  minSalaryPerDay = salarySplit[0]
                  minSalaryPerMonth = int(minSalaryPerDay) * 30
                  salary = minSalaryPerMonth
                  print("c'est en jours")

            data.append(str(salary) + " € par mois : " + jobsTitles[i].text)
            print(str(salary) + " € par mois : " + jobsTitles[i].text)
            print("====")


            print(data)
            data = natsorted(data)
            print(data)

            final_data = data[-3:]
            print(final_data)

            with open('salary.txt', 'w') as file:
                        for d in final_data:
                              file.write(d + '\n');

else:
      print('error')

