from sympy import* #Call Library of sympy
def f(x):
  return(2*x/(x**2-4))

def Error_bound_trap(f,l,u):#l is the lower limit and u is the upper limit of integral
   ddf = diff(f, x,2)    #Evaluating second derivative of f
   abs_max_ddf=max(abs(ddf.subs(x,l)),abs(ddf.subs(x,u)))
   h=u-l
   Error_bound=h**3*abs_max_ddf/12
   return(Error_bound,abs_max_ddf)
