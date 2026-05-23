
#!/usr/bin/env python3

"""Sort DataFrame by High price descending"""

def high(df):

    """Sort by High column in descending order"""

    return df.sort_values(by='High', ascending=False)

