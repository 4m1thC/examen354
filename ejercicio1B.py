# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:22:05 2022

@author: AmiTh
"""
import pandas as pd
import numpy as np

excel = pd.read_csv(r"C:\Users\AmiTh\Desktop\INF354\examen/insurance.csv")

df = pd.DataFrame(excel)
print("Datos de la columna de edades:")
print("primer cuartil: ", np.percentile(df.age, 25))
print("percentil 50: ", np.percentile(df.age, 50))

print("Datos de la columna de Índice de masa corporal:")
print("primer cuartil: ", np.percentile(df.bmi, 25))
print("percentil 50: ", np.percentile(df.bmi, 50))

print("Datos de la columna de niños(cantidad de hijos):")
print("primer cuartil: ", np.percentile(df.children, 25))
print("percentil 50: ", np.percentile(df.children, 50))

print("Datos de la columna de cargos(costos médicos individuales):")
print("primer cuartil: ", np.percentile(df.charges, 25))
print("percentil 50: ", np.percentile(df.charges, 50))

