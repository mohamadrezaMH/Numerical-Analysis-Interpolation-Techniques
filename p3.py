# 3. Using scipy for Interpolation and Detailed Error Calculation

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

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

# Create the interpolation function
interp_function = interp1d(x_points, y_points, kind='linear')

# Display the interpolation function details
print("\nInterpolation function created using scipy's interp1d with linear method.")

# New points for evaluation
# use x_new and y_new for visualization data with matplotlib
x_new = np.linspace(min(x_points), max(x_points), 100)
y_new = interp_function(x_new)

# Display new points for evaluation
print("\nNew points for evaluation (x_new):")
print(x_new)

# Evaluate the polynomial at original points for error calculation
y_interp_original = interp_function(x_points)

# Calculate error
error_interp = mean_absolute_error(y_points, y_interp_original)
print("\nScipy Interpolation Error (MAE):", error_interp)

# Print original and interpolated values
print("\nOriginal and interpolated values at original data points:")
for i, (orig, interp) in enumerate(zip(y_points, y_interp_original)):
    print(f"x = {x_points[i]}, Original y = {orig}, Interpolated y = {interp}")

# Plotting the results
plt.scatter(x_points, y_points, color='red', label='Data Points')
plt.plot(x_new, y_new, label='Scipy Interpolation')
plt.legend()
plt.title("Scipy Interpolation")
plt.show()