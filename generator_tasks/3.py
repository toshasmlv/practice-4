def divisible_by_3_and_4_generator(n):
    """Generator that yields numbers divisible by both 3 and 4 from 0 to n"""
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Get input from console
try:
    n = int(input("Enter a number: "))
    
    # Create and use the generator
    result = list(divisible_by_3_and_4_generator(n))
    
    # Print the results
    print(f"Numbers divisible by both 3 and 4 between 0 and {n}:")
    print(*result, sep=", ")
    
    # Alternative: iterate through generator directly
    print("\nIterating through generator directly:")
    for num in divisible_by_3_and_4_generator(n):
        print(num, end=" ")
    print()
    
except ValueError:
    print("Please enter a valid integer")