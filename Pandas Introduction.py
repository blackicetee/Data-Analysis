from urllib.request import urlretrieve
import numpy as np
import pandas as pd

#5 columns in iris.csv
#sepal_length  sepal_width
#petal_length  petal_width    species

df = pd.read_csv("D:\dev\python_datasets\iris.csv") 

maxSepalLength = df['sepal_length'].max()
print(maxSepalLength)

#print(df['species'][df['sepal_length'] >= 7.0])
averagePetalLength = df['petal_length'].mean()
print(averagePetalLength)
