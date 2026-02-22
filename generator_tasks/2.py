def even_number_generator(n):
    """Generator that yields even numbers from 0 to n"""
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Get input from console
try:
    n = int(input("Enter a number: "))
    
    # Create generator
    even_gen = even_number_generator(n)
    
    # Convert generator output to list and print as comma-separated
    even_numbers = list(even_gen)
    print(*even_numbers, sep=", ")
    
except ValueError:
    print("Please enter a valid integer")