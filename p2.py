# 2. Lagrange Interpolation and Detailed Error Calculation

import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_new):
    def L(k, x_point):
        term = [(x_point - x[j]) / (x[k] - x[j]) for j in range(len(x)) if j != k]
        return np.prod(term)

    y_new = np.array([sum(y[k] * L(k, x_point) for k in range(len(x))) for x_point in x_new])
    return y_new

def mean_absolute_error(y_true, y_pred):
    # Calculate the absolute differences
    abs_diff = np.abs(y_true - y_pred)
    print("\nAbsolute differences between true and predicted values:")
    print(abs_diff)
    
    # Calculate the mean of absolute differences
    mae = np.mean(abs_diff)
    return mae

# Get input from user
x_points = list(map(float, input("Enter x points (space-separated): ").split())) #[1, 2, 3, 4, 5]
y_points = list(map(float, input("Enter y points (space-separated): ").split())) #[1, 4, 9, 16, 25]

# Convert input lists to numpy arrays
x_points = np.array(x_points)
y_points = np.array(y_points)

print("Original data points (x, y):")
print(list(zip(x_points, y_points)))

# New points for evaluation
x_new = np.linspace(min(x_points), max(x_points), 100)
y_new = lagrange_interpolation(x_points, y_points, x_new)

# Evaluate the polynomial at original points for error calculation
y_lagrange_original = lagrange_interpolation(x_points, y_points, x_points)

# Calculate error
error_lagrange = mean_absolute_error(y_points, y_lagrange_original)
print("\nLagrange Interpolation Error (MAE):", error_lagrange)

# Displaying detailed step-by-step Lagrange polynomial construction
print("\nLagrange Polynomial Construction Details:")
for k in range(len(x_points)):
    print(f"Basis polynomial L_{k}(x):")
    for j in range(len(x_points)):
        if j != k:
            print(f"(x - {x_points[j]}) / ({x_points[k]} - {x_points[j]})")

# Print original and interpolated values
print("\nOriginal and interpolated values at original data points:")
for i, (orig, interp) in enumerate(zip(y_points, y_lagrange_original)):
    print(f"x = {x_points[i]}, Original y = {orig}, Interpolated y = {interp}")

# Plotting the results
plt.scatter(x_points, y_points, color='red', label='Data Points')
plt.plot(x_new, y_new, label='Lagrange Interpolating Polynomial')
plt.legend()
plt.title("Lagrange Interpolation")
plt.show()
