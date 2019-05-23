import json
import  collections
from datetime import datetime

def read_json():
    with open ('assets/bdays.json', 'r') as f:
        bday_dict = json.load(f)
        return bday_dict


def write_json(bday_dict):
    with open ('assets/bdays.json', 'w') as f:
        json.dump(bday_dict, f)


def show_bday(bday_dict):
    user_input = str(input("\nPlease enter a name > "))
    bday = bday_dict.get(user_input, "not listed")
    print("{}'s birthday is {}".format(user_input, bday))


def add_bday(bday_dict):
    name = str(input("\nWhose birthday would you like to add? > "))
    bday = str(input("And when where they born (dd/mm/yyyy)? > "))
    bday_dict[name] = bday
    write_json(bday_dict)
    print("{} has been added".format(name))


def list_months(bday_dict):
    months = []
    for k, v in bday_dict.items():
        date = datetime.strptime(v, '%d/%m/%Y')
        months.append(datetime.strftime(date,'%B'))
    months = collections.Counter(months)
    print("These are the months that contain birthdays:")
    for k, v in months.items():
        print(k+':', v)


bday_dict = read_json()

print("Welcome to the Birthday Dictionary!")
print("\nWe have the following birthdays stored:")
for name in bday_dict:
    print(name)

while True:
    print("\nYou can do any one of the following")
    print(
        "1: Show stored birthdays\n"
        "2: Add a birthdays\n"
        "3: List birthday months\n"
        "0: Quit program")
    choice = str(input("What would you like to do? > "))
    if choice == '1':
        show_bday(bday_dict)
    if choice == '2':
        add_bday(bday_dict)
    if choice == '3':
        list_months(bday_dict)
    if choice == '0':
        break
