import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

def impute_data(df: pd.DataFrame) -> pd.DataFrame:
    imputer = KNNImputer()
    
 
