# Instant EDA
Instantly generate common exploratory data plots without having to worry about cleaning your data.

The code is hosted on PyPi, the Python Package Index
[here](https://pypi.org/project/quickplotter/1.0/)

It can be installed by running 
```shell
pip install quickplotter==1.0
```

To setup the proper development environment, run 
```
conda env create -f environment.yml
conda update pip
```

Note: To find the most updated documentation, visit the Github [repo](https://github.com/jlehrer1/InstantEDA).

Description: The `quickplotter` module provided here is meant to provide common exploratory data plots without having to worry about cleaning your DataFrame or preanalyzing your data. Additionally, these plots can be exported to `.{png, jpeg}` for use in reports and papers. 

## 1. Usage:
```python3
plotter = quickplotter.QuickPlotter(df: pd.DataFrame) #creates a QuickPlotter object with the given DataFrame

plotter.common(subset=['correlation', 'percent_nan']) #plots correlation between features, and percent nan in each column

plotter.distribution(column_subset=df.columns[0:4]) #plots distributions for the first four columns in the DataFrame

plotter.common(column_subset=['body_mass_index', 'blood_type']) #plots common plots for the given columns
```

## 2. Fundamentals

If the number of `NaN` values in the DataFrame is `<= 5%` of the total values, the NaN rows will be dropped and the plots will be generated without them. **Remember, this is meant to be a quick and dirty tool for exploration, and not for being delicate with each data entry.**

### subset & diff lists
The quickplot module works mainly with two specifications, `subset` and `diff`. 

For any `subset`-like list, the items in the list will be used. For any `diff`-like list, all items *except* those in the list will be used. 

The options are as follow:
- `subset`: Use only the plots specified in the list
- `diff`: Use all plots *except* those specified in the list
- `subset_columns`: Use all columns specified in the list. Can either be `df.columns` slicing or by name
- `diff_columns`: Use all columns *except* those specified in the list. Can either be `df.columns` slicing or by name. 

## 3. Contributing

If you have read this far I hope you've found this tool useful. I am always looking to learn more and develop as a collaborative programmer, so if you have any ideas or contributions, feel free to write a feature or pull request. 





