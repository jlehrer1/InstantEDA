import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

def impute_data(df: pd.DataFrame) -> pd.DataFrame:
    imputer = KNNImputer()
    for column in df.columns:
        if df[column].isna().sum() != 0:
            df[column] = imputer.fit_transform(df[[column]])
    return df
    
 
