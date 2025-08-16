# Personal Contact Book Project

class Contact:
    def _init_(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def _str_(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactBook:
    def _init_(self):
        self.contacts = []

    # Add new contact
    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
        print("✅ Contact added successfully!")

    # Display all contacts
    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    # Search contact by name
    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                found = True
        if not found:
            print("❌ Contact not found.")

    # Update contact by name
    def update_contact(self, name, phone, email):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = phone
                contact.email = email
                print("✅ Contact updated successfully!")
                return
        print("❌ Contact not found.")

    # Delete contact by name
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("✅ Contact deleted successfully!")
                return
        print("❌ Contact not found.")


# Main program
book = ContactBook()

while True:
    print("\n--- Personal Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        book.add_contact(name, phone, email)

    elif choice == "2":
        book.display_contacts()

    elif choice == "3":
        name = input("Enter name to search: ")
        book.search_contact(name)

    elif choice == "4":
        name = input("Enter name to update: ")
        phone = input("Enter new Phone: ")
        email = input("Enter new Email: ")
        book.update_contact(name, phone, email)

    elif choice == "5":
        name = input("Enter name to delete: ")
        book.delete_contact(name)

    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")