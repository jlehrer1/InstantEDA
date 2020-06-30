import warnings

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn_pandas import CategoricalImputer


def is_likely_categorical(df_col: pd.Series) -> bool:
    """Heuristic method to check if column is likely categorical. If the ratio between the number of unique and
    total number of rows is small (< 0.05) then the column might be categorical and can be one-hot encoded"""
    return df_col.nunique() / df_col.count() < 0.05


def is_numeric(df_col: pd.Series) -> bool:
    """Checks if the dtype of the given pd.Series is a subtype of np.number"""
    return np.issubdtype(df_col.dtype, np.number)


def _impute_data(df: pd.DataFrame, categorical_all: bool = False, categorical_subset: list = None) -> pd.DataFrame:
    """Imputes missing numerical or categorical values if the percentage of rows containing NaN's is > 5%.
    Else, returns a dataframe without those rows.
        Usage:
        -------
        dataframe_no_nan = impute_data(dataframe_with_nan)
    """
    df = df.infer_objects()
    cols_to_use = list(df.columns)

    if df.isna().sum().sum() / df.shape[0] <= 0.05:
        return df.dropna().get_dummies()

    catimpute = CategoricalImputer()

    if categorical_all is True and categorical_subset is not None:
        warnings.warn(
            "categorical_all and subset both specified ... using subset and continuing")
        categorical_all = False

    if categorical_all:
        for column in cols_to_use:
            if is_likely_categorical(df[column]):
                warnings.warn(
                    "Column {} is likely categorical, creating dummies... run with categorical=False or categorical_subset=[column names] to disable warning".format(
                        column)
                )

                df[column] = catimpute.fit_transform(df[column])
                df[column] = pd.get_dummies(data=df[column])
                cols_to_use.remove(column)

    if categorical_subset is not None:
        for col in categorical_subset:
            df[col] = catimpute.fit_transform(df[col])
            df[col] = pd.get_dummies(data=df[col])
            cols_to_use.remove(col)

    for col in cols_to_use:
        if df[col].isna().sum() > 0:
            if is_numeric(df[col]):
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                warnings.warn(
                    "Column {} cannot be made numeric, dropping and continuing...".format(col))
                df.drop(col, axis=1, inplace=True)

    return df


def clean(df: pd.DataFrame, categorical: bool = False, categorical_subset: list = None) -> pd.DataFrame:
    """Returns cleaned DataFrame with ONLY numeric values (can be categorical)
        Usage:
        ------
        prepared_data = clean(raw_data)
    """
    return _impute_data(df, categorical, categorical_subset)
