# code for three point endpoint and three point midpoint formulae for finding f'(x) for an array of x and f(x).
import numpy as np

def three_point(x, y):

    # Compute the step size h
    data=[]
    h = x[1] - x[0]

    # Compute the forward difference approximation
    tp = np.zeros_like(y)
    tp[0]=(-3*y[0]+4*y[1]-y[2])/(2*h) #three point endpoint (left end) formula
    tp[-1]=(3*y[-1]-4*y[-2]+y[-3])/(2*h) #three point endpoint (right end) formula

    data.append([x[0],y[0],tp[0]])
    for i in range(1,len(y)-1):
        tp[i] = (y[i+1] - y[i-1]) / (2*h)
        data.append([x[i],y[i],tp[i]])
    data.append([x[-1],y[-1],tp[-1]])

    print(tabulate(data,headers=['x','f(x)','df(x)/dx'],tablefmt="github"))


    return
