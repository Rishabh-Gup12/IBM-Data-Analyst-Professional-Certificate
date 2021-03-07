# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:29:52 2021

@author: Rishabh
"""
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

filename="Data_converted.csv"
header=["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"] 
df=pd.read_csv(filename)
df.columns=header
df.head()
df.replace("?", np.nan, inplace = True)
print(df.head(5))
missing_data= df.isnull()
print(missing_data)
for i in missing_data.columns.values.tolist():
    print(i)
    print(missing_data[i].value_counts())
    print("")

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
df[["horsepower"]] = df[["horsepower"]].astype("float")

avg_normal_loss= df["normalized-losses"].astype("float").mean(axis=0)
print("Average normal losses: ", avg_normal_loss)
df["normalized-losses"].replace(np.nan, avg_normal_loss, inplace=True)

avg_bore=df["bore"].astype("float").mean(axis=0)
print("The average of bore is: ", avg_bore)
df["bore"].replace(np.nan, avg_bore)


df.dropna(subset=["price"],axis=0)

df.reset_index(drop=True)
print(df.head())


df["highway-mpg"]=235/df["highway-mpg"]
df.rename(columns ={'"highway-mpg"':'highway-L/100km'})
print(df.head())

# Write your code below and press Shift+Enter to execute 
df["height"]=df["height"]/df["height"].max()
print(df.head())

bins=np.linspace(min(df["horsepower"]),max(df["horsepower"]),4)
bins
group_name=["low", "medium","high"]
df["horsepower_bin"]=pd.cut(df["horsepower"],bins,labels=group_name)
print(df[["horsepower","horsepower_bin"]].head(20))

print(df["horsepower"].value_counts())

import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_name, df["horsepower_bin"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

# =============================================================================
# plt.pyplot.hist(df["horsepower"], bins = 3)
# 
# # set x/y labels and plot title
# plt.pyplot.xlabel("horsepower")
# plt.pyplot.ylabel("count")
# plt.pyplot.title("horsepower bins")
# =============================================================================

dummy_variable_1 = pd.get_dummies(df["fuel-type"])
print(dummy_variable_1.head())
