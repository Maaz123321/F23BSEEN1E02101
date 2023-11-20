def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number [::-1]

num=125

if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
    