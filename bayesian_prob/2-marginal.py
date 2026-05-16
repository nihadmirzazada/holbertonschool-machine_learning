#!/usr/bin/env python3
import numpy as np
from importlib import import_module

intersection = import_module('1-intersection').intersection


def marginal(x, n, P, Pr):
    return np.sum(intersection(x, n, P, Pr))
