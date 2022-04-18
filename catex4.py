import pandas as pd
import numpy as np
import copy
#from sklearn.preprocessing import LabelEncoder
#one-Hot Encoding
df_flights=pd.read_csv("flights.csv")
cat_df_flights
cat_onehot=df_flights.copy()
lb_obj=LabelBinarizer()
lb_results=lb.obj.fit_transform(df_lights['UniqueCarrier'])
print(lb_results)

lb_results_df=pd.DataFrame(lb_results,colums=lb_obj

