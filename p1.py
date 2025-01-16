# 1. Interpolation with Direct Method (Vandermonde Matrix) and Detailed Error Calculation

import numpy as np
import matplotlib.pyplot as plt

def vandermonde_interpolation(x, y):
    # Create the Vandermonde matrix
    V = np.vander(x, increasing=True)
    print("Vandermonde Matrix (V):")
    print(V)
    
    # Solve the linear system to find the coefficients
    coefficients = np.linalg.solve(V, y)
    print("\nCoefficients of the polynomial:")
    print(coefficients)
    
    return coefficients

def evaluate_polynomial(coefficients, x):
    return np.polyval(coefficients[::-1], x)

def mean_absolute_error(y_true, y_pred):
    # Calculate the absolute differences
    abs_diff = np.abs(y_true - y_pred)
    print("\nAbsolute differences between true and predicted values:")
    print(abs_diff)
    
    # Calculate the mean of absolute differences
    mae = np.mean(abs_diff)
    return mae

# Get input from the user
x_points = np.array(list(map(float, input("Enter x points (space-separated): ").split()))) #[1, 2, 3, 4, 5]
y_points = np.array(list(map(float, input("Enter y points (space-separated): ").split()))) #[1, 4, 9, 16, 25]

print("Original data points (x, y):")
print(list(zip(x_points, y_points)))

# Perform interpolation
coefficients = vandermonde_interpolation(x_points, y_points)

# Evaluate the polynomial at original and new points
y_vandermonde_original = evaluate_polynomial(coefficients, x_points)
x_new = np.linspace(min(x_points), max(x_points), 100)
y_vandermonde_new = evaluate_polynomial(coefficients, x_new)

# Calculate error
error_vandermonde = mean_absolute_error(y_points, y_vandermonde_original)
print("\nVandermonde Interpolation Error (MAE):", error_vandermonde)

# Print original and interpolated values
print("\nOriginal and interpolated values at original data points:")
for i, (orig, interp) in enumerate(zip(y_points, y_vandermonde_original)):
    print(f"x = {x_points[i]}, Original y = {orig}, Interpolated y = {interp}")

# Plotting the results
plt.scatter(x_points, y_points, color='red', label='Data Points')
plt.plot(x_new, y_vandermonde_new, label='Interpolating Polynomial')
plt.legend()
plt.title("Vandermonde Interpolation")
plt.show()
