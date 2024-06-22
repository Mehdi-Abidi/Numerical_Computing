#TASK1
import numpy as np
x=[1,2,3] # here 1,2,3 are coefficients of the polynomial in descending order
Poly1=np.poly1d(x)
Poly2=np.poly1d(x,True)
x = [0, 20,40,60, 80, 100]
y = [26.0, -48.6, 61.6, -71.2, 74.8, -75.2]
# Function to calculate Lagrange polynomial
def lagrange_poly(x, y):
    n = len(x)
    p = np.poly1d(0.0)
# Initialize the Lagrange basis polynomial for the current data point
    for i in range(n):
        L = np.poly1d(y[i])
# Iterate through all data points to construct the Lagrange basis polynomial
        for j in range(n):
            if j != i:
# Construct the ith Lagrange basis polynomial term
                L *= np.poly1d([1.0, -x[j]]) / (x[i] - x[j])
            p += L
    return p
# Interpolate at a specific point
point = float(input("Enter x-coordinate to interpolate: "))
interp_value = p(point)
# Print Lagrange polynomial and interpolated value
print("Lagrange polynomial is:")
print(p)
print("Interpolated value at x =", point, "is:", interp_value)
