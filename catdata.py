#Dealing with Categorical data
import pandas as pd
import numpy as np
import copy
df_flights=pd.read_csv("flights.csv")
print(df_flights.info())
cat_df_flights=df_flights.select_dtypes(include=['object']).copy()
print(cat_df_flights['UniqueCarrier'])
#print(cat_df_flights.dtypes)

# Label Encoding
cat_df_flights_lc=cat_df_flights.copy()
cat-df_flights_lc['UniqueCarrier']=cat_df_flights_lc['Uniquecarrier'].astype('category')
print(cat_df_flights_lc.dtypes)
cat_df_flights_lc['UniqueCarrier']=cat_df_flights_lc['UniqueCarrier'].cat.code
print(cat_df_flights_lc)
