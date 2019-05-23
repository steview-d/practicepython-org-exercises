from datetime import datetime

user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

currentYear = datetime.now().year
birthYear = currentYear - user_age

print("Hi {}! You will be 100 years old in the year {}".format(user_name, (birthYear + 100)))