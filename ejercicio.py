# 1. importe de librerias
#
import pandas as pd
import zipfile as zf
import os 
import glob
import fileinput

# 2. descomprimir el archivo. ZIP y lectura de las carpetas
archivo_origen = "data.zip"
archivo_destino = "data"

with zf.ZipFile(archivo_origen, "r") as zip_referen:
    zip_referen.extractall(archivo_destino)
    

# 3. Proceso de iteracion para leer las carpetas y archivos y almacenarlas en una lista de tuplas
sequence=[]

elements = os.listdir(archivo_destino)

for element in elements[:2]:
    files = os.listdir(f"{archivo_destino}/{element}")
    for file in files [1:]:
        filenames= glob.glob(f"{archivo_destino}/{element}/{file}/*")
        with fileinput.input(files = filenames) as f:
            for linea in f:
                sequence.append((fileinput.filename(), linea))

# 4. Conversión de una lista de tuplas a una lista de listas, para facilitar el manejo
linea_texto= [list(tupla) for tupla in sequence]

# 5. Proceso de conversión del dataframe a la forma que necesito

# 5.1. Conversión de la lista de listas al dataframe inicial
df = pd.DataFrame(linea_texto,
                columns= ["directory", "phrase"],
            )

# 5.2. Pasos iniciales separación de algunas columnas 

nueva_columnas = df["directory"].str.split("/", expand=True)
nueva_columnas.columns= ["data", "class","senti_text"]

nueva_columnas2= nueva_columnas["senti_text"].str.split("\\", expand=True)
nueva_columnas2.columns = ["sentiment", "text"]
nueva_columnas2["text"]= nueva_columnas2["text"].str.replace(".txt","")

# 5.3. Concatenación de los dataframe creados. 
df_ajus = pd.concat([df, nueva_columnas, nueva_columnas2], axis = 1)
df_ajus = df_ajus.drop(columns= ["data","directory","senti_text", "text"])


# 5.4. Separación de la información según el tipo de info requerida en el ejercicio
df_train_csv = df_ajus[df_ajus["class"]== "train"]
df_test_csv = df_ajus[df_ajus["class"]== "test"]

df_train_csv = df_train_csv.drop(columns= ["class"])
df_test_csv = df_test_csv.drop(columns=["class"])


## 6. CONVERSIÓN DE LOS DATAFRAME A UN ARCHIVO CSV

df_train_csv.to_csv("train_dataset.csv", index= False)
df_test_csv.to_csv("test_dataset.csv", index= False)