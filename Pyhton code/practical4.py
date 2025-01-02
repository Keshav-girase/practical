
# Function to perform linear search in a list
def linear_search(lst, key):
    for i, value in enumerate(lst):
        if value == key:
            return i  # Return index if the key is found
    return -1  # Return -1 if the key is not found

# Test case and expected output:
# Key 45 is found at index 6
numbers = [2, 4, 56, 5, 7, 4, 45, 67]
print("Key found at index:", linear_search(numbers, 45))
