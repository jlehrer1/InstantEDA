# Instant EDA (Work in progress!)
Instantly generate common exploratory data plots without having to worry about cleaning your data.

The code is hosted on PyPi, the Python Package Index
[here](https://pypi.org/project/quickplotter/0.3/#modal-close).

It can be installed by running 
```shell
pip install quickplotter==0.3
```

To setup the proper development environment, run `conda env create -f environment.yml`

Note: To find the most updated documentation, visit the Github [repo](https://github.com/jlehrer1/InstantEDA).

Usage:
```python3
plotter = quickplotter.QuickPlotter(df: pd.DataFrame) #creates a QuickPlotter object with the given DataFrame

plotter.common(subset=['correlation', 'percent_nan']) #plots correlation between features, and percent nan in each column

plotter.distribution(column_subset=df.columns[0:4]) #plots distributions for the first four columns in the DataFrame

```

The quickplot module works mainly with two specifications, `subset` and `diff`. 

For any `subset`-like list, the items in the list will be used. For any `diff`-like list, all items *except* those in the list will be used. 

To specifiy column `subset`'s or `diff`'s, call each plot individually or call `.common` with the `column_subset` or `column_diff` attributes (need to be added as of 6/18/20).
