import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

df =pd.read_csv("C:\\Users\\armin\\Desktop\\whatevr\\pandn\\data.csv")
df.dropna(subset=["target"],inplace=True)

df["hour"]=pd.to_datetime(df["timestamp"]).dt.hour
df["text_len"]=df["review"].str.len()

x=df.drop("target",axis=1)
y=df["target"]
x_train,x_val,y_train,y_val =train_test_split(x,y,test_size=0.2,random_state=42)