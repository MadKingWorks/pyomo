#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2024 rahul <rahul@MadkIngWorks>
#
# Distributed under terms of the MIT license.

"""
optimal power gen using pyomo and pandas
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import pandas as pd

data_gen = pd.read_csv('inputs.csv')
data_loads = pd.read_csv('loads.csv')

number_generators = len(data_gen)

model = pyo.ConcreteModel()
#define power generation 
model.pg = pyo.Var(range(number_generators),bounds=(0,None))
pg=model.pg



















