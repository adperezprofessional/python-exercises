# Find the roots of the quadratic equation: ax2 + bx + c = 0
import math

def find_roots(a, b, c):
    # My Solution - Dave Perez
    formula1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    formula2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    result = (formula1, formula2)
    return result
    # My Solution - Dave Perez

print(find_roots(2, 10, 8));