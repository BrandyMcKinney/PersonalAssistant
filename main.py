#imports PersonalAssistant.py file
import json
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    contact_list = json.load(contacts)
    assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

#print(assistant.birthdays)


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
  
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
      
    # Get Birthday
    elif user_command == "4":
        print("\nCurrent birthday list:")
        for k,v in assistant.birthdays.items():
          print(f"\n{k} -> {v}")
        
        user_input = input("\nSelect a name to display only their birthday: ")
        print(f"\n{user_input}'s birthday is {assistant.birthdays[user_input]}.")
    # Add Birthday
    elif user_command == "5":
        print("\nAdd a birthday")
        name = input("Enter the name of the person: ")
        date = input(f"\nEnter {name}'s birthday (ex: 08/18/2000): ")
        print(f"\n {assistant.add_birthday(name, date)}")
    # Remove Birthday
    elif user_command == "6":
        print("\nCurrent birthday list:")
        for k,v in assistant.birthdays.items():
          print(f"{k} -> {v}")
          
        user_input = input("Enter the name you would like to remove: ")
        print(f" {assistant.remove_birthday(user_input)}")
    # Get Contact
    elif user_command == "7":
        print(f"\nYour Contact List")
        for k,v in assistant.contacts.items():
            print(f"\n {k} -> {v}")

        user_input =input("\nPlease enter the name of a contact: ")
        print(f"\n {assistant.get_contact(user_input)}")

    elif user_command == "8":
        user_input_name = input("\nPlease enter the name of your new contact: ")
        user_input_job = input("Please enter the occupation of your new        contact: ")
        print(f"{assistant.add_contact(user_input_name, user_input_job)}")

    elif user_command == "9":
        print(f"\nYour Contact List:")
        for k,v in assistant.contacts.items():
          print(f"\n{k} -> {v}")
        user_input = input("\nPlease enter the name of the contact you would   like to remove: ")
        print(assistant.remove_contact(user_input))

  
    elif user_command == "exit" or user_command == "Exit" or user_command ==           "EXIT":
        done = True
        print("\nGoodbye, see you next time!")
    else:
        print("\nNot a valid command.")


# ADD CODE: write data to JSON file

with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
    json.dump(assistant.get_todos(), write_todos)
    json.dump(assistant.get_birthdays(), write_birthdays)
    json.dump(assistant.get_contacts(), write_contacts)
