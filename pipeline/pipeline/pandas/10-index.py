#!/usr/bin/env python3
"""Set Timestamp as index"""
import pandas as pd


def index(df):
    """Set Timestamp column as the index"""
    return df.set_index('Timestamp')
