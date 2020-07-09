import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def my_train_val_test_split(df):
  train_1, test = train_test_split(df, test_size=0.15, random_state=42)
  train, val = train_test_split(train_1, test_size=0.15, random_state=42)
  return train, val, test

def find_nulls_func(df):
  my_list = []
  my_list = df.isnull().sum().tolist()
  new_series = pd.Series(my_list, index = df.columns) 
  return new_series


def convert_to_dates(df):
  df['datetime'] = pd.to_datetime(df["date"])
  return df

def enlarge(n):
    """ Will multiply the input by 100 """
    return n * 100

if __name__ == '__main__': 
    y = int(input("Choose a number: "))
    print(y, enlarge(y))

