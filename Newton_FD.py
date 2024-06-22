
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt
def forward_divided_difference_table(x, y):
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = F[i + 1, j - 1] - F[i, j - 1]
    return F

def newton_forward_div_dif_poly(x, y, xi):
    F = forward_divided_difference_table(x, y)
    n = len(x)
    prod = np.poly1d(1)
    N = np.poly1d(F[0, 0])
    for i in range(1, n):
        prod *= np.poly1d([1, -x[i-1]])
        N += (F[0, i] * prod) / (mt.factorial(i) * (x[1] - x[0])**i)

    print("Newton's Forward Divided Difference Polynomial:")
    print(N)

    interpolated_value = N(xi)
    print("Interpolated value at x =", xi, "is:", interpolated_value)

    # Plotting
    xp = np.linspace(min(x), max(x), 100)
    yp = N(xp)

    plt.figure(figsize=(8, 6))
    plt.plot(xp, yp, label="Forward Divided Difference Polynomial")
    plt.plot(xi, interpolated_value, 'bo', label='Interpolated Point at x={}'.format(xi))
    plt.plot(x, y, 'ro', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title("Newton's Forward Divided Difference")
    plt.show()


df = pd.read_csv('/interpolation.csv')
x = df['x'].values
y = df['y'].values

point = float(input("Enter x-coordinate to interpolate: "))

# Call the function
newton_forward_div_dif_poly(x, y, point)
