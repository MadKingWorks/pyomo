"""
min -4x-2y
x+y<=8
8x+3y >= -24
-6x+8y<=483x+5y<=15
x<=3
y>=0
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()
model.x = pyo.Var(bounds=(-1000, 3))
model.y = pyo.Var(bounds=(0, 1000))

y = model.y
x = model.x

model.C1 = pyo.Constraint(expr=x + y <= 8)
model.C2 = pyo.Constraint(expr=8 * x + 3 * y >= 24)
model.C3 = pyo.Constraint(expr=-6 * x + 8 * y <= 48)
model.C4 = pyo.Constraint(expr=x + 5 * y <= 15)

model.obj = pyo.Objective(expr=4 * x + 2 * y, sense=pyo.maximize)

opt = SolverFactory("glpk")
opt.solve(model)
model.pprint()
