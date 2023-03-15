# Math Function Plotter
#### Video Demo:  <https://prezi.com/v/view/tZmUU5TmkK2gOyWWn0Pq/>
#### Description: My final project is a code that provides graphics of mathematical functions and can be used by high school students to study analytic geometry. To do this, it uses two libraries: numpy and pyplot from matplotlib. Numpy is used for mathematical operations, while pyplot is used to generate graphics.

The code works from the "Main" function, which directs the user through the steps of selecting a mathematical function and determining the values used in each of them.

First, the "main" function calls the "get_function" function, which prompts the user to select one of the following 9 mathematical functions:

1 - Linear
2 - Quadratic
3 - Sinusoidal
4 - Polynomial
5 - Cosinusoidal
6 - Exponential
7 - Constant
8 - Logarithmic
9 - Modular

After the user selects the desired mathematical function, "get_function" returns the corresponding numerical value to the "num" variable. Then, the "main" function calls the "Function_select" function, which takes "num" as an argument, containing the selected function.

Based on the argument provided, the "Function_select" function will call the corresponding Python function for the selected mathematical function in "get_function". Depending on the choice made by the user, the selected function may require certain attributes, such as indicating values for a, b, and c for quadratic functions or indicating the polynomial order for polynomial functions.

As a result, with the selection of the required values by the code, the selected function will return two arrays, X and y, respectively, which will be used as a basis for creating the graph of the chosen function. The x array is standard for all functions and is defined as "x = np.arange(-100,100,0.1)" within "Function_select" and serves as an argument for all functions, except for logarithmic and modular functions due to mathematical issues. On the other hand, the values of the y array are defined within the mathematical functions and depend on the nature of the function.

Finally, the values of X and Y returned for the mathematical functions, which are now within the scope of "Function_select", are returned to the main function, which will use these values in the pyplot functions to generate the graph with a title and present it on the user's screen.

It is important to note that my program does not intend to save images; therefore, options to save images to directories or display dialog windows were disregarded in development, as the goal is to visualize the graph's sketch, not to use it in other environments.

The code, in the "get_function" function, rejects values that are not within the integer range of 1-9. So, suppose the user makes an error and types "first degree function" instead of 1 for the same function: the program will reject the input string and repeat the prompt. The same thing will happen in the selection of numerical values for functions such as the quadratic function. Therefore, if any of the constants in the function ax²+bx+c are invalid, the system will reject the input and prompt the user to enter the value again.
