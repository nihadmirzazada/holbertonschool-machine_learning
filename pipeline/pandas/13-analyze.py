
#!/usr/bin/env python3

"""Compute descriptive statistics"""

def analyze(df):

    """Compute descriptive statistics excluding Timestamp column"""

    return df.drop(columns=['Timestamp']).describe()

