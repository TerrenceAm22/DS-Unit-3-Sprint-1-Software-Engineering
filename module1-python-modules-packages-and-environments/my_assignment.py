from sklearn.model_selection import train_test_split

import pandas as pd

from pandas import DataFrame
from pandas import crosstab



def split(df):
    """
    Param n is a an object

    Function will split dates into multiple columns.
    """

    return pd.set_option('display.max_columns', None)
if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    df2 = DataFrame({"abbrev": ["GA", "MN", "VA", "LA", "MA"]})
   # print(df.head())

    #add_state_names_column(df)
    #print(df.head())

print(df)
y = int(input("Displaying max rows"))
print(y, split(df))

   #train, test = train_test_split(df, random_state=42)
    #print(train)
    #print(test)
    

    

    

