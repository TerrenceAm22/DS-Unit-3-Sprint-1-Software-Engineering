import unittest
from random import randint
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split






from functions import Helper_Functions

class TestingCase(unittest.TestCase):
    """
    Function to test if train/test/split function
    work will
    """
    def test_train(self):
        """ Function will split data into
        train and test sets for machine learning
        """
        df = pd.DataFrame({10, 20, 40, 60, 70, 80, 80, 100, 110})
        train_test_split(df, test_size=.5)
        print(df.shape)
        return
    def test_add(self):
        df = pd.DataFrame({10, 20, 40, 60, 70, 80, 80, 100, 110, 120})
        names = pd.DataFrame({'Mario', 'Sonic', 'Sly', 'Duke', 'Tails', 'Luigi', 'CaptainMak', 'Crash', 'Knuckles', 'Tupac'})
        result = df.append(names, sort=False)
        return df




if __name__ == '__main__':
    unittest.main()