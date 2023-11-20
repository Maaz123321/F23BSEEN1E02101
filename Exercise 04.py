def check_first_last_equal(numbers):
    # Check if the first and last numbers are the same
    return numbers[0] == numbers[-1]

# Test cases
number_x = [10, 20, 30, 40, 10]
number_y = [75, 65, 35, 75, 30]

# Check for the first list (number_x)
if check_first_last_equal(number_x):
    print("The first and last numbers of number_x are the same.")
else:
    print("The first and last numbers of number_x are different.")

# Check for the second list (number_y)
if check_first_last_equal(number_y):
    print("The first and last numbers of number_y are the same.")
else:
    print("The first and last numbers of number_y are different.")
