import pandas as pd
import numpy as np
import warnings
from sklearn.impute import KNNImputer, SimpleImputer

def _is_likely_categorical(df_col: pd.Series) -> bool:
    return df_col.unique() / df_col.count() < 0.05

def impute_data(df: pd.DataFrame) -> pd.DataFrame:
    """Imputes missing numerical or categorical values with KNN Imputer"""
    imputer = KNNImputer()
    for column in df.columns:
        if df[column].isna().sum() != 0:
            df[column] = imputer.fit_transform(df[[column]])
    return df

def drop_bad_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.infer_objects()
    for col in df.columns:
        if _is_likely_categorical(df[col]):
            warnings.warn("Column {} is likely categorical, creating dummies... run with categorical=False to disable".format(col))
        elif not np.issubdtype(df[col].dtype, np.number):
            warnings.warn("Column {} dtype is string or uninterpretable... ignoring and continuing".format(col))
            df.drop(col, axis=1, inplace=True)
    return df

