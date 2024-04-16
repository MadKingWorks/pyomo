#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2024 remote <remote@MadKingWorks>
#
# Distributed under terms of the MIT license.

"""
problem is:
    maximise x + xy given
    -x+2xy<=8
    2x+y<=14
    2x-y<=10
    0<=x<=10
    0<=y<=10


"""
import numpy as np
from geneticalgorithm import geneticalgorithm as ga


def f(x):
    penalty = 0
    # the penalty has to be maximised if the optimum value is not found
    if not (2 * x[0] + 2 * x[0] * x[1] <= 8):
        penalty = np.inf
    if not (2 * x[0] + x[1] <= 14):
        penalty = np.inf
    if not (2 * x[0] - x[1] <= 10):
        penalty = np.inf

    # return the minimum objective value
    return -(x[0] + x[1] * x[0] + penalty)


# define the bounds of the variables
# x[0] and x[1] are x and y here

varbounds = np.array([[0, 10], [0, 10]])
vartype = np.array([["int"], ["int"]])
model = ga(
    function=f, dimension=2, variable_type_mixed=vartype, variable_boundaries=varbounds
)

model.run()
