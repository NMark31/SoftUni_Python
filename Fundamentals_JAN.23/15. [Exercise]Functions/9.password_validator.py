def is_long_enough(password):
    return 6 <= len(password) <= 10


def is_alphanumeric(password):
    return password.isalnum()


def has_two_digits(password):
    digit_count = 0
    for el in password:
        if el.isdigit():
            digit_count += 1

    return digit_count >= 2


def not_valid(password):
    errors = []
    valid = True

    if not is_long_enough(password):
        errors.append("Password must be between 6 and 10 characters")
        valid = False

    if not is_alphanumeric(password):
        errors.append("Password must consist only of letters and digits")
        valid = False

    if not has_two_digits(password):
        errors.append("Password must have at least 2 digits")
        valid = False

    if not valid:
        return errors


password_input = input()
errors = not_valid(password_input)

if errors:
    for err in errors:
        print(err)

else:
    print("Password is valid")

