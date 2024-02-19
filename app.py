from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, minimize, Constraint, SolverFactory, value
import time

# Create a Concrete Model
model = ConcreteModel()

# Define the decision variables
model.x = Var(within=NonNegativeReals)
model.y = Var(within=NonNegativeReals)
model.z = Var(within=NonNegativeReals)

# Define the objective function
model.obj = Objective(expr=2*model.x + 3*model.y + 5*model.z, sense=minimize)

# Define the constraints
model.constraint1 = Constraint(expr=3*model.x + 4*model.y + 2*model.z >= 10)
model.constraint2 = Constraint(expr=2*model.x + model.y + 3*model.z >= 8)
model.constraint3 = Constraint(expr=model.x + 3*model.y + 2*model.z >= 6)

# Import the GLPK solver
opt = SolverFactory('glpk')

# Benchmarking
start_time = time.time()

# Solve the optimization problem
results = opt.solve(model)

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Print the results
results.write()

# Print the variable values
print("Variable x =", value(model.x))
print("Variable y =", value(model.y))
print("Variable z =", value(model.z))

# Print the elapsed time
print("Elapsed time:", elapsed_time, "seconds")
