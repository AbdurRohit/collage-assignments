import math

# 1. Function to determine the season
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'

# 2. Function to calculate slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'Undefined (Vertical line)'
    return (y2 - y1) / (x2 - x1)

# 3. Function to solve a quadratic equation
def solve_quadratic_eqn(a, b, c):
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

# 4. Function to print each element of a list
def print_list(lst):
    for item in lst:
        print(item)

# 5. Function to reverse a list using loops
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 6. Sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^(n+1)/n
def sum_series(n):
    total = 0.0
    for i in range(1, n + 1):
        total += (-1)**(i + 1) / i
    return total

# 7. Compute sin x using series up to n terms
def sin_series(x, n):
    x = math.radians(x)  # Convert to radians
    sin_x = 0
    for i in range(n):
        sign = (-1)**i
        sin_x += sign * (x**(2*i + 1)) / math.factorial(2*i + 1)
    return sin_x

# 8. Compute cos x using series up to n terms
def cos_series(x, n):
    x = math.radians(x)  # Convert to radians
    cos_x = 0
    for i in range(n):
        sign = (-1)**i
        cos_x += sign * (x**(2*i)) / math.factorial(2*i)
    return cos_x

# 9. Print pattern for N lines
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("/ \\ ", end="")
        print()
        for j in range(1, i + 1):
            print("/_\\ ", end="")
        print()

# 10. Display a number as 8-segment display
def display_segment(n):
    for i in range(1, n + 1):
        print("_ " * i)
        print("|_" * i)

# 11. Print matrix pattern up to N lines
def matrix_pattern(n):
    matrix = [[0] * n for _ in range(n)]
    start = 1
    for layer in range((n + 1) // 2):
        for i in range(layer, n - layer):
            matrix[layer][i] = start
            start += 1
        for i in range(layer + 1, n - layer):
            matrix[i][n - layer - 1] = start
            start += 1
        for i in range(n - layer - 2, layer - 1, -1):
            matrix[n - layer - 1][i] = start
            start += 1
        for i in range(n - layer - 2, layer, -1):
            matrix[i][layer] = start
            start += 1
    for row in matrix:
        print(" ".join(map(str, row)))

# 12. Print table
def print_table():
    for i in range(1, 6):
        print(f"{i} {1} {i} {i**2} {i**3}")

# Main method to call all the functions
if __name__ == "__main__":
    print("Season:", check_season('January'))
    print("Slope:", calculate_slope(2, 3, 4, 5))
    print("Quadratic equation solution:", solve_quadratic_eqn(1, -3, 2))
    print_list([1, 2, 3, 4])
    print("Reversed list:", reverse_list([1, 2, 3, 4]))
    print("Sum of series:", sum_series(5))
    print("Sine of x:", sin_series(30, 5))
    print("Cosine of x:", cos_series(30, 5))
    print("Pattern for N lines:")
    print_pattern(3)
    print("Segment display for N lines:")
    display_segment(3)
    print("Matrix pattern:")
    matrix_pattern(3)
    print("Table:")
    print_table()