import pandas as pd 
import numpy as np 
from visualization import visualization
from cleaning import clean

class QuickPlotter:
    def __init__(self, df, y=None):
        self.y = y
        self.df = df 


