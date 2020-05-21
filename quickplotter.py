import pandas as pd 

from visualization import visualization
from cleaning import clean

class QuickPlotter:
    def __init__(self, df: pd.DataFrame, subset: list = None, diff: list = None):
        if subset is not None and diff is not None:
            print("add error here")

        self.df = df
        self.clean_df = clean.clean(df) #add ability to change params later
        self.subset = subset
        self.diff = diff

    def plot(self):
        if self.subset is not None:
            pass 
        if self.diff is not None:
            pass
        f1 = visualization.num_nan_plot(self.df).show()
        f2 = visualization.percent_nan_plot(self.df).show()
        f3 = visualization.generate_correlation_plot(self.df).show()

        plots = {
            'num_nan': f1, 
            'percent_nan': f2, 
            'corr': f3
        }