import pandas as pd 

from visualization import visualization
from cleaning import clean

class QuickPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.df_clean = clean.clean(df) #add ability to change params later
        self.plotlist = ['num_nan', 'percent_nan', 'correlation']

    def _get_plotlist(self):
        df1 = visualization.num_nan_plot(self.df)
        df2 = visualization.percent_nan_plot(self.df)
        df3 = visualization.generate_correlation_plot(self.df_clean)

        return {
            'num_nan': df1,
            'percent_nan': df2,
            'correlation': df3,
        }

    def plot_all(self):
        plots = self._get_plotlist()
        for plot in plots:
            plots[plot].show()
    
    def plot(self, subset: list = None, diff: list = None):
        to_plot = []
        if subset is None and diff is None:
            # plot is called without subset/diff specified, just plot all
            self.plot_all()
        elif subset is not None and set(subset).issubset(set(self.plotlist)):
            pass
        elif diff is not None and set(diff).issubset(set(self.plotlist)):
            pass
        else:
            # 
            raise ValueError("subset or diff contains improper values")