 def comp_trapezoidal_rule(f, a, b, n=1):  #n=1 indicates simple trpezoidal rule
     h = (b - a) / n
     x = [a + i*h for i in range(n+1)]
     y = [f(xi) for xi in x]
     s = sum(y[1:-1])
     ans=h/2 * (y[0] + 2*s + y[-1])
     return ans
