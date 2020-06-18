import pandas as pd

from visualization import visualization
from cleaning import clean

class QuickPlotter:
    def __init__(self, df: pd.DataFrame, categorical = True, categorical_subset = None):
        self.df = df
        self.df_clean = clean.clean(df, categorical=categorical, categorical_subset=categorical_subset)
        self.plotlist = {
            'common': ['num_nan', 'percent_nan', 'correlation'],
            'pairwise': ['pairwise'],
            'distribution': ['dist']
        }

    #--------------------------------------------------
    # Wrapper functions for the visualization module
    #--------------------------------------------------

    def _plot(self, plots: list):
        df1 = visualization.num_nan_plot(self.df)
        df2 = visualization.percent_nan_plot(self.df)
        df3 = visualization.correlation_plot(self.df_clean)

        all_plots = {
            'num_nan': df1,
            'percent_nan': df2,
            'correlation': df3,
        }

        for plot in plots:
            all_plots[plot].show()

    def _validity_check(self, subset, diff, subset_columns, diff_columns):
        """
        Checks each parameter in the QuickPlotter object's methods. 
        It is a private function which will not be of much use outside of the specified functions.
        """
        # Checks for subset/diff
        # ------------------------------------------
        plotlist = self.plotlist
        if subset is not None and diff is not None:
            raise ValueError(
                "subset and diff cannot both be used."
            )
        if subset is not None and not set(subset).issubset(plotlist):
            raise ValueError(
                "subset contains improper values. Check the plotlist attribute for appropriate ones."    
            )
        if diff is not None and not set(diff).issubset(plotlist):
            raise ValueError(
                "diff contains improper values. Check the plotlist attribute for appropriate ones."
            )

        # Checks for subset_columns/subset_diff
        # ------------------------------------------
        col_list = list(self.df.columns)
        if subset_columns is not None and diff_columns is not None:
            raise ValueError(
                "subset_columns and subset_diff cannot both be used"
            )
        if subset_columns is not None and not set(subset_columns).issubset(col_list):
            raise ValueError(
                "subset_columns contains improper values. Check that it only contains valid column names"
            )
        if diff_columns is not None and not set(diff_columns).issubset(col_list):
            raise ValueError(
                "diff_columns contains improper values. Check that it only contains valid column names."
            )

    def common(self, subset: list = None, diff: list = None, subset_columns: list = None, diff_columns: list = None):
        """
        Plots common EDA plots.
            Parameters:
            ----------
                subset: subset of common plots to show
                diff: plot all common plots except those in diff, i.e. {all plots}\\{diff}
        """
        self._validity_check(subset, diff, subset_columns, diff_columns)

        if subset is None and diff is None:
            # plot is called without subset/diff specified, just plot all
            self._plot(self.plotlist['common'])
        elif subset is not None:
            self._plot(subset)
        else:
            self._plot(list(set(self.plotlist) - set(diff)))

    def pairwise(self, subset: list = None, diff: list = None, subset_columns: list = None, diff_columns: list = None):
        """
        Plots each feature X_i against X_j, i=1,...,length(X.columns)
            Parameters
            ---------
                subset: subset of features to plot
                diff: plot all features except those in diff
        """
        self._validity_check(subset, diff, subset_columns, diff_columns)

        if subset is None and diff is None:
            visualization.pairwise_plot(
                self.df_clean, self.df_clean.columns).show()
        elif subset is not None:
            visualization.pairwise_plot(self.df_clean, subset).show()
        else:
            visualization.pairwise_plot(self.df_clean, list(
                set(self.df_clean.columns) - set(diff))).show()


    # def variance(self, subset: list = None, diff: list = None, subset_columns: list = None, diff_columns: list = None):
    #     """Plots pairwise variance"""
    #     self._validity_check(subset, diff)
        
