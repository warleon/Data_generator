import pandas as pd
import random as rd

n=140

eBase="Encuesta.csv" #la encuesta que ya tengas

#extrayendo las variables de la encuesta
DF = pd.read_csv(eBase)
nombres=DF.columns
###

#creado un diccionario 
d={}
for i in nombres:
    d[i]=[]
###

#generando los valores a partir de los valores previos en la encuesta
for x in range(n):
    for i in range(len(nombres)):
        elements=DF.iloc[:,i].unique()
        elec=rd.choice(elements)
        d[nombres[i]].append(elec)
###

#convirtieno el diccionario a un dataframe y guardandolo en un archivo.csv
d=pd.DataFrame.from_dict(d)

d.to_csv("experiment.csv",sep=";")
###
