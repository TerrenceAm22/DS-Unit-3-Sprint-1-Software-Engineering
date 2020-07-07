
import pandas
import sklearn
from sklearn.model_selection import train_test_split

from pandas import DataFrame



def __init__(self, name):
    self.name = name
    return
        
def add_state_names_column(my_df):
    """
    Add a column of corresponding state names to a dataframe.
    Params (my_df) a DataFrame with a column called "abbrev" that has state abbrevations
    Return a copy of the orginal dataframe, but with an extra column
    """
    return my_df
def split_data(my_df):
    train_test_split(my_df, test_size=.80)
    return my_df
    
def generate_data(self):
    my_df = DataFrame.append(df,tj, ignore_index=True)
    return my_df

    
    


    

     

if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    tj = DataFrame({"Added": ["GA","MS", "NY", "MO"]})
    data = (10, 20, 50, 80, 100, 110, 100)
    #print(df.head())
    print(split_data(data))
    print(generate_data(df))


   
   

   
  





