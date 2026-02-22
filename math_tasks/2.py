def trapezoid_area(height, base1, base2):
    """
    Calculate the area of a trapezoid
    
    Formula: Area = (1/2) × height × (base1 + base2)
    
    Args:
        height: height of the trapezoid
        base1: length of first base
        base2: length of second base
        
    Returns:
        area of the trapezoid
    """
    return (1/2) * height * (base1 + base2)

# Get input from user
try:
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    
    # Calculate area
    area = trapezoid_area(height, base1, base2)
    
    # Display result
    print(f"Expected Output: {area}")
    
