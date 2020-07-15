# from my_lambdata.ds_utilities import enlarge
import pandas as pd
from my_lambdata.ds_utilities import Others_Class

# y = 5
# print(y, enlarge(y))

url = "https://raw.githubusercontent.com/DrewRust/Kepler_Planet_data/master/SoccerMatches.csv"
soccer_df = pd.read_csv(url)

mls_df = Others_Class(soccer_df, 15, soccer_df['date'])

""" Calling Others_Class object to enlarge our number """
enlarged_num = mls_df.enlarge()
print(enlarged_num)