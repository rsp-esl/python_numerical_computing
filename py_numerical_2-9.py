# Show the value of the machine epsilon for 64-bit floating-point

eps = 1./(2 ** 52)
print (eps)
# 2.220446049250313e-16

print (1+eps, 1-eps)
# 1.0000000000000002 0.9999999999999998

eps /= 2.
print (eps)
# 1.1102230246251565e-16

print (1+eps, 1-eps)
# 1.0 0.9999999999999999

#####################################################################
