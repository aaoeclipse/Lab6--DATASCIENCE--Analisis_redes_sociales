# -*- coding: utf-8 -*-
"""Laboratorio6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CWW-VUOt4Y4SlUq6PMpK3otZ2_AMFFqB

# Laboratorio 6 - Analisis de Redes Sociales
# Introduccion

## Problema 1
Extraiga los datos relacionados con los temblores en Guatemala, puede utilizar cualquier red social, <br>
a la que se tenga acceso, y pueden extraerse datos de varias. Por ejemplo si extrae datos de twitter <br>
podría utilizar el hashtag #temblorgt <br>
* Explore  los  datos  que  extraiga  y  descubra  conocimiento, tendencias y elementos interesantes.

## Problema 2
Extraiga los datos relacionados con el  tráfico en la  ciudad de Guatemala, puede utilizar cualquier <br>
red social, a la que se tenga acceso, y pueden extraerse datos de varias. Por ejemplo si extrae datos <br>
de twitter podría utilizar los hashtag #TraficoGTo #TransitoGT <br>
* Explore los datos que extraiga y descubra conocimiento, tendencias y elementos interesantes.

## Problema 3
Extraiga  los  datos de las redes  sociales de  una  empresa,  una  campaña de  marketing de  una <br>
empresa o el lanzamiento  de  un  producto. <br>
Agregue  la  descripción de  la  empresa,  campaña o producto y analice las interacciones de los clientes <br>
con ellos, determine el éxito de la campaña,  producto o empresa en las interacciones de los clientes<br>


###Empresa
Se estudiara el desempeño para transmitir y el impacto que tiene Leag Of Leagends internacionalmente con el  #Worlds2018, ya que estan a punto de tener la final.<br>
ya que estan a punto de entrar a la final del campeonato 2018

# Configuraciones Iniciales
"""

!pip install twitter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk import ngrams
# Load library
from nltk.corpus import stopwords
import os
# You will have to download the set of stop words the first time
import nltk
import operator 
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

"""# Solucion problema 1

## Descarga de Informacion de Twitter
"""

from twitter import Twitter, OAuth                                                                                                                                                                                                         

ACCESS_TOKEN = '339324943-grMlvtueGSOgmP4L1ycn0HylyfAtfYkqOlbNmpsz'
ACCESS_SECRET = 'i2LECt5Gfl8oTyGxgwjYyVdxLMbHk1Qqj6wrSulK28KQf'
CONSUMER_KEY = 'xmdPRdhFjTEmYGvL8nCNe18bv'
CONSUMER_SECRET = 'BW2o4ndwdPE9KecS8YpQe5kSSJmIIe77ZqifYcDW7VLxrfjYtV'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
t = Twitter(auth=oauth)

query = t.search.tweets(q='%23temblorgt')

for s in query['statuses']:
    print(s['created_at'], s['text'], '\n')

"""## Limpieza de datos

#### Volviendo Todo en Minuscula
"""

for s in query['statuses']:
  s['text'] = s['text'].lower()

"""#### Quitar los caracteres especiales que aparecen como “#”,”@” o los apóstrofes."""

for s in query['statuses']:
  s['text'] = re.sub(r"@", "", s['text'])
  s['text'] = re.sub(r"#", "", s['text'])  
  s['text'] = re.sub(r"\'", "", s['text'])  
  s['text'] = re.sub(r"—", "", s['text'])
  s['text'] = re.sub(r'🚨',"",s['text'])
  s['text'] = re.sub(r'🔍',"",s['text'])

"""#### Quitar las url"""

for s in query['statuses']:
  s['text'] = re.sub(r"(http|ftp|https)[:A-Za-z//.0-9_]*$", "", s['text'])

"""#### Quitando Stopwords"""

for s in query['statuses']:
#   s['text'] = s['text'].split()
  s['text'] = ' '.join([word for word in s['text'].split() if word not in stop_words])

# query['statuses'] = query['statuses'].split(' ').apply(lambda x: ' '.join(k for k in x if k not in stop_words))
# dataset['reviewtext'] = dataset['reviewtext'].str.split(' ').apply(lambda x: ' '.join(k for k in x if k not in stop_words))

for s in query['statuses']:
  print(s['text'])

"""## Descubriendo Informacion
Se crea un diccionario con las palabras utilizadas y se van contando cuantas veces se repiten <br>

#### Diccionario
"""

palabrasMasComunes = {}

