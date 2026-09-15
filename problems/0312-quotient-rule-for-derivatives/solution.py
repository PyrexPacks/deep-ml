import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    polyg = np.polyder(g_coeffs)
    polyh = np.polyder(h_coeffs)

    g = np.polyval(g_coeffs, x)
    h = np.polyval(h_coeffs, x)
    gprime=np.polyval(polyg, x)
    hprime=np.polyval(polyh, x)

    return (gprime * h - g * hprime) / abs(h) **2
    

