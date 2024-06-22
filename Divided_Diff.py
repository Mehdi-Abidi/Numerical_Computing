
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def divided_difference_table(x, y):
    n = len(x)
    F = [[0] * n for _ in range(n)]
    for i in range(n):
        F[i][0] = y[i]

    for j in range(1, n):
        for i in range(j, n):
            F[i][j] = (F[i][j-1] - F[i-1][j-1]) / (x[i] - x[i-j])

    # Print Divided Difference Table
    print("Divided Difference Table:")
    print(tabulate(F, headers=x, tablefmt='github'))

    return F

def newton_div_dif_poly(x, y, xi):
    F = divided_difference_table(x, y)  # Saving divided difference in a variable F
    n = len(x)
    prod = np.poly1d(1)
    N = np.poly1d(F[0][0])
    for i in range(1, n):
        prod = np.poly1d(x[0:i], True)
        N += np.poly1d(F[i][i] * (prod.c))

    print("\nNewton's Divided Difference Polynomial:")
    print(N)

    interpolated_value = N(xi)
    print("\nInterpolated value at x =", xi, "is:", interpolated_value)

    # Plotting
    xp = np.linspace(min(x), max(x), 100)
    yp = N(xp)

    plt.figure(figsize=(8, 6))
    plt.plot(xp, yp, label="Newton's Divided Difference Poly")
    plt.plot(xi, interpolated_value, 'bo', label='Interpolated Point at x={}'.format(xi))
    plt.plot(x, y, 'ro', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title("Newton's Divided Difference Interpolation")
    plt.show()

# Given data points
x = [0, 20, 40, 60, 80, 100]
y = [26.0, -48.6, 61.6, -71.2, 74.8, -75.2]

# User input for interpolation point
xi = float(input("Enter the value of x for interpolation: "))

# Call the function
newton_div_dif_poly(x, y, xi)
