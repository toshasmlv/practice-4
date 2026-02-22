def countdown(n):
    """
    Generator that yields numbers from n down to 0
    
    Args:
        n: starting number (must be >= 0)
    """
    for i in range(n, -1, -1):
        yield i

# Test the generator
print("Testing countdown generator:")
print("-" * 30)

# Test case 1: Standard countdown
print("Countdown from 5 to 0:")
for num in countdown(5):
    print(f"  {num}")

print()

# Test case 2: Countdown from 0
print("Countdown from 0 to 0:")
for num in countdown(0):
    print(f"  {num}")

print()

# Test case 3: Larger countdown (showing just a few)
print("Countdown from 10 to 0 (first few):")
counter = 0
for num in countdown(10):
    if counter < 5:  # Show first 5 numbers
        print(f"  {num}")
    counter += 1
print("  ...")

print()

# Interactive version
try:
    n = int(input("Enter a starting number: "))
    if n < 0:
        print("Please enter a non-negative number")
    else:
        print(f"\nCountdown from {n} to 0:")
        for num in countdown(n):
            print(num, end=" ")
        print()  # New line at the end
except ValueError:
    print("Please enter a valid integer")