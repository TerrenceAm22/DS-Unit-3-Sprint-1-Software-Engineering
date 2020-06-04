from sklearn.model_selection import train_test_split
import pandas

from pandas import DataFrame
from pandas import Series

df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
df2 = DataFrame({"abbrev": ["GA", "MN", "VA", "LA", "MA"]})


#def train_val_split(df):
    #train = train_test_split(df)
    #return train



#print("The split", train_val_split(df))



def convert_list_add_to_dateframe(df):
    """
    It supposed to turn list into a pandas series

    Atleast I hope so
    """

    df = Series([df])
    df3 = df.append(df2)
    

    return df3

    
print("Adding a series into dataframe", convert_list_add_to_dateframe(df2))
#print(df3)