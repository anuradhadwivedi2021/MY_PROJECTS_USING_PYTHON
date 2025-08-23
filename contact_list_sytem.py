contacts = {}

def add_contact(name, number):
    contacts[name] = number

def view_contacts():
    for name, number in contacts.items():
        print(name, ":", number)

while True:
    choice = input("1.Add 2.View 3.Exit: ")
    if choice == "1":
        n = input("Name: ")
        num = input("Number: ")
        add_contact(n, num)
    elif choice == "2":
        view_contacts()
    else:
        break