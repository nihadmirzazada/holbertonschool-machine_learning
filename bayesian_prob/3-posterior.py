#!/usr/bin/env python3
import numpy as np
from importlib import import_module

intersection = import_module('1-intersection').intersection
marginal     = import_module('2-marginal').marginal


def posterior(x, n, P, Pr):
    return intersection(x, n, P, Pr) / marginal(x, n, P, Pr)
