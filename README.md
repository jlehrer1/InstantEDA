# Instant EDA (Work in progress!)
Instantly generate common exploratory data plots without having to worry about cleaning your data.

The code is hosted on PyPi, the Python Package Index
[here](https://pypi.org/project/quickplotter/0.1/#modal-close).

It can be installed by running 
```shell
pip install quickplotter==0.1
```

To setup the proper development environment, run `conda env create -f environment.yml`

Usage:
```python3
plotter = quickplotter.QuickPlotter(df: pd.DataFrame) #creates a QuickPlotter object with the given DataFrame

plotter.common(subset=['correlation', 'percent_nan']) #plots correlation between features, and percent nan in each column

plotter.distribution(column_subset=df.columns[0:4]) #plots distributions for the first four columns in the DataFrame

```

The quickplot module works mainly with two specifications, `subset` and `diff`. 

For any `subset`-like list, the items in the list will be used. For any `diff`-like list, all items *except* those in the list will be used. 

To specifiy column `subset`'s or `diff`'s, call each plot individually or call `.common` with the `column_subset` or `column_diff` attributes (need to be added as of 6/18/20).

Ideas so far:

Number of NaN's in each column (done)

Percent of Nan's in each column (done)

Correlation matrix (done)

distribution matrix for all features (done)

univariate distribution of each feature (bar + kde for numeric,  just bar for categorical)

time series distribution of numeric features if we can infer a timestamp column (look at: [this](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.infer_objects.html))

pairplot of all  numerical everything if number of columns is manageable (done)

