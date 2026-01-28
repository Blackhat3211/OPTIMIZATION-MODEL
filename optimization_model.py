import pulp


prob = pulp.LpProblem("Maximize_Factory_Profit", pulp.LpMaximize)


A = pulp.LpVariable('Product_A_Units', lowBound=0, cat='Integer')
B = pulp.LpVariable('Product_B_Units', lowBound=0, cat='Integer')


prob += 50 * A + 40 * B, "Total_Profit"


prob += 2 * A + 1 * B <= 80, "Labor_Constraint"

prob += 1 * A + 3 * B <= 100, "Material_Constraint"


status = prob.solve()

# 6. Output the Results
print(f"Status: {pulp.LpStatus[status]}")
print(f"Produce {A.varValue} units of Product A")
print(f"Produce {B.varValue} units of Product B")
print(f"Maximum Profit: ${pulp.value(prob.objective)}")