# Evaluate the following polynomial at x=1/3 using the Horner scheme.
#
#  p(x) = 3 x^3 - 2 x^2 - x + 1

a = [1,-1,-2,3]   # coefficients: a0, a1, a2, a3
x = 1./3
n = len(a)
b = a[n-1]
for i in range(1,n):
    b = a[n-i-1] + b*x

print ( 'ans = {:16.15f}'.format( b ) )
# -> ans = ans = 0.555555555555556

print ( 'ans = {:16.15f}'.format( 5./9) )
# -> ans = 0.555555555555556

#####################################################################
