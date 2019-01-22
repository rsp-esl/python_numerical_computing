# Estimate the number of digits in base=10 for 2^i and 2^-i
import math 

print ( math.pow(2,-1023) )     # 1.1125369292536007e-308
print ( math.pow(2, 1023) )     # 8.98846567431158e+307
print ( math.pow(2, 1023.999) ) # 1.796447500688184e+308
print ( math.pow(2, 1023)*2 )   # inf

#####################################################################
