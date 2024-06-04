# imports PersonalAssistant.py file
import json
from PersonalAssistant import PersonalAssistant

# ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    contact_list = json.load(contacts)
    assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

# print(assistant.birthdays)


while not done:
    user_command = input("""
    How can I help you?

    **** To-do List *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list

    **** Birthdays *****
    4: Get Birthday
    5: Add Birthday
    6: Remove Birthday

    **** Contacts *****
    7: Get Contact
    8: Add Contact
    9: Delete Contact

    Select a number or type 'Exit' to quit:

    """)

    match user_command.lower():
        # Add to do
        case "1":
            user_input = input("Add an item to your to-do list: ")
            assistant.add_todo(user_input)

        # Remove to do
        case "2":
            print(f"Your current to-do list: {assistant.get_todos()}")
            user_input = input("Pick an item to remove from your to-do list: ")
            print(f"\n {assistant.remove_todo(user_input)}")

        # Get to do list
        case "3":
            print("\nHere's your to-do list!")
            print(f"\n {assistant.get_todos()}")

        # Get birthday
        case "4":
            print("\nThis is your current list of birthdays:")
            for k, v in assistant.birthdays.items():
                print(f"\n{k}'s birthday is {v}")
            user_input = input(
                "\nSelect a name to display only their birthday: ")
            print(f"\n{user_input}'s birthday is \
                  {assistant.birthdays[user_input]}.")

        # Add a birthday
        case "5":
            name = input("To add a birthday, enter the name of the person: ")
            date = input(f"\nEnter {name}'s birthday (ex: 08/18/2000): ")
            print(f"\n {assistant.add_birthday(name, date)}")

        # Remove a birthday
        case "6":
            print("\nCurrent birthday list:")
            for k, v in assistant.birthdays.items():
                print(f"{k} -> {v}")
            user_input = input("Enter the name you would like to remove: ")
            print(f" {assistant.remove_birthday(user_input)}")

        # Get contact
        case "7":
            print(f"\nHere is your current Contact List")
            for k, v in assistant.contacts.items():
                # why am I displaying the value? the key should suffice
                print(f"\n {k} -> {v}")
            user_input = input("\nPlease enter the name of a contact: ")
            print(f"\n {assistant.get_contact(user_input)}")

        # Add a contact
        case "8":
            user_input_name = input(
                "\nPlease enter the name of your new contact: ")
            user_input_job = input(
                "Please enter the occupation of your new contact: ")
            print(f"{assistant.add_contact(user_input_name, user_input_job)}")

        # Delete a contact
        case "9":
            print(f"\nHere is your list of contacts:")
            for k, v in assistant.contacts.items():
                print(f"\n{k} -> {v}")
            user_input = input(
                "\nPlease enter the name of the contact you would like to remove: ")
            print(assistant.remove_contact(user_input))

        case "exit":
            done = True
            print("\nGoodbye,see you next time!")

        case _:
            print("\nNot a valid command.")

    # elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":


# ADD CODE: write data to JSON file
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
    json.dump(assistant.get_todos(), write_todos)
    json.dump(assistant.get_birthdays(), write_birthdays)
    json.dump(assistant.get_contacts(), write_contacts)
