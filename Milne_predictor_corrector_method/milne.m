% -------------MATLAB Code--------------------------
% The following is the algorithm to determine
% solution of a user-defined differential equation
% using the Milne's predictor-corrector method
% given the initial conditions and using the 
% data obtained to plot the curve of the function y(x)
% -------------------------------------------------

% User defines the function.
a    = input('Enter the function function whose left hand side is dy/dx :', 's');
df   = @(x,y)(eval(a));

x4 = input('Enter the value of x at which the solution is required :');		

% This is the code to get the values of function y at different values of x

x_val = input('Enter the different values of x in order in square brackets'); % enter the x values as (1 X 3) array

y_val = input('Enter the different values of y in order in square brackets'); % enter the y values as (1 X 3) array

C = cat(1,x_val,y_val); % Concatenate the above two arrays to form a (3 X 3) array

% Code to write the information entered by user as a table

fprintf('The following are the X values and corresponding Y values entered by you :')

T = array2table(transpose(C),...	 
    'VariableNames',{'X','Y'})

% Obtain the value of h

h = x_val(2) - x_val(1);

% THE FOLLOWING IS THE ALGORITHM FOR MILNE'S PREDICTOR FORMULA

% The following are the values of f0, f1, f2 and f3

f0 = df(x_val(1),y_val(1));
f1 = df(x_val(2),y_val(2));
f2 = df(x_val(3),y_val(3));
f3 = df(x_val(4),y_val(4));

% Next we get the corresponding value of x_sol at which solution is required

y4 = y_val(1) + (4*(h/3))*(2*f1 - f2 + 2*f3);

% Obtain the value of f4

f4 = df(x4,y4);

% THE FOLLOWING IS THE ALGORITHM FOR MILNE'S CORRECTOR FORMULA to improve the value of y4

y4_corrected = y_val(3) + (h/3)*(f2 + 4*f3 + f4);

fprintf('The value of y at given value of x = %4.3f\n is :',x4)
asnwer = y4_corrected