# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:55:53 2022

@author: AmiTh
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\AmiTh\Desktop\INF354\examen/insurance.csv")

df = pd.get_dummies(data=df, drop_first=True)

explicativas = df.drop(columns="age")
objetivo = df.age

model = DecisionTreeClassifier(max_depth=3)

model.fit(X=explicativas, y=objetivo)

plt.figure(figsize=(14, 8))
plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=3);

plt.show()

