
# Function to calculate the square root of a number using Newton's method
def newton_sqrt(n, tolerance=1e-7):
    x = n  # Initial guess
    while True:
        root = 0.5 * (x + (n / x))
        # Check for convergence within the tolerance
        if abs(root - x) < tolerance:
            return root
        x = root

# Test case and expected output:
# Square root of 16 is 4.0
print("Square root of 16:", newton_sqrt(16))
