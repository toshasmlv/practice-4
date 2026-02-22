def parallelogram_area(base, height):
    return base * height
# Get input from user
try:
    base = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    
    # Validate inputs
    if base <= 0 or height <= 0:
        print("Base and height must be positive numbers")
    else:
        # Calculate area
        area = parallelogram_area(base, height)
        
        # Display result
        print(f"Expected Output: {area}")
        