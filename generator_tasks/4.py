def squares(a, b):
    """
    Generator that yields the square of all numbers from a to b (inclusive)
    
    Args:
        a: starting number
        b: ending number
    """
    for i in range(a, b + 1):
        yield i ** 2

# Test the generator with a for loop
print("Testing squares generator:")
print("-" * 30)

# Test case 1: Positive numbers
print("Squares from 3 to 7:")
for square in squares(3, 7):
    print(f"  {square}")

print()  # Empty line

# Test case 2: Including negative numbers
print("Squares from -3 to 3:")
for square in squares(-3, 3):
    print(f"  {square}")

print()

# Test case 3: Single number
print("Squares from 5 to 5:")
for square in squares(5, 5):
    print(f"  {square}")

print()

# Test case 4: Zero range
print("Squares from 0 to 0:")
for square in squares(0, 0):
    print(f"  {square}")

print()

# Test case 5: Larger range (showing first few and last few)
print("Squares from 1 to 10 (all values):")
result = list(squares(1, 10))
print(f"  {result}")