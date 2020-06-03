from sklearn.model_selection import train_test_split

import pandas

from pandas import DataFrame


def add_state_names_column(my_df):
    """
    Add a column of corresponding state names to a dataframe.

    Params (my_df) a DataFrame with a column called "abbrev" that has state abbrevations


    Return a copy of the orginal dataframe, but with an extra column
    """
    
    return my_df


if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    #print(df.head())

    add_state_names_column(df)
    #print(df.head())

    train, test = train_test_split(df, random_state=42)
    print(train)
    print(test)
    
    

    

