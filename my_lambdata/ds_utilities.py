import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint


class Test_Split_Class:

    """
    Don't really need the dataset here.
    This will load in google colab
    """

    def __init__(self, df, X, y):
        self.df = df
        self.X = X
        self.y = y

    def my_train_val_test_split(self):
        train_1, test = train_test_split(
            self.df, test_size=0.15, random_state=42)
        train, val = train_test_split(
            train_1, test_size=0.15, random_state=42)
        return train, val, test

    def example_train_val_test_split(
        self, train_size=0.7, val_size=0.1, test_size=0.2,
            random_state=None, shuffle=True):
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state,
            shuffle=shuffle)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size/(train_size+val_size),
            random_state=random_state, shuffle=shuffle)
        return X_train, X_val, X_test, y_train, y_val, y_test


class Others_Class:
    def __init__(self, df, n, dateColumn):
        self.df = df
        self.n = n
        self.dateColumn = dateColumn

    def find_nulls_func(self):
        my_list = []
        new_df = self.df
        my_list = new_df.isnull().sum().tolist()
        new_series = pd.Series(my_list, index=new_df.columns)
        return new_series

    def drop_nulls_cols(self):
        new_df = self.df
        final_df = new_df.dropna(axis=0)
        return final_df

    def convert_to_dates(self):
        new_df = self.df
        new_df['date_dtype'] = pd.to_datetime(self.dateColumn)
        return new_df

    def enlarge(self):
        """ Will multiply the input by 100 """
        return self.n * 100


if __name__ == '__main__':

    """
    This is the dataset used and it works here better.
    Originally I had it above defined in the class.
    That is not the best place for it otherwise it gets repeatedly called.
    """
    url = "https://raw.githubusercontent.com/DrewRust/Kepler_Planet_data/master/SoccerMatches.csv"
    soccer_df = pd.read_csv(url)

    """ This would load a built in wine dataset """
    # raw_data = load_wine()
    # df = pd.DataFrame(data=raw_data['data'],
    # columns=raw_data['feature_names'])
    # df['target'] = raw_data['target']

    """ This is for the vscode editor """
    # breakpoint allows for debugging and data exploration
    # breakpoint()
    # print(df.shape)

    """ Creating an object of the Test_Split_Class """
    dataframe1 = Test_Split_Class(
        soccer_df, soccer_df[['proj_score1', 'spi1']], soccer_df['score1'])

    """ Creating an object of the Others_Class """
    mls_df = Others_Class(soccer_df, 10)
