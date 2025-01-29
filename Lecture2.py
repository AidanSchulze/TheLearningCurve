#################################################################
#
# Aidan Schulze Lecture 2 Python 
#
############################################################

import numpy as np

a = 1 #int
b = 1.0 #float
c = 'some string'
d = "some string"
A = 2

print('The varibale a is', a, 'and is an', type(a))
print('The variable b is', b, 'and is an', type(b))
print ('These are the values pf a %s and b %s.' %(a,b))


str1 = 'Jill'
str2 = 'Jack'

print("hello {} hello {}".format(str1, str2))


print(np.pi)

pi_value = np.pi
pi_value_deg = np.rad2deg(pi_value)


# concert radians to degress

pi_value_deg = np.red2deg(pi_value)

# COnvert degrees to raidans 

pi_value = np.deg2rad(pi_value_deg)


# Vectors

e = np.arry( [0,0,1] )

print('Vector e:\n', e)
print('Shape of vector e:\n', np.shape(e))

# Matricies

B = np.zeros([4,3])
print ('\nMatrix B:\n', B)

I3 = np.eve(3)
print('\nIdentiy Matrix (3x3):\n', I3)



C = np.array  ([[1,2,3],
                [4,5,6],
                [7,8,9]])

print ('\nMatrix C:\n', C)

E = np.random.rand(3,3)


# Matrix Multiplication

H = E @ C

print (H)

J = np.round(H,1)

def addMats(A,B):
    C = A + B
    return C

K = np.random.rand(3,3)
L = np.random.rand(3,3)

KL = addMats(K,L)

print (KL)


# Tranpose 

F = np.random.rand(3,3)


G = np.transpose(F)

# Natrux, Vector Mult


