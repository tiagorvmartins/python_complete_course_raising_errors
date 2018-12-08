# wrong version
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using a default value 0')
        return 0
    finally:
        n_square = n ** 2
        return n_square



# good version
def power_of_two2():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
        n_square = n ** 2
        return n_square
    except ValueError:
        print('Your input was invalid. Using a default value 0')
        return 0

print(power_of_two2())
print(power_of_two2())