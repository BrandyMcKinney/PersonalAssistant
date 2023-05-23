class PersonalAssistant:
    def __init__(self, todos, birthdays, contacts):
        
        self.todos = todos
        self.birthdays = birthdays
        self.contacts = contacts
      
    """To-do List"""      
    def add_todo(self, new_item):
        self.todos.append(new_item)

    def remove_todo(self, todo_item):
        if todo_item in self.todos:
            # Get the todo_item index in list
            index = self.todos.index(todo_item)
            # pop the index for todo_item in todos list
            self.todos.pop(index)
        else:
            return "Todo is not in list!"

    def get_todos(self):
        return self.todos
      
    """Birthdays"""      
    def get_birthdays(self):
        return self.birthdays

    def get_birthday(self, name):
        if name in self.birthdays:
          return f"{name}'s birthday is on {self.birthdays[name]}."
        else:
          return "The birthday for the given name could not be found"

    def add_birthday(self, name, date):
        if name in self.birthdays:
          return f"A birthday already exists for {name}."
        else:
          self.birthdays[name] = date
          return f"{name} has been added to your birthday list"
          
    def remove_birthday(self, name):
        if name in self.birthdays:
          self.birthdays.pop(name)
          return f"{name} has been removed."

    """Contacts """
    def get_contacts(self):
        return self.contacts

    def get_contact(self, name):
      if name in self.contacts:
        return f"Name: {name}\nOccupation: {self.contacts[name]}"
      else:
        return f"{name} is not in your contact list."

    def add_contact(self, name, job):
      if name not in self.contacts:
        self.contacts[name] = job
        return f"\n{name} has been added to your contacts."
      else:
        return f"\n{name} is already a contact."

    def remove_contact(self, name):
      if name in self.contacts:
        self.contacts.pop(name)
        return f"\n{name} has been removed from your contacts."

    



