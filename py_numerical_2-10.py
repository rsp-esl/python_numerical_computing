# Compute the following two arithmetic expressions 
# and notice the difference

print ('{:.32f}'.format(4/3 - 1/3))
print ('{:.32f}'.format(7/3 - 4/3))
# 1.00000000000000000000000000000000
# 1.00000000000000022204460492503131

print ('{:.32f}'.format(1./2**52))
# 0.00000000000000022204460492503131

print (bin(int(4./3 * 2**52)).zfill(53) )

# 0b10101010101010101010101010101010101010101010101010101

x = 0b100101010101010101010101010101010101010101010101010110
y = 0b010101010101010101010101010101010101010101010101010101
result  = x-y
bin_str = bin(result)[2:]
print (bin_str, len(bin_str))

# 10000000000000000000000000000000000000000000000000001 53

#####################################################################
