# Evaluate the following polynomial at x=1/3
#   p(x) = 1/(1-x) = 1 + x + x^2 + x^3 + ... + x^n + ..., |x| < 1
#
# Hint: use the Horner scheme

x = 1.0/3
n = 30
b = 1
for i in range(n):
    b = 1 + b*x

print ( '{:16.15f}'.format( b ) )
# n=30 -> s = 1.499999999999998

x = 1.0/3
n = 30
b = 1
for i in range(n):
    b = 1 + b*x

print ( '{:16.15f}'.format( b ) )
# n=30 -> s = 1.499999999999998

#####################################################################
