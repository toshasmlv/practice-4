import math

def regular_polygon_area(n_sides, side_length):
    return (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))

# Get input from user
try:
    n_sides = int(input("Input number of sides: "))
    side_length = float(input("Input the length of a side: "))
    
    # Validate inputs
    if n_sides < 3:
        print("A polygon must have at least 3 sides")
    elif side_length <= 0:
        print("Side length must be positive")
    else:
        # Calculate area
        area = regular_polygon_area(n_sides, side_length)
        
        # Display result
        print(f"The area of the polygon is: {area}")
        
except ValueError:
    print("Please enter valid numbers")