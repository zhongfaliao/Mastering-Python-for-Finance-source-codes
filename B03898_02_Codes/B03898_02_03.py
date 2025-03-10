"""
README
======
This is a Python code.
======
"""

""" A simple linear optimization problem with 2 variables """
import pulp

x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

problem = pulp.LpProblem("A simple maximization objective",
                         pulp.LpMaximize)
problem += 3*x + 2*y, "The objective function"
problem += 2*x + y <= 100, "1st constraint"
problem += x + y <= 80, "2nd constraint"
problem += x <= 40, "3rd constraint"
problem.solve()

print ("Maximization Results:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
