import numpy as np

# generate 5 random numbers
for i in range(5):
    x = np.random.random_sample()
    print (x)

# generate a list of 5 random numbers
print ( np.random.random_sample((5,)) )

# import the 'sqrt' function from Numpy's 'scimath' module
from numpy.lib.scimath import sqrt

# compute the square root of 2 and print the result
print (sqrt(2.0))
# -> 1.4142135623730951

#####################################################################
