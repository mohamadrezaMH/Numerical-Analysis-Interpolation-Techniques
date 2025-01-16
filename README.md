### Method Description for Interpolation in Python:
In Python, one of the most common methods for interpolation is using the SciPy library. This library provides a comprehensive set of functions and tools for scientific and engineering computations, including various interpolation functions.

#### Interpolation Methods in SciPy:
SciPy offers several interpolation methods through its `scipy.interpolate` subpackage. The most commonly used methods include `interp1d` for 1D interpolation and `griddata` for multidimensional interpolation.

##### interp1d:
The `interp1d` function is used for 1D interpolation, and it can perform both linear and nonlinear interpolation. This function takes input data and generates an interpolation object (a function) that can be used to calculate values at new points.

- **Types of Interpolation**: The `interp1d` function can perform different types of interpolation. Some common types that can be specified with the `kind` parameter are:
  - `kind='linear'`: Linear interpolation (default).
  - `kind='nearest'`: Nearest neighbor interpolation.
  - `kind='zero'`: Zero-order (step) interpolation.
  - `kind='slinear'`: Piecewise linear interpolation.
  - `kind='quadratic'`: Quadratic interpolation.
  - `kind='cubic'`: Cubic interpolation.
  
##### griddata:
For multidimensional interpolation, `scipy.interpolate.griddata` is used. This function allows us to interpolate multidimensional data, making it ideal for more complex datasets.

---

### Error Calculation:
To measure interpolation accuracy, we use the **Mean Absolute Error (MAE)** criterion. This helps us compute the average absolute difference between actual and predicted values. MAE is calculated as follows:

- First, compute the absolute difference between each actual value and its corresponding predicted value.
- Then, compute the average of these absolute differences.

**MAE Formula:**

![image](https://github.com/user-attachments/assets/37497458-4f19-48df-9f10-067e840be950)

Where:
- `n`: number of data points.
- `y_i`: the actual value at point `i`.
- `\hat{y}_i`: the predicted value at point `i`.

In Python, we use a simple function to compute MAE by calculating the absolute differences and averaging them.

---

### Code Explanations:

#### Code Block 1 (p1.py):
This code demonstrates the use of the Vandermonde matrix for data interpolation:

- **Vandermonde Matrix**: For given data points `x` and `y`, the Vandermonde matrix is constructed, where each row contains different powers of the values of `x`.
- **Coefficient Calculation**: By solving the matrix equation `V⋅c = y`, the polynomial coefficients are obtained.
- **Polynomial Evaluation**: Using the coefficients, the polynomial value is calculated at both the original and new points.
- **Error Calculation**: The **Mean Absolute Error (MAE)** between the actual and interpolated values is computed and displayed.
- **Plotting**: The given data points and the interpolated polynomial are plotted using `matplotlib`.

#### Code Block 2 (p2.py):
This code implements Lagrange interpolation as follows:

- **Lagrange Interpolation**: A function computes the Lagrange polynomial for data points `x` and `y`, and finds the interpolated values for new points `xnew`.
- **Lagrange Basis Polynomials**: For each `k`, the basis polynomial `Lk(x)` is computed as:
  \[
  L_k(x) = \prod_{i \neq k} \frac{x - x_i}{x_k - x_i}
  \]
- **Error Calculation**: The MAE between the actual values `y` and the interpolated values at the original points `x` is calculated.
- **Input and Output**: The user inputs the data points `x` and `y`. The code computes the interpolated values at new points and displays both the actual and interpolated values.
- **Plotting**: A graph is generated showing the original data points and the Lagrange interpolated polynomial.

#### Code Block 3 (p3.py):
This code utilizes `scipy.interpolate` as follows:

- **Using `interp1d`**: The code uses the `interp1d` function from `scipy` to create an interpolation function based on data points `x` and `y`, defaulting to linear interpolation.
- **Error Calculation**: A function computes the MAE between the actual values `y` and the interpolated values.
- **User Input**: The user enters data points `x` and `y`, which are then converted into NumPy arrays.
- **Interpolation Function**: An interpolation function is created that allows evaluating `y` values at any point `x` within the given range.
- **Error Evaluation**: The code evaluates the interpolated values at both the original and new points and computes the MAE to assess the interpolation accuracy.
- **Plotting**: Results are plotted on a graph displaying the original data points and the interpolated values.

---

### Summary of Differences Between Methods:
- **Vandermonde Interpolation** is ideal for small datasets but can become computationally expensive for larger datasets due to polynomial degree growth.
- **Lagrange Interpolation** provides an exact fit for a given set of data points, but higher-degree polynomials can cause oscillations for larger datasets.
- **SciPy's `interp1d`** offers a flexible, efficient method for 1D interpolation with various methods like linear, cubic, etc., and is widely used for practical applications.
