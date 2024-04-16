
import pyomo.environ as pyo
from pyomo.environ import *
import time
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()
opt=SolverFactory('ipopt',executable='~/Downloads/ipopt/ipopt.mexa64')

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x=model.x
y=model.y


model.C1=pyo.Constraint(expr= -x+2*x*y<=8)

model.C2=pyo.Constraint(expr= 2*x+y<=14)
model.C3=pyo.Constraint(expr= 2*x-y<=10)

model.obj = pyo.Objective(expr=x+y*x,sense=maximize)
opt.solve(model)
model.pprint()


