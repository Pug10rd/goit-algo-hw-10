import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

x = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")  
y = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += x + y, "Total Production"

model += 2 * x + y <= 100, "Water_Limit"
model += x <= 50, "Sugar_Limit"
model += x <= 30, "Lemon_Juice_Limit"
model += 2 * y <= 40, "Fruit_Puree_Limit"

model.solve()

print("Status:", pulp.LpStatus[model.status])
print("Lemonade:", x.varValue)
print("Fruit Juice:", y.varValue)
print("Total Production:", pulp.value(model.objective))
