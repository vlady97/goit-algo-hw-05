import re
from typing import Callable

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact found. Please try again."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return " Command format is incorrect."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact with name '{name}' already exists. Please choose another name."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error  
def change_contact(args,contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"New contact number {phone} is updated."
    else:
        return f"No name {name} is found in contacts."
    

@input_error
def show_phone(args,contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number for '{name}' is {contacts[name]}"
    else:
        return f"No name '{name}' is found in contacts."
    

@input_error
def show_all(contacts):
    if contacts:
        return contacts
    else:
        return "No contacts."
    
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


