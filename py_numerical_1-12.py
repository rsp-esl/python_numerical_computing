# Evaluate the following polynomial at x=1/3 using the Horner scheme.
#
#  p(x) = 3 x^3 - 2 x^2 - x + 1
#
# Hint: use Numpy's poly1d functions

from numpy import poly1d

p = poly1d( [3,-2,-1,1] )

print (p)
#    3     2
# 3 x - 2 x - 1 x + 1

print ( 'ans: {:16.15f}'.format( p(1./3) ) )
# -> ans: 0.555555555555556

# import numpy
# numpy.info( 'poly1d' )

#####################################################################
