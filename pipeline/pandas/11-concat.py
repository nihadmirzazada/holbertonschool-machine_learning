
#!/usr/bin/env python3

"""Concatenate two DataFrames"""

index = __import__('10-index').index

def concat(df1, df2):

    """Concatenate bitstamp up to 1417411920 to top of coinbase"""

    pd = __import__('pandas')

    df1 = index(df1)

    df2 = index(df2)

    df2 = df2.loc[:1417411920]

    return pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])

