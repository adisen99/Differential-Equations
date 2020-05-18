#-------------Python Code--------------------------
# The following is the algorithm to determine
# solution of a user-defined differential equation
# using the Modified Euler's method, given the initial 
# conditions and using the data obtained to plot  
# the curve of the function y(x)
#--------------------------------------------------

# import the necessary libraries
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

dfx = input("Enter the function whose left hand side is dy/dx :")      # take function as input from the user
df  = lambda x,y: eval(dfx) 

x0 = float(input('Starting point:'))		# initial value of x 
xf = float(input('End Point:'))				# final value of x i.e. the value upto which you want to determine y
n  = int(input('Number of intervals:'))		# number of intervals
# initial condition i.e. value of y at x = x0
y0 = float(input('Initial condition i.e. value of y when x is at its initial value:')) 

h = (xf - x0)/n 				# Define the interval size

# Initialise the iteration
x = np.arange(x0, xf, h)
y = np.zeros([n])
y[0] = y0

# Euler's method algorithm
for i in range(1,n):
	x[i] = x[i - 1] + h
	y[i] = y[i - 1] + (h/2.0)*(df(x[i - 1],y[i -1]) + df(x[i - 1] + h,y[i - 1] + h*df(x[i - 1],y[i -1])))
	

# Obtain the data
for i in range(n):
	print(round(x[i],3),round(y[i],3),round(df(x[i],y[i]),3))

# Plot the curve
fig = plt.figure()
plt.plot(x, y, '-bo', label = 'Function')
plt.plot(x, df(x,y), '-gD', label = 'Derivative')
plt.xlabel('Value of x')
plt.ylabel('Value of y')
plt.title('Approximate Solution with Forward Euler’s Method')
plt.legend()
plt.show()