import math

# 1. Sum of square root of any three numbers
def sum_of_square_roots(a, b, c):
    return math.sqrt(a) + math.sqrt(b) + math.sqrt(c)

# 2. Solve a quadratic equation ax^2 + bx + c = 0
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "Complex roots"

# 3. Find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 4. Various computations
def computations():
    results = {
        "5^8": 5 ** 8,
        "sqrt(400)": math.sqrt(400),
        "exp(5)": math.exp(5),
        "log(625, 5)": math.log(625, 5)
    }
    return results

# 5. Trigonometric computations
def trigonometry():
    results = {
        "sin(60 degrees)": math.sin(math.radians(60)),
        "cos(pi)": math.cos(math.pi),
        "sin(0.8660)": math.sin(0.8660254037844386),
        "tan(90 degrees)": "undefined" if math.isclose(math.cos(math.radians(90)), 0) else math.tan(math.radians(90))
    }
    return results

# 6. Sum function
def sum_function(x, y):
    return x + y

# 7. Reverse a given string
def reverse_string(s):
    return s[::-1]

# 8. Calculate power using recursion
def power_recursive(base, exp):
    if exp == 0:
        return 1
    return base * power_recursive(base, exp - 1)

# 9. Convert Decimal number to Binary
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# 10. Check if a number is Krishnamurthy number
def is_krishnamurthy(n):
    factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
    return n == sum(factorial(int(digit)) for digit in str(n))

# 11. Sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 12. Print multiplication table of a number
def multiplication_table(n):
    return [n * i for i in range(1, 11)]

# 13. Print first 6 terms of geometric sequence
def geometric_sequence(a, r, terms=6):
    return [a * r ** i for i in range(terms)]

# 14. Print series up to N terms: 1, 2, 6, 24, 120, 720...
def factorial_series(n):
    result = [1]
    for i in range(2, n + 1):
        result.append(result[-1] * i)
    return result

# 15. Calculate power without using exponentiation or pow()
def power_without_exp(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Main method to call all the functions
if __name__ == "__main__":
    print("Sum of square roots:", sum_of_square_roots(4, 9, 16))
    print("Quadratic solution:", solve_quadratic(1, -3, 2))
    print("GCD:", gcd(60, 48))
    print("Computations:", computations())
    print("Trigonometry:", trigonometry())
    print("Sum function:", sum_function(5, 3))
    print("Reversed string:", reverse_string("hello"))
    print("Power using recursion:", power_recursive(2, 3))
    print("Decimal to Binary:", decimal_to_binary(10))
    print("Is Krishnamurthy:", is_krishnamurthy(145))
    print("Sum of digits:", sum_of_digits(123))
    print("Multiplication table:", multiplication_table(5))
    print("Geometric sequence:", geometric_sequence(2, 3))
    print("Factorial series:", factorial_series(6))
    print("Power without exp:", power_without_exp(2, 3))