import sympy as sp
import sys

significance = 8

############################################

def solver_differentiation(option: int):

    f = input("\nFunción? ")
    x = float(input("\nx? "))
    h = float(input("\nh? "))

    real_value = solver_differenciation_real_value(f, x)
    calculated_value = solver_differenciation_calculated_value(option, f, x, h)
    error = solver_differenciation_error(real_value, calculated_value)

    print("\nValor real: ", real_value)
    print("Valor calculado: ", calculated_value)
    print("Error: ", round(error, 2),"%")


def solver_differenciation_real_value(function: str, x: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(function)

    f_derivative = sp.diff(f, sy_x)
    evaluation = f_derivative.subs(sy_x, x)

    return round(evaluation, significance)


def solver_differenciation_error(real_value: float, calculated_value: float):

    error = abs((real_value - calculated_value)*(100)/real_value)

    return round(error, significance)


def solver_differenciation_calculated_value(option: int, f: str, x: float, h: float):

    def f_xi_h(times: int):
        return round(f.subs(sy_x, x+h*times), significance)

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

    return round(formula_result, significance)

############################################

def solver_integration(option: int):

    f = input("\nFunción? ")
    x = float(input("\nx? "))
    h = float(input("\nh? "))

    real_value = solver_integration_real_value(f, x)
    calculated_value = solver_integration_calculated_value(option, f, x, h)
    error = solver_integration_error(real_value, calculated_value)

    print("\nValor real: ", real_value)
    print("Valor calculado: ", calculated_value)
    print("Error: ", round(error, 2),"%")


def solver_integration_real_value(function: str, x: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(function)

    f_derivative = sp.diff(f, sy_x)
    evaluation = f_derivative.subs(sy_x, x)

    return round(evaluation, significance)


def solver_integration_error(real_value: float, calculated_value: float):

    error = abs((real_value - calculated_value)*(100)/real_value)

    return round(error, significance)


def solver_integration_calculated_value(option: int, f: str, x: float, h: float):

    def f_xi_h(times: int):
        return round(f.subs(sy_x, x+h*times), significance)

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


