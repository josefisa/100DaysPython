import numpy as np
from scipy.optimize import minimize

def economic_dispatch(D, P_min, P_max):

    # Cost functions
    def cost_func(P):
        P1, P2, P3 = P
        c1 = 40 + 11.5*P1 + 0.02*P1**2
        c2 = 150 + 7.5*P2 + 0.004*P2**2
        c3 = 100 + 9.3*P3 + 0.003*P3**2
        return c1 + c2 + c3
    
    # Power balance constraint: P1 + P2 + P3 = D
    def power_balance(P):
        return P[0] + P[1] + P[2] - D
    
    # Initial guess (equal division among generators)
    P_init = [D/3, D/3, D/3]
    
    # Adjust initial guess if outside bounds
    for i in range(3):
        if P_init[i] < P_min[i]:
            P_init[i] = P_min[i]
        elif P_init[i] > P_max[i]:
            P_init[i] = P_max[i]
    
    # Constraints
    constraints = [{'type': 'eq', 'fun': power_balance}]
    
    # Bounds for each generator
    bounds = [(P_min[0], P_max[0]), (P_min[1], P_max[1]), (P_min[2], P_max[2])]
    
    # Solve the optimization problem
    result = minimize(
        cost_func,
        P_init,
        method='SLSQP',
        constraints=constraints,
        bounds=bounds,
        options={'disp': False}
    )
    
    # Extract results
    P1, P2, P3 = result.x
    total_cost = result.fun
    
    # Calculate lambda (marginal cost)
    # Lambda is the partial derivative of each cost function at the optimal point
    lambda1 = 11.5 + 0.04*P1
    lambda2 = 7.5 + 0.008*P2
    lambda3 = 9.3 + 0.006*P3
    
    # In a perfect solution, all lambdas would be equal
    # We can take the average as an approximation
    lambda_avg = (lambda1 + lambda2 + lambda3) / 3
    
    return {
        "D": D,
        "P1": P1,
        "P2": P2,
        "P3": P3,
        "lambda": lambda_avg,
        "Total Cost": total_cost,
        "Success": result.success
    }

# Example usage
D_values = [400, 300, 350]

# Define generation limits [min, max] for each generator
P1_limits = [30, 100]   # Generator 1: 50 ≤ P1 ≤ 200
P2_limits = [40, 300]   # Generator 2: 20 ≤ P2 ≤ 150
P3_limits = [50, 50]   # Generator 3: 30 ≤ P3 ≤ 180

results = []
for D in D_values:
    # Check if the problem is feasible
    min_total = P1_limits[0] + P2_limits[0] + P3_limits[0]
    max_total = P1_limits[1] + P2_limits[1] + P3_limits[1]
    
    if D < min_total:
        print(f"Demand {D} is less than minimum possible generation {min_total}")
        continue
    elif D > max_total:
        print(f"Demand {D} exceeds maximum possible generation {max_total}")
        continue
    
    result = economic_dispatch(D, 
                              [P1_limits[0], P2_limits[0], P3_limits[0]],
                              [P1_limits[1], P2_limits[1], P3_limits[1]])
    results.append(result)

# Print results in a formatted way
print("\nOptimal Power Dispatch Results:")
print("-------------------------------")
for result in results:
    print(f"\nDemand: {result['D']} MW")
    print(f"P1: {result['P1']:.2f} MW")
    print(f"P2: {result['P2']:.2f} MW")
    print(f"P3: {result['P3']:.2f} MW")
    print(f"Sum: {result['P1'] + result['P2'] + result['P3']:.2f} MW")
    print(f"Marginal Cost (λ): ${result['lambda']:.4f}/MW")
    print(f"Total Cost: ${result['Total Cost']:.2f}")

