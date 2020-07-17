import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_wine
# from pdb import set_trace as breakpoint
# from IPython.display import display

def enlarge(n):
    ''' 
    This function will multiple the input by 100 
    '''
    return n * 100

class Test_Split_Class:

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
    def __init__(self, df):
        self.df = df

    def delete_col(self, col_to_del):
        new_df = self.df
        final_df = new_df.drop(columns=[col_to_del])
        return final_df

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

    def convert_to_dates(self, dateColumn):
        new_df = self.df
        new_df['date_dtype'] = pd.to_datetime(dateColumn)
        return new_df

    def enlarge(self, n):
        """ Will multiply the input by 100 """
        return n * 100


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

    """ Creating an object of the Others_Class """
    first_obj = Others_Class(soccer_df)
    first_instance = first_obj.enlarge(5)
    second_instance = first_obj.convert_to_dates(soccer_df['date'])
    third_instance = first_obj.delete_col('league_id')
    fourth_instance = first_obj.find_nulls_func()
    fifth_instance = first_obj.drop_nulls_cols()

