import math

# get the mantissa and exponent as a pair (m, e) of x.
# Note: e=exponent and m=mantissa.

# Are there any errors in the results ?

values = [2.5, 0.1, 0.005, 1/(2**52)]
for x in values:
    m, e = math.frexp(x)
    print ( '%.32f = %.18f * 2**(%d)' % (m * 2**e, m, e) )

#####################################################################
