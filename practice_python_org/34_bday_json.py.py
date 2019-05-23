import json

def write_json():
    with open ('assets/bdays.json', 'w') as f:
        json.dump(birthday_dict, f)


def show_bday():
    user_input = str(input("\nPlease enter a name > "))
    bday = birthday_dict.get(user_input, "not listed")
    print("{}'s birthday is {}".format(user_input, bday))


def add_bday():
    name = str(input("Whose birthday would you like to add? > "))
    bday = str(input("And when where they born (dd/mm/yyyy)? > "))
    birthday_dict[name] = bday
    write_json()


birthday_dict = {
    "Person A":"01/01/1960",
    "Person B":"01/01/1970",
    "Person C":"01/01/1980",
    "Person D":"01/01/1990",
}

write_json()

print("Welcome to the Birthday Dictionary!")
print("\nWe have the following birthdays stored:")
for name in birthday_dict:
    print(name)
