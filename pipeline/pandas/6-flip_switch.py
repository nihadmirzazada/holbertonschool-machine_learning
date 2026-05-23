
#!/usr/bin/env python3

"""Sort in reverse chronological order and transpose"""

def flip_switch(df):

    """Sort by index descending and transpose"""

    return df.sort_index(ascending=False).transpose()

