
#!/usr/bin/env python3

"""Slice DataFrame every 60th row"""

def slice(df):

    """Extract High, Low, Close, Volume_BTC every 60th row"""

    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]

