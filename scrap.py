from bs4 import BeautifulSoup
import requests
import pandas as pd
#Descargar HTML
url = "https://colombia.as.com/resultados/futbol/colombia_i/clasificacion/"
page = requests.get(url)
#Transformar a beautifulsoup para identificar varios elementos de html
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos
eq = soup.find_all('span',class_='nombre-equipo')

equipos = list()
count = 0
for i in eq:
    if count < 20:
        equipos.append(i.text)
    else:
        break
    count += 1

#Puntos
pt = soup.find_all('td',class_='destacado')

puntos = list()
count = 0
for i in pt:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count += 1

#Convertirlo a DataFrame

df = pd.DataFrame({'Nombre':equipos,'Puntos':puntos},index=list(range(1,21)))
print(df)
