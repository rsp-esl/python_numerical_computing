# The results should be 1 in both cases. Is this true ?

print ('%.16f %.16f' % (1./49*49, 1./51*51) )
print ('{:.16f} {:.16f}'.format(1./49*49, 1./51*51) )

# -> 0.9999999999999999 1.0000000000000000
# -> 0.9999999999999999 1.0000000000000000 

#####################################################################
