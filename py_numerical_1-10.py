# Approximate the value of \pi using The Gregory–Leibniz series:
#   arctan(1) = \frac{\pi}{4} = 1 - 1/3 + 1/5 - 1/7 + 1/9 -/+ ...
#   \frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}

import numpy as np 
 
n = 100
s = 0
m = 1.0
for i in range(n):
    t  = m*(2*i+1)
    s += 1/t
    m = -m
 
print ( 'pi = {:16.15f}'.format( 4*s ) )
# n =  50 -> pi = 3.121594652591011
# n = 100 -> pi = 3.131592903558554
 
print ( 'pi = {:16.15f}'.format( 4*np.arctan(1) ) )
# -> pi = 3.141592653589793

#####################################################################
