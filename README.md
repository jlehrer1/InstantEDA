# Instant EDA
Instantly generate common exploratory data plots.

To guarantee you are using the correct packages, run `pip install -r requirements.txt`.

Usage:
```python3
plotter = quickplotter.QuickPlotter(df: pd.DataFrame) #creates a QuickPlotter object with the given DataFrame
```

Attributes:
```python3
self.plotlist 
>>> {
            'common': ['num_nan', 'percent_nan', 'correlation'],
            'pairwise': [],
            'variance': []
        }
```

Ideas so far:

Number of NaN's in each column  

Percent of Nan's in each column. 

Correlation matrix. 

distribution matrix for all features?  

univariate distribution of each feature (bar + kde for numeric,  just bar for categorical)

time series distribution of numeric features if we can infer a timestamp column (look at: [this](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.infer_objects.html))

pairplot of all  numerical everything if number of columns is manageable