def word_count(str, dictionary):
  for word in str.split():
    if word in dictionary:
      dictionary[word] += 1
    else:
      dictionary[word] = 1
  return dictionary

for s in query['statuses']:
  palabrasMasComunes = word_count(s['text'], palabrasMasComunes)

# for palabra in palabrasMasComunes:

"""#### Palabras mas Comunes"""

for key in palabrasMasComunes:
    print ("%s: %s" % (key, palabrasMasComunes[key]))

"""#### Ordenamos la lista de mayor a menor"""

def keyInOrder(listName, number):
  keys = list(sorted(listName, key=listName.__getitem__, reverse=True))
  keys = keys[:number]
  firstFew = {x:listName[x] for x in keys}
  return firstFew

palabrasOrdenadas = {}

for key, value in sorted(palabrasMasComunes.items(), key=operator.itemgetter(1), reverse=True):
  palabrasOrdenadas[key] = int(value)

# sorted(palabrasMasComunes.items(), key=operator.itemgetter(1), reverse=True)
print(palabrasOrdenadas)

keys = keyInOrder(palabrasOrdenadas, 10)

print (keys)

"""#### Representacion en Graficas"""

plt.bar(keys.keys(), keys.values(), color='b')
plt.title("Palabras Mas Comunes")

"""## Conclusiones Problema 1

Viendo las palabras mas comunes: **temblorgt**, **guatemala**, **efemérides**, **años**, **magnitud** <br>
Podemos decir que las emociones de los que estan escribiendo son negativas y preocupantes, informatica

# Solucion problema 2

## Descarga de Informacion de Twitter
Se va a buscar twitts que tengan los hashtags #TraficoGTo y #TransitoGT
"""

##TraficoGTo #TransitoGT
query1 = t.search.tweets(q='%23PrecaucionGT')
query2 = t.search.tweets(q='%23TransitoGT')

for s1 in query1['statuses']:
    print(s1['created_at'], s1['text'], '\n')

for s2 in query2['statuses']:
    print(s2['created_at'], s2['text'], '\n')

"""## Limpieza de datos

#### Volviendo Todo en Minuscula
"""

for s1 in query1['statuses']:
  s1['text'] = s1['text'].lower()
  
for s2 in query2['statuses']:
  s2['text'] = s2['text'].lower()

"""#### Quitar los caracteres especiales que aparecen como “#”,”@” o los apóstrofes."""

for s1 in query1['statuses']:
  s1['text'] = re.sub(r"@", "", s1['text'])
  s1['text'] = re.sub(r"#", "", s1['text'])  
  s1['text'] = re.sub(r"\'", "", s1['text'])
  s1['text'] = re.sub(r"rt", "", s1['text'])
  
  
for s2 in query2['statuses']:
  s2['text'] = re.sub(r"@", "", s2['text'])
  s2['text'] = re.sub(r"#", "", s2['text'])  
  s2['text'] = re.sub(r"\'", "", s2['text'])
  s2['text'] = re.sub(r"rt", "", s2['text'])

"""#### Quitar las url"""

for s1 in query1['statuses']:
  s1['text'] = re.sub(r"(http|ftp|https)[:A-Za-z//.0-9_]*$", "", s1['text']) 
  
for s2 in query2['statuses']:
  s2['text'] = re.sub(r"(http|ftp|https)[:A-Za-z//.0-9_]*$", "", s2['text'])

"""#### Quitando Stopwords"""

for s1 in query1['statuses']:
  s1['text'] = ' '.join([word for word in s1['text'].split() if word not in stopwords.words('spanish')])
  
for s2 in query2['statuses']:
  s2['text'] = ' '.join([word for word in s2['text'].split() if word not in stopwords.words('spanish')])

"""## Descubriendo Informacion
Se crea un diccionario con las palabras utilizadas y se van contando cuantas veces se repiten <br>

#### Diccionario
"""

palabrasMasComunes1 = {}
palabrasMasComunes2 = {}

for s1 in query1['statuses']:
  palabrasMasComunes1 = word_count(s1['text'], palabrasMasComunes1)

for s2 in query2['statuses']:
  palabrasMasComunes2 = word_count(s2['text'], palabrasMasComunes2)

"""#### Palabras mas Comunes"""

for key in palabrasMasComunes1:
    print ("%s: %s" % (key, palabrasMasComunes1[key]))

for key in palabrasMasComunes2:
    print ("%s: %s" % (key, palabrasMasComunes2[key]))

"""###Ordenamos la ista de mayor a menor"""

