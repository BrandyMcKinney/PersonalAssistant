class PersonalAssistant:
    def __init__(self, tasks, birthdays, contacts):

        self.tasks = tasks
        self.birthdays = birthdays
        self.contacts = contacts

    """Task List"""

    def add_task(self, new_item):
        try:
            assert type(new_item) is str
            self.tasks.append(new_item)
        except AssertionError:
            raise TypeError("Task must be a string")

    def remove_task(self, task_item):
        if task_item in self.tasks:
            # Get the task_item index in list
            index = self.tasks.index(task_item)
            # pop the index for task_item in todos list
            self.tasks.pop(index)
        else:
            return "The task is not in list!"

    def get_tasks(self):
        return self.tasks

    """Birthdays"""

    def get_birthdays(self):
        return self.birthdays

    def get_birthday(self, name):
        if name in self.birthdays:
            return f"{name}'s birthday is on {self.birthdays[name]}."
        else:
            return "The birthday for the given name could not be found"

    def add_birthday(self, name, date):
        try:
            assert type(name) is str
            assert type(date) is str
            if name in self.birthdays:
                return f"A birthday already exists for {name}."
            else:
                self.birthdays[name] = date
                return f"{name} has been added to your birthday list"
        except:
            raise TypeError("Name and date must be a string")

    def remove_birthday(self, name):
        if name in self.birthdays:
            self.birthdays.pop(name)
            return f"{name} has been removed."
        else:
            return "The birthday for the given name could not be found"

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
        else:
            return f"\n{name} is not in your contacts list."
