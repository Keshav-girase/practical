
# Function to perform binary search in a sorted list
def binary_search(lst, key):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid  # Key found
        elif lst[mid] < key:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Key not found

# Test case and expected output:
# Key 45 is found at index 4
numbers = [12, 24, 32, 39, 45, 50, 54]
print("Key found at index:", binary_search(numbers, 45))
