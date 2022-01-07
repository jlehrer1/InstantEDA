# test_quickplotter.py

# Needed for testing
import pandas as pd
import numpy as np
import quickplotter 

# Define dummy DataFrame for testing
d = {
    'col1': [1, 2], 
    'col2': [3, 4], 
    'col3': [np.nan, 6],
    'col4': [7,8],
    'col5':[9, np.nan],
}

df = pd.DataFrame(data=d)

qp = quickplotter.QuickPlotter(df)

def test_class_is_creatable():
    qp = quickplotter.QuickPlotter(df)

def test_class_common_plots_show():
    qp.common()

def test_class_pairwise_plots_show():
    qp.pairwise()

def test_class_distribution_plots_show():
    qp.distribution()

def test_class_subset_passes():
    # only for .common() now
    qp.common(['num_nan', 'percent_nan'])

def test_class_diff_passes():
    # only for .common() now
    qp = quickplotter.QuickPlotter(df)

def test_class_subset_col_passes():
    pass

def test_class_diff_col_passes():
    pass




