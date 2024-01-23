import xpress as xp
# xp.init('/Applications/FICO Xpress/xpressmp/bin/xpauth.xpr')
xp.init()
x1 = xp.var(vartype=xp.integer, name='x1', lb=-10, ub=10)
x2 = xp.var(name='x2')
p = xp.problem(x1, x2,            # variables of the problem
               x1**2 + 2*x2,      # single expression is taken as the objective function
               x1 + 3*x2 >= 4,    # one or more constraints
               name='myexample')  # problem name (optional)
p.optimize()
print ("solution: {0} = {1}; {2} = {3}".format (x1.name, p.getSolution(x1), x2.name, p.getSolution(x2)))