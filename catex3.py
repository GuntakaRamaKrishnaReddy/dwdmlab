import pandas as pd
import numpy as np
import copy
#from sklearn.preprocessing import LabelEncoder
#one-Hot Encoding
df_flights=pd.read_csv("flights.csv")
cat_onehot=df_flights.copy()

cat_onehot=pd.get_dummies(cat_onehot,coloums=['Uniquecarrier'],prefix=['Uniquecarrier'])
print(cat_onehot)





