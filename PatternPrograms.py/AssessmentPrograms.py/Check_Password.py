def check_valid_password(passwordVal):
    capital_letter = False
    small_letter = False
    special_character = False

    if len(passwordVal) < 8:
        return False
    for val in passwordVal:
        ascii_value = ord(val)
        if ascii_value >=65 and ascii_value <= 90:
            capital_letter = True
        elif ascii_value >=97 and ascii_value <=122:
            small_letter = True
        elif not ((ascii_value>=48 and ascii_value <=57) or
              (ascii_value >=65 and ascii_value <= 90)or
               (ascii_value >=97 and ascii_value <=122)):
               special_character = True
    if capital_letter and small_letter and special_character:
        return True
    else:
        return False
def main():
    password = input("Enter your password: ")

    if check_valid_password(password):
        print("Password is valid.")
    else:
        print("Invalid password")

if __name__ == "__main__":
    main()

