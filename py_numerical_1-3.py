import numpy as np

# Calculate/approximate the pi number
# by using the following formula:
#  \pi^2/6 = \sum_{k=1}^{\infty} 1/k^2

s = 0.0
n = 1000000
for k in range(1,n):
    s += 1.0/(k*k)
pi = np.sqrt(6*s)
print ( 'pi = {:16.15f}'.format( pi ) )

pi = 4*np.arctan(1)
print ( 'pi = {:16.15f}'.format( pi ) )

print ( 'pi = {:16.15f}'.format( np.pi ) )

# -> pi = 3.141591698659554
# -> pi = 3.141592653589793
# -> pi = 3.141592653589793

#####################################################################