palabrasOrdenadas1 = {}
palabrasOrdenadas2 = {}

for key, value in sorted(palabrasMasComunes1.items(), key=operator.itemgetter(1), reverse=True):
  palabrasOrdenadas1[key] = int(value)
  
for key, value in sorted(palabrasMasComunes2.items(), key=operator.itemgetter(1), reverse=True):
  palabrasOrdenadas2[key] = int(value)

print(palabrasOrdenadas1)
print(palabrasOrdenadas2)

keys1 = keyInOrder(palabrasOrdenadas1, 50)

keys2 = keyInOrder(palabrasOrdenadas2, 50)


print (keys1)

print (keys2)

"""#### Representacion en Graficas"""

plt.bar(keys1.keys(), keys1.values(), color='b')
plt.title("Palabras Mas Comunes")

plt.bar(keys2.keys(), keys2.values(), color='b')
plt.title("Palabras Mas Comunes")

"""## Conclusiones Problema 2
Primero se puede observar que para #TraficoGTo, no se encuentran tweets y es porque ha estado inactivo desde 2016<br>
por lo cual se cambiará a #PrecaucionGT<br>
con lo que podemos observar que al ver las palabras más comunes: Dissel, Derramado, Carro averiado, villa nueva, zona "4 y 2"<br><br>

por lo cual se puede decir que las zonas 4 y 2 son las zonas con más alertas denunciadas, el aceite derramado es el mayor causante de las alertas así como carros averiados. <br><br><br>


Ahora viendo las palabras más comunes de TransitoGT <br>
Se observa que hay varios RT sobre Almicar Montejo, por lo cual es muy difícil hacer el análisis<br>

por lo cual se decide hacer un estudio de una lista de 50 palabras en la cual se encuentran las palabras: Villa linda, villa nueva, Carro averiado, Fallas, tráiler, periférico. <br><br>

por lo cual podemos discutir que la mayor influencia sobre accidentes o avisos es por carros averiados, fallas con tráiler, con villa nueva, villa linda y el periférico siendo las áreas más afectadas.

# Solucion problema 3

## Descarga de Informacion de Twitter
Se va a buscar twitts que tengan los hashtags #Worlds2018
"""

query3 = t.search.tweets(q='%23Worlds2018')
for s3 in query3['statuses']:
    print(s3['created_at'], s3['text'], '\n')

"""## Limpieza de datos

#### Volviendo Todo en Minuscula
"""

for s3 in query3['statuses']:
  s3['text'] = s3['text'].lower()

"""#### Quitar los caracteres especiales que aparecen como “#”,”@” o los apóstrofes."""

for s3 in query3['statuses']:
  s3['text'] = re.sub(r"@", "", s3['text'])
  s3['text'] = re.sub(r"#", "", s3['text'])  
  s3['text'] = re.sub(r"\'", "", s3['text'])
  s3['text'] = re.sub(r"rt", "", s3['text'])
  s3['text'] = re.sub(r"worlds2018", "", s3['text'])

"""#### Quitar las url"""

for s3 in query3['statuses']:
  s3['text'] = re.sub(r"(http|ftp|https)[:A-Za-z//.0-9_]*$", "", s3['text'])

"""#### Quitando Stopwords"""

for s3 in query3['statuses']:
  s3['text'] = ' '.join([word for word in s3['text'].split() if word not in stopwords.words('english')])

"""## Descubriendo Informacion
Se crea un diccionario con las palabras utilizadas y se van contando cuantas veces se repiten <br>

#### Diccionario
"""

palabrasMasComunes3 = {}

for s3 in query3['statuses']:
  palabrasMasComunes3 = word_count(s3['text'], palabrasMasComunes3)

"""#### Palabras mas Comunes"""

for key in palabrasMasComunes3:
    print ("%s: %s" % (key, palabrasMasComunes3[key]))

"""###Ordenamos la ista de mayor a menor"""

palabrasOrdenadas3 = {}

for key, value in sorted(palabrasMasComunes3.items(), key=operator.itemgetter(1), reverse=True):
  palabrasOrdenadas3[key] = int(value)
  
print(palabrasOrdenadas3)

keys3 = keyInOrder(palabrasOrdenadas3, 10)


print (keys3)

"""#### Representacion en Graficas"""

plt.bar(keys3.keys(), keys3.values(), color='b')
plt.title("Palabras Mas Comunes")

"""## Conclusiones Problema 3
Se puede observar que la mayoria de fans estan a favor de cloud9 que es un equipo que proviene de USA
"""