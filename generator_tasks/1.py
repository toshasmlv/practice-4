def square_generator(N):
    """Generator that yields squares from 0² up to N²"""
    for i in range(N + 1):
        yield i ** 2

# Usage
for square in square_generator(5):
    print(square)
# Output: 0, 1, 4, 9, 16, 25