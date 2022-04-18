#Dealing with Categorical data
import pandas as pd
import numpy as np
import copy
df_catdata=pd.read_csv("catdata2.csv")
print(df_catdata.info())
cat_df_catdata=df_catdata.select_dtypes(include=['object']).copy()
print(cat_df_catdata['RollNo'])
#print(cat_df_catdata.dtypes)

# Label Encoding
cat_df_catdata_lc=cat_df_catdata.copy()
cat_df_catdata_lc['RollNo']=cat_df_catdata_lc['RollNo'].astype('category')
print(cat_df_catdata_lc.dtypes)
cat_df_catdata_lc['Rollno']=cat_df_catdata_lc['RollNo'].cat.code
print(cat_df_catdata_lc)
