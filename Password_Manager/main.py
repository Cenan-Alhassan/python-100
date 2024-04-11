"""
You have a list of website names as variables, each containing the password

on start, verify password.
afterwards, choose: 1- display websites and passwords. 2- add new website or update available website (update function)
3- delete entry 4-change program password (enter old password)

When choosing 2 or 3, call random password generator (print to user) and update the value.
When choosing 3,  ask for name, apppend the name and update it's value

*In order to convert input string to variable:
x='buffalo'
exec("%s = %d" % (x,2))

*password is a random string between 10-15 which contains upper and lower case letters, numbers and symbols.
"""
def generatePassword(name):
    total = []
    nr_letters = int(input("\nHow many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    for i in range(0, nr_letters):
        total.append(random.choice(letters))

    for i in range(0, nr_symbols):
        total.append(random.choice(symbols))

    for i in range(0, nr_numbers):
        total.append(random.choice(numbers))

    random.shuffle(total)
    total = ''.join(total)

    print(f"\nThe password for {name} is: " + total)
    return total


# option 1 displaying entries (keys) and passwords (items)
def displayEntries():
    print(f"\nThere are currently {len(entries)} entries:")

    if len(entries) == 0:
        check = input("There are no entries. Would you like to add one? Y/N: ")
        match check.lower():
            case 'y':
                addOrUpdate()
            case 'n':
                print("Then why are you here?")
            case _:
                print("Incorrect input")

    count = 1
    for keys, values in entries.items():  # same as enumerate
        print(f"{count}- {keys}: {values}")
        count+=1

# option 2 add new website or update available website
def addOrUpdate():
    while True:
        checkEntry = input('''\nPress E to update an entry. If doesn't exist, entry will be added. To check current
entry list, enter letter C. To exit, enter X: ''')

        match checkEntry.lower():
            case 'c':
                displayEntries()
            case 'x':
                return
            case 'e':
                while True:
                    checkEntry = input("Enter name of entry: ")
                    checkIfRandom = input("Press 1 to generate a random password. Press 2 to input a password: ")
                    match checkIfRandom:
                        case '1':
                            password = generatePassword(checkEntry)
                            entries.update({checkEntry: password})
                            return
                        case '2':
                            password = input("Enter password: ")
                            entries.update({checkEntry: password})
                            return
                        case _:
                            print("Invalid input.")

            case _:
                print("Invalid input")


if __name__ == "__addOrUpdate__":
    addOrUpdate()


def delete():
    checkDelete = input("Password cannot be retrieved once deleted. Proceed? Y/N: ")
    match checkDelete.lower():
        case 'n':
            return
        case 'y':
            deleteName = input("Name of entry to delete: ")
            if entries.get(deleteName, "NULL") != 'NULL':
                del entries[deleteName]
                print(f"The entry \'{deleteName}\' has been deleted successfully.")
            else:
                print("Entry does not exist. Exiting.")



import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

entries = {'a': 5} #using dictionaries


def main():

    while True:

        systemPassword = "1234"
        checkSP = input("Enter password: ")
        if checkSP == systemPassword:
            print("Password is valid.\nWelcome to the Password Manager!")

            while True:
                mode = input('''\nPress 1 to display current entries.
Press 2 to add a new entry or update an existing one.
Press 3 to delete an entry.\nPress 4 to change system password.
Enter: ''')
                match mode:
                    case '1':
                        displayEntries()
                    case '2':
                        addOrUpdate()
                    case '3':
                        delete()
                    case _:
                        print("Invalid input")

        else:
            print("Invalid password. Try again.")


if __name__ == "__main__":
    main()

