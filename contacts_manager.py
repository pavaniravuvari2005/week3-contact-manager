# Contact Management System
# Author: Pavani Ravuvari
# Week 3 – Functions & Dictionaries

import json
import re
from datetime import datetime

DATA_FILE = "contacts_data.json"

# ------------------ Helpers ------------------

def load_contacts():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def validate_phone(phone):
    digits = re.sub(r"\D", "", phone)
    return digits if 10 <= len(digits) <= 15 else None

# ------------------ CRUD Operations ------------------

def add_contact(contacts):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty")
        return

    phone = validate_phone(input("Phone: "))
    if not phone:
        print("Invalid phone number")
        return

    email = input("Email (optional): ").strip()
    group = input("Group (Friends/Work/Family): ").strip() or "Other"

    contacts[name] = {
        "phone": phone,
        "email": email,
        "group": group,
        "updated": datetime.now().isoformat()
    }
    save_contacts(contacts)
    print("✅ Contact added")

def search_contact(contacts):
    term = input("Search name: ").lower()
    found = False
    for name, info in contacts.items():
        if term in name.lower():
            print(f"\n{name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Group: {info['group']}")
            found = True
    if not found:
        print("No contacts found")

def update_contact(contacts):
    name = input("Enter name to update: ")
    if name not in contacts:
        print("Contact not found")
        return

    phone = validate_phone(input("New Phone: "))
    if phone:
        contacts[name]["phone"] = phone

    contacts[name]["updated"] = datetime.now().isoformat()
    save_contacts(contacts)
    print("✅ Contact updated")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("✅ Contact deleted")
    else:
        print("Contact not found")

def view_all(contacts):
    if not contacts:
        print("No contacts available")
        return

    for name, info in contacts.items():
        print(f"\n{name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Group: {info['group']}")

# ------------------ Menu ------------------

def main():
    contacts = load_contacts()

    while True:
        print("\nCONTACT MANAGEMENT SYSTEM")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            view_all(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
