# Calculate an approximate value of exp(x), where x=1/3
# using the following formula (Taylor Series):
#
#  e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}

import numpy as np 

x = 1./3
n = 15
s = 0
f = 1
p = 1
for i in range(n):
    s += p/f
    p *= x
    f *= (i+1)

print ( 'exp(1./3) = {:16.15f}'.format( s ) )
# n = 5  -> exp(1./3) = 1.395576131687243
# n = 10 -> exp(1./3) = 1.395612425081278
# n = 15 -> exp(1./3) = 1.395612425086090

print ( 'exp(1./3) = {:16.15f}'.format( np.exp(1./3) ) )
# -> exp(1./3) = 1.395612425086090

#####################################################################
