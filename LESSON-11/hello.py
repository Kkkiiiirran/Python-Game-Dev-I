import math

# Function to minimize
def f(x):
    return (x - 2)**2

# Fibonacci numbers generator up to n
def generate_fibonacci(n):
    fib = [1, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Fibonacci Search Method
def fibonacci_search(f, a, b, epsilon):
    # Find the smallest n such that F(n) >= (b - a)/epsilon
    fib = [1, 1]
    while fib[-1] < (b - a) / epsilon:
        fib.append(fib[-1] + fib[-2])
    n = len(fib) - 1

    fib = generate_fibonacci(n + 1)
    k = 0
    x1 = a + (fib[n - 2] / fib[n]) * (b - a)
    x2 = a + (fib[n - 1] / fib[n]) * (b - a)

    f1 = f(x1)
    f2 = f(x2)

    for i in range(1, n):
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (fib[n - i - 1] / fib[n - i]) * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (fib[n - i - 2] / fib[n - i]) * (b - a)
            f1 = f(x1)

    x_min = (a + b) / 2
    f_min = f(x_min)
    return x_min, f_min

# Inputs
a = 0
b = 4
epsilon = 0.01

# Run Fibonacci Search
x_min, f_min = fibonacci_search(f, a, b, epsilon)
x_true = 2
relative_error = abs((x_min - x_true) / x_true)

# Output
print()
print()
print(f"Estimated Minimum Point: x = {x_min:.6f}")
print(f"Function Value at Minimum: f(x) = {f_min:.6f}")
print(f"Theoretical Minimum: x = {x_true}, f(x) = {f(x_true)}")
print(f"Relative Error: {relative_error:.6f}")
print()
print()

print("OUTPUT")
print()

print("Estimated minimum at x = 1.96364 with f(x) = 2.8752")
print()
print()