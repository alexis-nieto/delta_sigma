import sympy as sp
import sys

sig_fig = 8

############################################

def solver_differentiation(option: int):

    f = input("\nFunción? ")
    x = float(input("\nx? "))
    h = float(input("\nh? "))

    real_value = solver_differenciation_real_value(f, x)
    estimated_value = solver_differenciation_estimated_value(option, f, x, h)
    error = solver_differenciation_error(real_value, estimated_value)

    print("\nValor real:", real_value)
    print("Valor estimado:", estimated_value)
    print("Error:", round(error, 2),"%")


def solver_differenciation_real_value(function: str, x: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(function)

    f_derivative = sp.diff(f, sy_x)
    evaluation = f_derivative.subs(sy_x, x)

    return round(evaluation, sig_fig)


def solver_differenciation_error(real_value: float, estimated_value: float):

    error = abs((real_value - estimated_value)*(100)/real_value)

    return round(error, sig_fig)


def solver_differenciation_estimated_value(option: int, f: str, x: float, h: float):

    def f_xi_h(times: int):
        return round(f.subs(sy_x, x+h*times), sig_fig)

    sy_x = sp.symbols('x')
    f = sp.sympify(f)

    f_xi = f.subs(sy_x, x)

    if option == 1:

        # Forward, First Derivative, O(h)
        
        formula_result = (f_xi_h(+1) - f_xi)/h

    elif option == 2:

        # Forward, First Derivative, O(h²)
        formula_result = (-f_xi_h(+2) + 4*f_xi_h(+1) - 3*f_xi)/(2*h)

    elif option == 3:
        
        # Forward, Second Derivative, O(h)
        formula_result = (f_xi_h(+2) - 2*f_xi_h(+1) + f_xi)/(h**2)

    elif option == 4:
        
        # Forward, Second Derivative, O(h²)
        formula_result = (-f_xi_h(+3) + 4*f_xi_h(+2) - 5*f_xi_h(+1) + 2*f_xi)/(h**2)

    elif option == 5:
        
        # Forward, Third Derivative, O(h)
        formula_result = (f_xi_h(+3) - 3*f_xi_h(+2) + 3*f_xi_h(+1) - f_xi)/(h**3)

    elif option == 6:
        
        # Forward, Third Derivative, O(h²)
        formula_result = (-3*f_xi_h(+4) + 14*f_xi_h(+3) - 24*f_xi_h(+2) + 18*f_xi_h(+1) - 5*f_xi)/(2*h**3)

    elif option == 7:
        
        # Forward, Fourth Derivative, O(h)
        
        formula_result = (f_xi_h(+4) - 4*f_xi_h(+3) + 6*f_xi_h(+2) - 4*f_xi_h(+1) + f_xi)/(h**4)

    elif option == 8:
        
        # Forward, Fourth Derivative, O(h²)
        
        formula_result = (-2*f_xi_h(+5) + 11*f_xi_h(+4) - 24*f_xi_h(+3) + 26*f_xi_h(+2) - 14*f_xi_h(+1) + 3*f_xi)/(2*h**4)

    elif option == 9:
        
        # Backward, First Derivative, O(h)
        
        formula_result = (f_xi - f_xi_h(-1))/h

    elif option == 10:
        
        # Backward, First Derivative, O(h²)
        
        formula_result = (3*f_xi - 4*f_xi_h(-1) + f_xi_h(-2))/(2*h)

    elif option == 11:
        
        # Backward, Second Derivative, O(h)
        
        formula_result = (f_xi - 2*f_xi_h(-1) + f_xi_h(-2))/(h**2)

    elif option == 12:
        
        # Backward, Second Derivative, O(h²)
        
        formula_result = (2*f_xi - 5*f_xi_h(-1) + 4*f_xi_h(-2) - f_xi_h(-3))/(h**2)

    elif option == 13:
        
        # Backward, Third Derivative, O(h)
        
        formula_result = (f_xi - 3*f_xi_h(-1) + 3*f_xi_h(-2) - f_xi_h(-3))/(h**3)

    elif option == 14:
        
        # Backward, Third Derivative, O(h²)
        
        formula_result = (5*f_xi - 18*f_xi_h(-1) + 24*f_xi_h(-2) - 14*f_xi_h(-3) + 3*f_xi_h(-4))/(2*h**3)

    elif option == 15:

        # Backward, Fourth Derivative, O(h)
        
        formula_result = (f_xi - 4*f_xi_h(-1) + 6*f_xi_h(-2) - 4*f_xi_h(-3) + f_xi_h(-4))/(h**4)

    elif option == 16:
        
        # Backward, Fourth Derivative, O(h²)
        
        formula_result = (3*f_xi - 14*f_xi_h(-1) + 26*f_xi_h(-2) - 24*f_xi_h(-3) + 11*f_xi_h(-4) - 2*f_xi_h(-5))/(h**4)

    elif option == 17:
        
        # Centered, First Derivative, O(h²)
        
        formula_result = (f_xi_h(+1) - f_xi_h(-1))/(2*h)

    elif option == 18:
        
        # Centered, First Derivative, O(h⁴)
        
        formula_result = (-f_xi_h(+2) + 8*f_xi_h(+1) - 8*f_xi_h(-1) + f_xi_h(-2))/(12*h)

    elif option == 19:
        
        # Centered, Second Derivative, O(h²)
        
        formula_result = (f_xi_h(+1) - 2*f_xi + f_xi_h(-1))/(h**2)

    elif option == 20:
        
        # Centered, Second Derivative, O(h⁴)
        
        formula_result = (-f_xi_h(+2) + 16*f_xi_h(+1) - 30*f_xi + 16*f_xi_h(-1) - f_xi_h(-2))/(12*h**2)

    elif option == 21:
        
        # Centered, Third Derivative, O(h²)
        
        formula_result = (f_xi_h(+2) - 2*f_xi_h(+1) + 2*f_xi_h(-1) - f_xi_h(-2))/(2*h**3)

    elif option == 22:
        
        # Centered, Third Derivative, O(h⁴)
        
        formula_result = (-f_xi_h(+3) + 8*f_xi_h(+2) - 13*f_xi_h(+1) + 13*f_xi_h(-1) - 8*f_xi_h(-2) + f_xi_h(-3))/(8*h**3)

    elif option == 23:
        
        # Centered, Fourth Derivative, O(h²)
        
        formula_result = (f_xi_h(+2) - 4*f_xi_h(+1) + 6*f_xi - 4*f_xi_h(-1) + f_xi_h(-2))/(h**4)

    elif option == 24:
        
        # Centered, Fourth Derivative, O(h⁴)
        
        formula_result = (-f_xi_h(+3) + 12*f_xi_h(+2) - 39*f_xi_h(+1) + 56*f_xi - 39*f_xi_h(-1) + 12*f_xi_h(-2) - f_xi_h(-3))/(12*h**4)

    else:
        print("\nError desconocido\n")
        sys.exit(2)

    return round(formula_result, sig_fig)

############################################

def solver_integration(option: int):

    f = input("\nFunción? ")
    a = float(input("\na? "))
    b = float(input("\nb? "))

    real_value = solver_integration_real_value(f, a, b)
    estimated_value = solver_integration_estimated_value(option, f, a, b, real_value)
    error = solver_integration_error(real_value, estimated_value)

    print("Valor real:", real_value)
    print("Valor estimado:", estimated_value)
    print("Error:", round(error, sig_fig),"%")


def solver_integration_real_value(function: str, a: float, b: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(function)

    definite_integral = sp.integrate(f, (sy_x, a, b))

    return round(definite_integral, sig_fig)


def solver_integration_error(real_value: float, estimated_value: float):

    error = abs((real_value - estimated_value)*(100)/real_value)

    return round(error, sig_fig)


def solver_integration_estimated_value(option: int, f: str, a: float, b: float, real_value: float):

    def f_(limit: int):
        return round(f.subs(sy_x, limit), sig_fig)

    sy_x = sp.symbols('x')
    f = sp.sympify(f)

    if option == 1:

        # Trapezoidal Rule
        formula_result = (b - a)*(f_(a) + f_(b))/2

    elif option == 2:

        # Trapezoidal Rule (Multiple Application)

        n = int(input("\nNúmero de intervalos inicial? "))

        h = (b - a)/n

        x_list = []

        for i in range(1, n):
           #print(f"x{i}: {a+h*i}")
           x_list.append(round(a+h*i, sig_fig))

        #print(x_list)

        formula_result = round((b - a)*(f_(a) + 2*sum(f_(i) for i in x_list) + f_(b))/(2*n), sig_fig)

    elif option == 3:
        
        # Trapezoidal Rule (Multiple Application AND Iterative)

        error = float(input("\nError? (Formato: 0.01 = 0.01%) "))

        n = int(input("\nNúmero de intervalos inicial? "))

        formula_result_list = []

        while True:

            h = (b - a)/n

            x_list = []

            for i in range(1, n):
                x_list.append(round(a+h*i, sig_fig))

            #print(x_list)

            formula_result_list.append((b - a)*(f_(a) + 2*sum(f_(i) for i in x_list) + f_(b))/(2*n))

            if solver_integration_error(real_value, formula_result_list[-1]) <= error:

                #todo: print_table(formula_result_list)

                print("\nIteraciones: ", len(formula_result_list))

                return round(formula_result_list[-1], sig_fig)

                break

            n += 1

    elif option == 4:
        pass

    elif option == 5:
        pass

    elif option == 6:
        pass

    elif option == 7:
        pass

    return round(formula_result, sig_fig)

