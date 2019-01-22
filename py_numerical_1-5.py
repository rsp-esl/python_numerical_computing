from math import sinh, exp, e, pi

# Evaluate Hyperbolic Sine function: sinh⁡(x) at x=2\pi,
# using three different methods:

x  = 2*pi
r1 = sinh(x)
r2 = (exp(x) - exp(-x))/2
r3 = (e**(x) - e**(-x))/2
print ('{:.16f}\n{:.16f}\n{:.16f}'.format(r1,r2,r3) )

# -> 267.7448940410164369
# -> 267.7448940410164369
# -> 267.7448940410163232

#####################################################################
