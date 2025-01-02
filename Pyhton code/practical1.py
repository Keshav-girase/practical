
import math

# Function to calculate the Greatest Common Divisor (GCD) of two numbers
def calculate_gcd(a, b):
    return math.gcd(a, b)

# Test cases and expected output:
# GCD of 60 and 48 is 12
# GCD of 0 and 48 is 48
# GCD of -60 and 48 is 12

print("GCD of 60 and 48:", calculate_gcd(60, 48))
print("GCD of 0 and 48:", calculate_gcd(0, 48))
print("GCD of -60 and 48:", calculate_gcd(-60, 48))
