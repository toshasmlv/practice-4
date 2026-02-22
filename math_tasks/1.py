import math

def degrees_to_radians(degrees):
    return degrees * math.pi / 180

# Get input from user
try:
    degrees = float(input("Input degree: "))
    
    # Convert to radians
    radians = degrees_to_radians(degrees)
    
    # Display result with 6 decimal places
    print(f"Output radian: {radians:.6f}")
    