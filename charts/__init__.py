__version__ = '0.1'


def best_correlation(df, isrc, show_heatmap=False, amount=3, isrc_column='ISRC', date_column='DATE', total_column='TOTAL'):
    """Find the best correlated tracks by their performance"""
    df = pd.pivot_table(df, values=total_column, index=[date_column],columns=isrc_column, aggfunc=np.sum)
    if show_heatmap:
        plt.figure(figsize=(15,10))
        sns.heatmap(df.corr(), cmap='RdBu', annot=True,
            annot_kws={"size": 7}, vmin=-1, vmax=1)
    df = df.corr().unstack().sort_values(ascending=False, key=abs).drop_duplicates()
    df = pd.DataFrame(df)
    df.index.rename(['ISRC1','ISRC2'], inplace=True)
    df = df.query(f"ISRC1=='{isrc}' & 0!=1").head(amount)
    df.reset_index(inplace=True)
    df = df['ISRC2'].tolist()
    df.append(isrc)
    return df
