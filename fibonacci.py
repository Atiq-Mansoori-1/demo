def generate_fibonacci(n):
    """
    Generate a Fibonacci series up to n terms.
    
    Args:
        n (int): Number of Fibonacci terms to generate
    
    Returns:
        list: A list of Fibonacci numbers
    """
    # Handle edge cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the Fibonacci series
    fib_series = [0, 1]
    
    # Generate subsequent Fibonacci numbers
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    
    return fib_series

def print_fibonacci(n):
    """
    Print the Fibonacci series up to n terms.
    
    Args:
        n (int): Number of Fibonacci terms to print
    """
    fibonacci_numbers = generate_fibonacci(n)
    print(f"Fibonacci Series ({n} terms):")
    for num in fibonacci_numbers:
        print(num, end=" ")
    print()  # New line at the end

# Example usage
if __name__ == "__main__":
    # Generate and print Fibonacci series for different lengths
    print_fibonacci(10)
    print_fibonacci(15)
