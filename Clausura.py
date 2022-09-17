from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.auf.org.uy/uruguayo-1-division/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')

# TOP 20- Equipos de primera división futbol Uruguayo
eq = soup.find_all('span',class_='valign-medio hidden-sm')
cuenta = 0
equipos = list()

for x in eq:
    if cuenta < 20:
        equipos.append(x.text)
        print(x.text)
    else:
        break
    cuenta +=1


#Puntos de los equipos
pts = soup.find_all('div',class_='col-2 bold text-center')
cuenta = 0
puntos = list()
for x in pts:
    if cuenta < 20:
        puntos.append(x.text)
    else:
        break
    cuenta +=1

df= pd.DataFrame({'Nombre':equipos,'Puntos':puntos},index=list(range(1,21)))
print(df)
