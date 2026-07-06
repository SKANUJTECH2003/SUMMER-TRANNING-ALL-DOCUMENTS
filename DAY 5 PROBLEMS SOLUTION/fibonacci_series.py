# Program to print the Fibonacci series up to n terms

def print_fibonacci(n):
    a, b = 0, 1
    
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(f"Fibonacci series up to {n} term:")
        print(a)
    else:
        print(f"Fibonacci series up to {n} terms:")
        i = 0
        while i < n:
            print(a, end=" ")
            a, b = b, a + b
            i += 1
        print()  # For a new line at the end

# Change this value to print more or fewer terms
terms = int(input("Enter the number of terms for the Fibonacci series: "))
print_fibonacci(terms)