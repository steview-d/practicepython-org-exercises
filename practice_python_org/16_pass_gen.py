import random

pw_len, upper, lower, numbers, symbols = 8, 1, 1, 1, 1
stored_pw = []
pw_list_upper = "QAZXSWEDCVFRTGBNHYUJMKIOLP"
pw_list_lower = "polmkiujnbhytgvcfredxzswqa"
pw_list_numbers = "1234567890"
pw_list_symbols = '!"£$%^&*()_+][}{;@#:~?><,./\|'


def generate_password(source, pass_length):
    """Generate a password
    source is the list of chars to choose from
    length is the number of chars in the password"""
    
    new_pw = ''
    for x in range(pass_length):
        new_pw += random.choice(source)
    stored_pw.append(new_pw)
    return new_pw


def make_char_list(mcl_upper, mcl_lower, mcl_numbers, mcl_symbols):
    """Generate a string with all available chars to choose from
    based on the users requirements"""
    # This can all definitely be shortened & cleaned up
    new_char_list = ""
    if mcl_upper:
        new_char_list += pw_list_upper
    if mcl_lower:
        new_char_list += pw_list_lower
    if mcl_numbers:
        new_char_list += pw_list_numbers
    if mcl_symbols:
        new_char_list += pw_list_symbols
    return new_char_list


def draw_screen():
    print("*** PASSWORD GENERATOR {} ***".format("v0.1"))
    print("-------------------------------\n")
    print("1. Generate password(s) with current settings\n"
          "2. Change settings\n"
          "3. Display stored passwords\n"
          "4. Exit program\n")
    # Print out current settings
    print("\nCurrent Settings\n"
          "----------------")
    print("Password length to generate: {}".format(pw_len))
    print("Use UPPER case characters: {}".format("Yes" if upper == 1 else "No"))
    print("Use LOWER case characters: {}".format("Yes" if lower == 1 else "No"))
    print("Use NUMBERS: {}".format("Yes" if numbers == 1 else "No"))
    print("Use SYMBOLS: {}".format("Yes" if symbols == 1 else "No"))


char_list = make_char_list(upper, lower, numbers, symbols)

while True:
    draw_screen()
    u_input = input("\nPlease choose an option from above ")
    if u_input == "q" or u_input == "4":
        break
    if u_input == "1":
        pw = (generate_password(char_list, pw_len))
        print("Your new password is \n\n{}".format(pw))
        input("\n(enter to continue)")
    if u_input == "2":
        pw_len = int(input("How many characters should the password contain?"))
        _ = input("Use UPPER case characters? [y]es or [n]o? ")
        if _ == "y" or _ == "yes":
            upper = 1
        else:
            upper = 0
        _ = input("Use LOWER case characters? [y]es or [n]o? ")
        if _ == "y" or _ == "yes":
            lower = 1
        else:
            lower = 0
        _ = input("Use NUMBERS? [y]es or [n]o? ")
        if _ == "y" or _ == "yes":
            numbers = 1
        else:
            numbers = 0
        _ = input("Use SYMBOLS? [y]es or [n]o? ")
        if _ == "y" or _ == "yes":
            symbols = 1
        else:
            symbols = 0
        char_list = make_char_list(upper, lower, numbers, symbols)
        input("\n(enter to continue)")
    if u_input == "3":
        print("The following passwords have been stored:\n")
        for _ in stored_pw:
            print(_)
        input("\n(enter to continue)")

"""
Could go to town on this and really expand. Think Dashlane pw gen - simulate that, in Python
Features List
* Password Length
* Password Content Choice, so - upper / lower case, numbers, symbols
* Store previously generated passwords
* Use a dict to store password and site / program name
* Allow possibility of password containing multiple same chars
"""