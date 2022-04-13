# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:43:38 2022

@author: AmiTh
"""
import pandas as pd
import matplotlib.pyplot as plt

excel = pd.read_csv(r"C:\Users\AmiTh\Desktop\INF354\examen/insurance.csv")

df = pd.DataFrame(excel)

#grafico de edades
valores_x1 = df["age"].unique()
valores_y1 = df["age"].value_counts().tolist()
plt.bar(valores_x1, valores_y1)
plt.title("grafico de edades")
plt.show()


#grafico de Índice de masa corporal
valores_x2 = df["bmi"].unique()
valores_y2 = df["bmi"].value_counts().tolist()
plt.bar(valores_x2, valores_y2)
plt.title("grafico de Índice de masa corporal")
plt.show()


#grafico de cantidad de hijos
valores_x3 = df["children"].unique()
valores_y3 = df["children"].value_counts().tolist()
plt.bar(valores_x3, valores_y3)
plt.title("grafico de cantidad de hijos")
plt.show()

#grafico de costos médicos individuales
valores_x4 = df["charges"].unique()
valores_y4 = df["charges"].value_counts().tolist()
plt.bar(valores_x4, valores_y4)
plt.title("grafico de cargos")
plt.show()
