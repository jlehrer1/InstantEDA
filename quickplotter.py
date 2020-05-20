import pandas as pd 
from visualization import visualization
from cleaning import clean

class QuickPlotter:
    def __init__(self, df: pd.DataFrame, y: str = None, subset: list = None, diff : list = None):
        self.y = y
        self.df = df 
        self.subset = subset
        self.diff = diff 

    def plot(self):
        f1 = visualization.num_nan_plot(self.df).show()
        f2 = visualization.percent_nan_plot(self.df).show()
        f3 = visualization.generate_correlation_plot(self.df).show()

        plots = {'num_nan': f1, 'percent_nan': f2, 'corr': f3}

        
        




