#-------------Python Code--------------------------
# The following is the algorithm to determine
# solution of a user-defined differential equation
# using the Milne's predictor-corrector method
# given the initial conditions and using the 
# data obtained to plot the curve of the function y(x)
#--------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

# Define the function prefixes using NumPy
sin = np.sin
cos = np.cos
tan = np.tan
pi  = np.pi
exp = np.exp
ln  = np.log
log = np.log10

dfx = input("Enter the function whose left hand side is dy/dx :")   # take function as input from the user
df  = lambda x,y: eval(dfx)

x4 = float(input('Enter the value of x at which the solution is required:')) 

# This is the code to get the values of function y at different values of x
n = int(input('Enter the no. of elements known then enter the items in separate lines with a space:')) # n is the number of items you want to enter
d = {}                     

# This for loop helps to obtain the user's input as a dictionary
for i in range(n):        
    text = input().split()     # split the input text based on space & store in the list 'text'
    d[text[0]] = text[1]       # assign the 1st item to key and 2nd item to value of the dictionary

print('The table inserted by you is:',d)

# Obtain the x values separately and print them out

x_val = list(d.keys()) # Convert the dictionary to list by obtaining all the y values i.e. the values of the dictionary
x_val = [float(i) for i in x_val] # Convert the items of the list from strings to floats
print('The different values of x are',x_val)

# Obtain the y values separately and print them out

y_val = list(d.values()) # Convert the dictionary to list by obtaining all the y values i.e. the values of the dictionary
y_val = [float(i) for i in y_val] # Convert the items of the list from strings to floats
print('The different values of y at respective values of x are',y_val)

# Obtain the value of h

h = x_val[1] - x_val[0]

# THE FOLLOWING IS THE ALGORITHM FOR MILNE'S PREDICTOR FORMULA

# The following are the values of f0, f1, f2 and f3

f0 = df(x_val[0],y_val[0])
f1 = df(x_val[1],y_val[1])
f2 = df(x_val[2],y_val[2])
f3 = df(x_val[3],y_val[3])

# Next we get the corresponding value of x_sol at which solution is required

y4 = y_val[0] + (4*(h/3))*(2*f1 - f2 + 2*f3)

# Obtain the value of f4

f4 = df(x4,y4)

# THE FOLLOWING IS THE ALGORITHM FOR MILNE'S CORRECTOR FORMULA to improve the value of y4

y4_corrected = y_val[2] + (h/3)*(f2 + 4*f3 + f4)

print('The value of y at given value of x is:',y4_corrected)


