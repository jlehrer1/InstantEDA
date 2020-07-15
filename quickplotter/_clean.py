import warnings

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn_pandas import CategoricalImputer


def is_likely_categorical(df_col: pd.Series) -> bool:
    """Heuristic method to check if column is likely categorical. If the ratio between the number of unique and
    total number of rows is small (< 0.05) then the column might be categorical and can be one-hot encoded"""
    return df_col.nunique() / df_col.count() < 0.05


def _is_numeric(df_col: pd.Series) -> bool:
    """Checks if the dtype of the given pd.Series is a subtype of np.number"""
    return np.issubdtype(df_col.dtype, np.number)


def _impute_data(df: pd.DataFrame, categorical_all: bool = False, categorical_subset: list = None) -> pd.DataFrame:
    """Imputes missing numerical or categorical values if the percentage of rows containing NaN's is > 5%.
    Else, returns a dataframe without those rows.
        Usage:
        -------
        dataframe_no_nan = impute_data(dataframe_with_nan)
    """

    # try to infer object types, as this will make calculating numeric columns much easier
    df = df.infer_objects()

    # If there are very few missing values (<= 5%), then just drop those rows and return the DataFrame, as
    # it should be enough for the provided plots
    if df.isna().sum().sum() / df.shape[0] <= 0.05:
        return df.dropna().get_dummies()

    catimpute = CategoricalImputer()

    if categorical_all is True and categorical_subset is not None:
        warnings.warn(
            "categorical_all and subset both specified ... using subset and continuing")
        categorical_all = False

    # Try and make dummies for all categorical columns
    if categorical_all:
        likely_categorical_cols = []
        for col in df.columns:
            if is_likely_categorical(df[col]):
                df[col] = pd.get_dummies(data=df[col])
                df[col] = catimpute.fit_transform(df[col])

                likely_categorical_cols.append(col)
        if likely_categorical_cols is not None:
            # Grammatically correct
            if len(likely_categorical_cols) > 1:
                warnings.warn(
                    "Columns {} are likely categorical, creating dummies. Run with categorical=False (to disable all) or categorical_subset=[column names] to disable warning".format(
                        likely_categorical_cols)
                )
            else:
                warnings.warn(
                        "Column \"{}\" is likely categorical, creating dummies. Run with categorical=False (to disable all) or categorical_subset=[column names] to disable warning".format(
                        likely_categorical_cols[0])
                )

    # Or only make dummies for specified columns
    if categorical_subset is not None:
        for col in categorical_subset:
            # NaN's should be ignored here
            df[col] = pd.get_dummies(data=df[col])
            df[col] = catimpute.fit_transform(df[col])

    df.infer_objects()

    for col in df.columns:
        if df[col].isna().sum() > 0:
            if _is_numeric(df[col]):
                # fill using mean TODO: allow this to be specified
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                warnings.warn(
                    "Column \"{}\" cannot be made numeric, dropping and continuing. If this is incorrect, specify it as categorical or transform to a numeric dtype".format(col))
                df.drop(col, axis=1, inplace=True)

    return df


def clean(df: pd.DataFrame, categorical_all: bool = False, categorical_subset: list = None) -> pd.DataFrame:
    """Returns cleaned DataFrame with ONLY numeric values (can be categorical)
        Usage:
        ------
        prepared_data = clean(raw_data)
    """
    return _impute_data(df, categorical_all, categorical_subset)
