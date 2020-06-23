import pandas as pd
import random as rd
import numpy as np

n=212 #numero de lineas a generar
ignorefirst=3

eBase="Encuesta_modificada.csv" #nombre la encuesta que ya tengas
eGen="nueva_data.csv" #nombre de la encuesta generada
#tienen que ser .csv


#extrayendo las variables de la encuesta
DF = pd.read_csv(eBase)
nombres=DF.columns
###

seleccion={}
for i in nombres:
    seleccion[i]={"variables":[],"siguientes":[]}

for i in range(ignorefirst,len(nombres)):#recorre las columnas y recolecta las variables con su frecuencia relativa
    seleccion[nombres[i]]["variables"]=pd.value_counts(DF.iloc[:,i])#.to_dict()
    
    if i< len(nombres)-1:
        for j in range(len(seleccion[nombres[i]]["variables"])):
            le_sigue= DF.iloc[:,i] == seleccion[nombres[i]]["variables"].index[j]
            seleccion[nombres[i]]["siguientes"].append(pd.value_counts(DF[le_sigue].iloc[:,i+1]))
#    print(seleccion[nombres[i]]["siguientes"])



d={}
for i in nombres:
    d[i]=[]

#print(seleccion)

for x in range(n):#cantidad de filas generadas
    elec=rd.choices(seleccion[nombres[ignorefirst]]["variables"].index,
                    weights=seleccion[nombres[ignorefirst]]["variables"].values,
                    k=1)
    d[nombres[ignorefirst]].append(elec[0])
#    print(d[nombres[ignorefirst]][-1]==seleccion[nombres[ignorefirst]]["variables"].index)
#    print(len(seleccion[nombres[ignorefirst]]["variables"]))
#    print(np.where(d[nombres[ignorefirst]][-1]==seleccion[nombres[ignorefirst]]["variables"].index)[0][0])

    for i in range(len(nombres)-1):#recorrer columnas
#        print(i)
        if i<ignorefirst:
            d[nombres[i]].append("")
            continue

        variables=seleccion[nombres[i]]["variables"].index
#        print(variables)
#        print(d[nombres[i]][-1])
        sig=np.where(variables==d[nombres[i]][-1])[0][0]
#        print(sig)
#        print(seleccion[nombres[i]]["siguientes"][sig].values)

        elec=rd.choices(seleccion[nombres[i]]["siguientes"][sig].index,
                        weights=seleccion[nombres[i]]["siguientes"][sig].values,k=1)

        d[nombres[i+1]].append(elec[0])


#print(d)




##convirtieno el diccionario a un dataframe y guardandolo en un archivo.csv
d=pd.DataFrame.from_dict(d)

d.to_csv(eGen,sep=";")
###
