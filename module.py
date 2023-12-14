#!/bin/bash/python3.11

# imports
import numpy as np
from scipy.stats import random_correlation
from statsmodels.tsa.tsatools import add_lag
import random

# helper functions
def make_eigs(size:int, rand_factor = 2):
    """Creates tuple of size n, where length is equal to size and sum is equal to size
    
    Parameters
    ----------
    size: int
        Whole number integer or scalar
    
    rand_factor: int, default = 2
        Increase the randomness of the returned tuple. 1 is low, for example. 10, would be higher.

    Returns
    -------
    eigs: tuple
    """
    eigs = []
    for i in range(size - 1):
        bank = size
        choices = list(np.linspace(1, size, size*rand_factor))
        idx = random.choice(choices)
        val = idx/bank
        eigs.append(val)
        bank -= 1
    eigs.append(size - sum(eigs))

    return(tuple(eigs))

def make_rand_corrmat(size:int):
    """Generates random correlation matrix
    
    Parameters
    ----------
    size: int
        Number of rows OR columns in a NxN matrix. 

    Returns
    -------
    X: ndarray
        NxN random correlation matrix
    """
    e = make_eigs(size)
    rng = np.random.default_rng()
    X = random_correlation.rvs(eigs=e, random_state=rng)

    return(X)