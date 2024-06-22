from sympy import* #Call Library of sympy
x = symbols('x')   #Make x a symbol
f = x**4       #Define your function here in 'x'
def Error_bound_simp(f,l,u):#l is the lower limit and u is the upper limit of integral
   d4f = diff(f, x,4)    #Evaluating second derivative of f
   abs_max_ddf=max(abs(d4f.subs(x,l)),abs(d4f.subs(x,u)))
   h=(u-l)/2
   Error_bound=h**5*abs_max_ddf/90
   return(Error_bound,abs_max_ddf)
