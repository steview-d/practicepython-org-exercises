birthday_dict = {
    "Person A":"01/01/1960",
    "Person B":"01/01/1970",
    "Person C":"01/01/1980",
    "Person D":"01/01/1990",
}

print("Welcome to the Birthday Dictionary!")
print("\nWe have the following birthdays stored:")
for name in birthday_dict:
    print(name)

user_input = str(input("\nPlease enter a name > "))
bday = birthday_dict.get(user_input, "not listed")
print("{}'s birthday is {}".format(user_input, bday))