# 1. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 2. Swap two numbers
def swap_numbers(a, b):
    return b, a

# 3. Check if a year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 4. Display reverse of a number
def reverse_number(num):
    return int(str(num)[::-1])

# 5. Find factors of a given number
def find_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

# 6. Generate prime number series up to n
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

# 7. Display numbers divisible by 7 but not multiple of 5 between 1000 and 2000
def divisible_by_7_not_5():
    return [num for num in range(1000, 2001) if num % 7 == 0 and num % 5 != 0]

# 8. Check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# 9a. Check if a number is perfect
def is_perfect_number(num):
    return sum(i for i in range(1, num) if num % i == 0) == num

# 9b. Check if a number is Armstrong
def is_armstrong_number(num):
    return sum(int(digit) ** len(str(num)) for digit in str(num)) == num

# 10. Generate Fibonacci series up to n
def fibonacci_series(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Example usage
if __name__ == "__main__":
    print(f"1. 25°C to Fahrenheit: {celsius_to_fahrenheit(25)}")
    print(f"2. Swap 5 and 10: {swap_numbers(5, 10)}")
    print(f"3. Is 2024 a leap year? {is_leap_year(2024)}")
    print(f"4. Reverse of 12345: {reverse_number(12345)}")
    print(f"5. Factors of 24: {find_factors(24)}")
    print(f"6. Prime numbers up to 20: {generate_primes(20)}")
    print(f"7. Numbers divisible by 7 but not 5 between 1000 and 2000: {divisible_by_7_not_5()}")
    print(f"8. Is 12321 a palindrome? {is_palindrome(12321)}")
    print(f"9a. Is 28 a perfect number? {is_perfect_number(28)}")
    print(f"9b. Is 153 an Armstrong number? {is_armstrong_number(153)}")
    print(f"10. Fibonacci series up to 10 terms: {fibonacci_series(10)}")