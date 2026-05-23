#!/usr/bin/env python3
"""Convert last 10 rows of High and Close to numpy array"""
import pandas as pd


def array(df):
    """Select last 10 rows of High and Close, return as numpy array"""
    return df[['High', 'Close']].tail(10).to_numpy()
