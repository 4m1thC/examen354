# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 01:10:50 2022

@author: AmiTh
"""

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv(r"C:\Users\AmiTh\Desktop\INF354\examen/insurance.csv")
print(df.describe())

dataset = df.drop("age", axis=1)
label = df["age"].copy()

#1.asignamos el valor medio en los valores nulos
mean_temp = df["age"].mean()
dataframe_op1 = df["age"].fillna(mean_temp)


#2. Pasando los atributos de texto a número
region_cat = df[['region']]

ordinal_encoder = OrdinalEncoder()
region_cat_encoded = ordinal_encoder.fit_transform(region_cat)
print(region_cat_encoded[:10])

#3. Normalización de valores de un atributo
min_max_scaler = MinMaxScaler()
charges_values = df[['charges']]
scaled_values = min_max_scaler.fit(charges_values)
print(min_max_scaler.transform(charges_values)[0:10])