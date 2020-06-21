# Instant EDA 
## Work in progress :)
Instantly generate common exploratory data plots without having to worry about cleaning your data.

To guarantee you are using the correct packages, run `pip install -r requirements.txt`.

Usage:
```python3
plotter = quickplotter.QuickPlotter(df: pd.DataFrame) #creates a QuickPlotter object with the given DataFrame

plotter.common(subset=['correlation', 'percent_nan']) #plots correlation between features, and percent nan in each column
```

The quickplot module works mainly with two specifications, `subset` and `diff`. 

For any `subset`-like list, the items in the list will be used. For any `diff`-like list, all items *except* those in the list will be used. 

To specifiy column `subset`'s or `diff`'s, call each plot individually or call `.common` with the `column_subset` or `column_diff` attributes (need to be added as of 6/18/20).

Ideas so far:

Number of NaN's in each column  

Percent of Nan's in each column. 

Correlation matrix. 

distribution matrix for all features?  

univariate distribution of each feature (bar + kde for numeric,  just bar for categorical)

time series distribution of numeric features if we can infer a timestamp column (look at: [this](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.infer_objects.html))

pairplot of all  numerical everything if number of columns is manageable

