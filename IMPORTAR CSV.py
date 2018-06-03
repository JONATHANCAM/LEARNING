# Carga de datos a travez de read_cvs
import pandas as pd
import os # concatenador 
ruta = "D:\DATA"
fileName = "BASE1.xlsx"
fullpath = os.path.join(ruta,fileName) # evita el contatenado manual " + / + "

data = pd.read_excel(fullpath)
data.head()
#data = pd.read_excel(filepath = "BASE1.xlsx",dtype = {"date":np.date})
