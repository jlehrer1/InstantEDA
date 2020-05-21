import pandas as pd 

from visualization import visualization
from cleaning import clean

class QuickPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.df_clean = clean.clean(df) #add ability to change params later
        self.plotlist = {
            'common': ['num_nan', 'percent_nan', 'correlation'],
            'pairwise': [],
            'variance': []
        }

    def _get_plots(self):
        df1 = visualization.num_nan_plot(self.df)
        df2 = visualization.percent_nan_plot(self.df)
        df3 = visualization.correlation_plot(self.df_clean)

        return {
            'num_nan': df1,
            'percent_nan': df2,
            'correlation': df3,
        }

    def _plot(self, plots: list):
        all_plots = self._get_plots()
        for plot in plots:
            all_plots[plot].show()

    def common(self, subset: list = None, diff: list = None):
        """Plots common EDA plots.
            Parameters:
                subset: subset of common plots to show
                diff: plot all common plots except those in diff, i.e. {all plots}\\{diff}
            """
        if subset is None and diff is None:
            # plot is called without subset/diff specified, just plot all
            self._plot(self.plotlist['common'])
        elif subset is not None and set(subset).issubset(set(self.plotlist)):
            self._plot(subset)
        elif diff is not None and set(diff).issubset(set(self.plotlist)):
            self._plot(list(set(self.plotlist) - set(diff)))
        else:
            raise ValueError("subset or diff contains improper values. Check plotlist attribute for appropriate values")
    
    def pairwise(self, subset: list = None, diff: list = None):
        """Plots each feature X_i against X_j
            Parameters
            ------
            subset: subset of features to plot
            diff: plot all features except those in diff
        """
        pass 

    def variance(self, subset: list = None, diff: list = None):
        """"""
        pass