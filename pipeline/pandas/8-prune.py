
#!/usr/bin/env python3

"""Remove rows where Close is NaN"""

def prune(df):

    """Remove entries where Close has NaN values"""

    return df.dropna(subset=['Close'])

