import pandas as pd
import numpy as np
import warnings
from sklearn.impute import KNNImputer, SimpleImputer

# HELPER FUNCTIONS TO CLEAN DATA

def _is_likely_categorical(df_col: pd.Series) -> bool:
    return df_col.unique() / df_col.count() < 0.05

def _impute_data(df: pd.DataFrame) -> pd.DataFrame:
    """Imputes missing numerical or categorical values in DataFrame
        Usage:
        -------
        dataframe_no_nan = impute_data(dataframe_with_nan)
    """
    imputer = KNNImputer()
    for column in df.columns:
        if df[column].isna().sum() != 0:
            df[column] = imputer.fit_transform(df[[column]])
    return df

def _drop_bad_dtypes(df: pd.DataFrame, categorical=False) -> pd.DataFrame:
    """"""
    df = df.infer_objects()
    for col in df.columns:
        if _is_likely_categorical(df[col]) and not categorical:
            warnings.warn("Column {} is likely categorical, creating dummies... run with categorical=False to disable".format(col))
            df = pd.get_dummies(data=df, columns=[col])
        elif not np.issubdtype(df[col].dtype, np.number):
            warnings.warn("Column {} dtype is string or uninterpretable... ignoring and continuing".format(col))
            df.drop(col, axis=1, inplace=True)
        else:
            continue
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Returns cleaned DataFrame with ONLY numeric values (can be categorical)
        Usage:
        ------
        prepared_data = clean(raw_data)
    """
    pass
