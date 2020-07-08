%-------------MATLAB Code--------------------------
% The following is the algorithm to determine
% solution of a user-defined differential equation
% using the Runge-Kutta method, given the initial 
% conditions and using the data obtained to plot  
% the curve of the function y(x)
%--------------------------------------------------

% User defines the function.
a    = input('Enter the function function whose left hand side is dy/dx :', 's');
df   = @(x,y)(eval(a));

x0 = input('Starting point:');		% initial value of x 
xf = input('End Point:');			% final value of x i.e. the value upto which you want to determine y
n  = input('Number of intervals:'); % number of intervals
y0 = input('Initial condition:');	% initial condition i.e. value of y at x = x0

h    = (xf-x0)/n;	% interval size	
x(1) = x0;			% Initialize the iteration
y(1) = y0;
	
% Euler's method algorithm	
for i = 1:n
	x(i+1) = x(i) + h;
	k1 = h*df(x(i),y0);
	k2 = h*df(x(i) + (h/2),y0 + (k1/2));
	k3 = h*df(x(i) + (h/2),y0 + (k2/2));
	k4 = h*df(x(i) + h,y0 + k3);
	y(i+1) = y(i) + (1/6)*(k1 + 2*(k2 + k3) + k4);
end;

% Gather the data
V = [x;y];

%Make Table
T = array2table(transpose(V),... 
    'VariableNames', {'x_values', 'y_values'})

% Plot the curve
plot(x,y)
title('Runge-Kutta Method')
