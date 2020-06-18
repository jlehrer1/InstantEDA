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
        # Checks for subset/diff
        # ------------------------------------------
        if not (set(subset).issubset(self.plotlist) and set(diff).issubset(self.plotlist)):
            raise ValueError(
                "subset or diff contains improper values. Check plotlist attribute for appropriate values")
        if subset is not None and diff is not None:
            raise ValueError(
                "subset and diff cannot both be used."
            )

        # Checks for subset_columns/subset_diff
        # ------------------------------------------
        if not (set(subset_columns).issubset(self.plotlist) and set(diff_columns).issubset(self.plotlist)):
            raise ValueError(
                "subset_columns or subset_diff contain improper values. Check that they only contain valid column names."
            )
        if subset_columns is not None and diff_columns is not None:
            raise ValueError(
                "subset_columns and subset_diff cannot both be used"
            )

    def common(self, subset: list = None, diff: list = None, subset_columns: list = None, diff_columns: list = None):
        """Plots common EDA plots.
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
        elif diff is not None:
            self._plot(list(set(self.plotlist) - set(diff)))
        else:
            raise ValueError(
                "subset or diff contains improper values. Check plotlist attribute for appropriate values"
                )

    def pairwise(self, subset: list = None, diff: list = None, subset_columns: list = None, diff_columns: list = None):
        """Plots each feature X_i against X_j
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
        elif diff is not None and set(diff).issubset(set(self.df.columns)):
            visualization.pairwise_plot(self.df_clean, list(
                set(self.df_clean.columns) - set(diff))).show()
        else:
            raise ValueError(
                "feature_subset or feature_diff contain values that are not column names")

    # def variance(self, subset: list = None, diff: list = None):
    #     """Plots pairwise variance"""
    #     self._validity_check(subset, diff)
        
