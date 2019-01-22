# show the value of 2^i, log10(2^i) and number of digts, for i=0..N
import math 

N = 16
for i in range(0,N+1):
    x = 2**i
    f = math.log10(x)
    print( '%2d) %5d, %.5f, %2d' % (i, x, f, int(math.ceil(f))) )

#  0)     1, 0.00000,  0
#  1)     2, 0.30103,  1
#  2)     4, 0.60206,  1
#  3)     8, 0.90309,  1
#  4)    16, 1.20412,  2
#  5)    32, 1.50515,  2
#  6)    64, 1.80618,  2
#  7)   128, 2.10721,  3
#  8)   256, 2.40824,  3
#  9)   512, 2.70927,  3
# 10)  1024, 3.01030,  4
# 11)  2048, 3.31133,  4
# 12)  4096, 3.61236,  4
# 13)  8192, 3.91339,  4
# 14) 16384, 4.21442,  5
# 15) 32768, 4.51545,  5
# 16) 65536, 4.81648,  5

#####################################################################
