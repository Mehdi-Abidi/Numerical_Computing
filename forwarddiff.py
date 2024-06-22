# code of forward difference formula.

import numpy as np
from tabulate import tabulate


def forward_diff(x, y):

    # Compute the step size h
    h = x[1] - x[0]
    data=[]

    # Compute the forward difference approximation
    fdf = np.zeros_like(y)
    fdf[-1] = (y[-1] - y[-2]) / h  # use backward difference at the end point
    for i in range(len(y) - 1):
        fdf[i] = (y[i+1] - y[i]) / h
        data.append([x[i],y[i],fdf[i]])
    data.append([x[-1],y[-1],fdf[-1]])

    print(tabulate(data,headers=['x','f(x)','df(x)/dx'],tablefmt="github"))

    return
