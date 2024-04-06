import time
import pyomo.environ as pyo

from pyomo.environ import *

from pyomo.opt import SolverFactory
import pandas as pd

model = pyo.ConcreteModel()
#deckaration of x
range_i = range(1,6)
model.x = pyo.Var(range_i,within=Integers,bounds=(0,None))
x=model.x
#declaration of y
model.y = pyo.Var(bounds = (0,None))
y = model.y
#apply first consraint here

model.C1 = pyo.Constraint(expr = sum([x[i] for i in range_i]) + y <=20)

model.C2 = pyo.ConstraintList()

for i in range_i:
    model.C2.add(x[i]+y>=15)

model.C3 = pyo.Constraint(expr=sum([i*x[i] for i in range_i])>=10)

model.C4 = pyo.Constraint(expr=x[5]+2*y>=30)

#define the objective
model.obj = pyo.Objective(expr=sum([x[i] for i in range_i])+y,sense = minimize)
begin = time.time()
opt = SolverFactory('glpk')
opt.solve(model)
deltaT=time.time()-begin

model.pprint()


print(f"Time taken is {deltaT}")
print(f"The soltion is ")
for i in range_i:
    print(f"x[{i}] = {pyo.value(x[i])}")
print(f"y = {pyo.value(y)}")
print(f"Obj = {pyo.value(model.obj)}")
    


