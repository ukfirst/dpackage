__version__ = '0.1'

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from charts.pandas_helper import prepare_pivot

@dataclass
class MusicAnalysis:
    """Class to analyze and return different analytical insights about song data"""
    df: pd.DataFrame
    isrc_column: str = 'ISRC'
    date_column: str = 'DATE'
    total_column: str = 'TOTAL'

    def __post_init__(self):
        self.df = prepare_pivot(self.df, self.total_column, self.date_column, self.isrc_column)
    def best_correlation(self, isrc, amount=3, show_heatmap=False):
        """Find the best correlated tracks by their performance"""
        if show_heatmap:
            plt.figure(figsize=(15, 10))
            sns.heatmap(df.corr(), cmap='RdBu', annot=True,
                        annot_kws={"size": 7}, vmin=-1, vmax=1)
        df = self.df.corr().unstack().sort_values(ascending=False, key=abs).drop_duplicates()
        df = pd.DataFrame(df)
        df.index.rename(['ISRC1', 'ISRC2'], inplace=True)
        df.rename(columns={0: 'value'}, inplace=True)
        df = df.query(f"ISRC1=='{isrc}' & 0!=1").head(amount)
        df.reset_index(inplace=True)
        df = df[['ISRC2', 'value']].values.tolist()
        values = [[isrc, 1], *df]
        return values
