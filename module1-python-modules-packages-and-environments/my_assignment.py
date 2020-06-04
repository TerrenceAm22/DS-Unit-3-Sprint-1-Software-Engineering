from sklearn.model_selection import train_test_split

import pandas as pd

from pandas import DataFrame
from pandas import crosstab



#def split(df):
    #"""
    #Param n is a an object

    #Function will split dates into multiple columns.
    #"""

    #return pd.set_option('display.max_columns', None)
#if __name__ == "__main__":
   # df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    #df2 = DataFrame({"abbrev": ["GA", "MN", "VA", "LA", "MA"]})


#def train_test_split(df): 
    #from sklearn.model_selection import train_test_split
    #train = train_test_split(df)
    #train, val = train_test_split(train)
    #return df


if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    df2 = DataFrame({"abbrev": ["GA", "MN", "VA", "LA", "MA"]})




    

    
def traintestsplit():

    """
    Turning a list into a series
    """
    train = train_test_split()

    print(train_test_split(train.head()))

    


    #print("Train Test Split", train_test_split(df))
    #print(train)
    

