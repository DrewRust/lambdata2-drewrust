import unittest
import pandas as pd
import numpy as np
from my_lambdata.ds_utilities import enlarge, Others_Class


class TestDsUtilities(unittest.TestCase):

    def test_enlarge(self):
        # first assert will fail
        # self.assertEqual(enlarge(3), 350)
        self.assertEqual(enlarge(3), 300)


    # def test_enlarge(self):
    #     url = "https://raw.githubusercontent.com/DrewRust/Kepler_Planet_data/master/SoccerMatches.csv"
    #     soccer_df = pd.read_csv(url)
    #     first_obj = Others_Class(soccer_df)
    #     bigger_num = first_obj.enlarge(3)
    #     self.assertEqual(bigger_num, 300)

    # def test_enlarge(self):

    #     """ Created Data set of soccer stats. """
    #     data ={'team1':  ['DC_United', 'FC_Cincinnati','Columbus_Crew'],
    #         'proj_score1':  [3, 2, 4],
    #         'spi1': [7, 5, 9],
    #         'score1': [4, 3, 3],
    #         'date': [2020-7-13, 2020-7-16, 2020-7-17],
    #         'col_not_needed': [np.nan, np.nan, np.nan]}

    #     created_df = pd.DataFrame (data, columns= ['team1','proj_score1', 'spi1', 'score1', 'date', 'col_not_needed'])
    #     first_obj = Others_Class(created_df)
    #     bigger_num = first_obj.enlarge(5)
    #     self.assertEqual(bigger_num, 500)

    def test_delete_col(self):

        """ Created Data set of soccer stats. """
        data ={'team1':  ['DC_United', 'FC_Cincinnati','Columbus_Crew'],
            'proj_score1':  [3, 2, 4],
            'spi1': [7, 5, 9],
            'score1': [4, 3, 3],
            'date': [2020-7-13, 2020-7-16, 2020-7-17],
            'col_not_needed': [np.nan, np.nan, np.nan]}

        created_df = pd.DataFrame (data, columns= ['team1','proj_score1', 'spi1', 'score1', 'date', 'col_not_needed'])
        

        current_shape = created_df.shape[1]
        # expected_shape = current_shape - 1
        expected_shape = current_shape - 2

        first_obj = Others_Class(created_df)
        one_less_col_df = first_obj.delete_col('col_not_needed')

        # # Create Others_Class object
        # one_less_col = Others_Class(created_df, 5, created_df['date'], 'col_not_needed')
        # one_less_col_df = one_less_col.delete_col()

        self.assertEqual(expected_shape, one_less_col_df.shape[1])


if __name__ == '__main__':
    # url = "https://raw.githubusercontent.com/DrewRust/Kepler_Planet_data/master/SoccerMatches.csv"
    # soccer_df = pd.read_csv(url)
    # first_obj = Others_Class(soccer_df)
    unittest.main()