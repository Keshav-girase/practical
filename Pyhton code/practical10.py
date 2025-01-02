
def overloaded_function(*args):
    if len(args) == 1:
        return f"Single argument: {args[0]}"
    elif len(args) == 2:
        return f"Two arguments: {args[0]}, {args[1]}"
    else:
        return "Invalid number of arguments"

# Test cases
print(overloaded_function(10))
print(overloaded_function(20, 30))
