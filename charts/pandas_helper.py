import pandas as pd
import numpy as np

def prepare_pivot(df, total_column, date_column, group_column):
    """Make pivot table from pandas dataframe data"""
    df = pd.pivot_table(df, values=total_column, index=[date_column], columns=group_column,
                        aggfunc=np.sum)
    df.index = pd.to_datetime(df.index, errors='coerce')
    return df
