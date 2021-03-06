# Evaluate the following polynomial at x=1/3
#  p(x) = 1/(1-x) = 1 + x + x^2 + x^3 + ... + x^n + ..., |x| < 1

x = 1.0/3
n = 30
s = 0
p = 1
for i in range(n):
    s += p
    p *= x

print( 's = {:16.15f}'.format(s) )
# n=10 -> s = 1.499974597368287
# n=20 -> s = 1.499999999569804
# n=30 -> s = 1.499999999999993

print ( 's = {:16.15f}'.format( 1/(1-1.0/3)) )
# -> s = 1.500000000000000

#####################################################################
