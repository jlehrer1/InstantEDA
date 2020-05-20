import warnings

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer, SimpleImputer

# HELPER FUNCTIONS TO CLEAN DATA

def _is_likely_categorical(df_col: pd.Series) -> bool:
    return df_col.nunique() / df_col.count() < 0.05

def _is_numeric(df_col: pd.Series) -> bool:
    return np.issubdtype(df_col.dtype, np.number) 

def _impute_data(df: pd.DataFrame, categorical: bool = True) -> pd.DataFrame:
    """Imputes missing numerical or categorical values if the percentage of rows containing NaN's is > 5%.
    Else, returns a dataframe without those rows.
        Usage:
        -------
        dataframe_no_nan = impute_data(dataframe_with_nan)
    """
    df = df.infer_objects()
    print("DTYPES ARE", df.dtypes)
    if df.isna().sum().sum() / df.shape[0] <= 0.05:
        return df.dropna()
    
    knnimp = KNNImputer() # for numeric 
    simpimp = SimpleImputer(strategy='most_frequent') # for categorical

    for column in df.columns:
        if _is_likely_categorical(df[column]) and categorical:
            warnings.warn("Column {} is likely categorical, creating dummies... run with categorical=False to disable".format(column))
            df[column] = simpimp.fit_transform(df[[column]])
    for column in df.columns:
        if _is_numeric(df[column]):
            df[column] = knnimp.fit_transform(df[[column]])
        else:
            df[column].fillna(value='')
    return df

# def _drop_bad_dtypes(df: pd.DataFrame, categorical: bool = True) -> pd.DataFrame:
#     """Attempts to infer a type for each column. If this isn't possible, then drops the column.
#     Also generates categorical variables when possible."""
    
#     df = df.infer_objects()
#     for col in df.columns:
#         if _is_likely_categorical(df[col]) and not categorical:
#             warnings.warn("Column {} is likely categorical, creating dummies... run with categorical=False to disable".format(col))
#             df = pd.get_dummies(data=df, columns=[col])
#         elif not np.issubdtype(df[col].dtype, np.number):
#             warnings.warn("Column {} dtype is string or uninterpretable... ignoring and continuing".format(col))
#             df.drop(col, axis=1, inplace=True)
#         else:
#             continue
#     return df


def clean(df: pd.DataFrame, categorical: bool = True) -> pd.DataFrame:
    """Returns cleaned DataFrame with ONLY numeric values (can be categorical)
        Usage:
        ------
        prepared_data = clean(raw_data)
    """
    return _impute_data(df, categorical)
