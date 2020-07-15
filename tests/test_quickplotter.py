# test_quickplotter.py

# Needed for testing
import pandas as pd
import numpy as np

# Define dummy DataFrame 
d = {'col1': [1, 2], 'col2': [3, 4], 'col3': [np.nan, 6]}
df = pd.DataFrame(data=d)

def is_importable():
    assert import quickplotter

def class_is_creatable():
    assert qp = quickplotter.QuickPlotter(df)

def class_common_plots_show():
    pass

def class_subset_passes():
    pass

def class_diff_passes():
    pass

def class_subset_col_passes():
    pass

def class_diff_col_passes():
    pass




