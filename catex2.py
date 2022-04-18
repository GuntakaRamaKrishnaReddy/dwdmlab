#Dealing the categorial data using sklearn
import pandas as pd
import numpy as np
import copy
from sklearn.preprocessing import LabelEncoder
df_flights=pd.read_csv("flights.csv")
#print(df_flights[:30]['Uniquecarrier']
#Step1: Create an object of LabelEncoder class
lbobj=LabelEncoder()

#Step2: Transform the column uisng the encoder object
print(df_flights.info())
cat_sklearn_flights=df_flights.copy()
cat_sklearn_flights['UniqueCarrier']=lbobj.fit_transform(df_flights['UniqueCarrier'])
print(cat_sklearn_flights['Uniquecarrier'])
