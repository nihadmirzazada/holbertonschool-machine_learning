#!/usr/bin/env python3
"""Compute descriptive statistics"""
import pandas as pd


def analyze(df):
    """Compute descriptive statistics excluding Timestamp column"""
    return df.drop(columns=['Timestamp']).describe()
