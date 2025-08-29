import numpy as np

def clean_inventory(df):
    df = df.drop_duplicates(subset='SKU')
    df = df[df['OnHandQty'] >= 0]
    df['ReorderQty'] = np.maximum(0, df['ReorderPoint'] - df['OnHandQty'])
    return df
