import math

# Calculate by approximation: ln(1+x) where x=1/3 
# Use the following formula:
#  ln(1+x) = \lim_{n \rightarrow \infty} \sum_{k=1}^{n} \frac{1}{k}\Big(\frac{x}{1+x}\Big)^k 

x=1./3
n=20
s=0
for k in range(1, n+1):
    s += (1.0/k)*(x/(1.0+x))**k

print ('{:.16f}'.format(s) )

# use the function math.log() to compute ln(1+x)
print ('{:.16f}'.format( math.log(1+x) ) )

# -> 0.2876820724517666
# -> 0.2876820724517808

#####################################################################
