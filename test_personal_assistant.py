from .personal_assistant import PersonalAssistant
import pytest
import json

# Sample data for tests generated from AI
# tasks_data = ["Buy groceries", "Finish report", "Walk the dog"]
# birthdays_data = {"Alice": "01/01/2000", "Bob": "02/15/2001"}
# contacts_data = {"Charlie": "Software Engineer", "David": "Data Scientist"}

# using real data from json file. this is repeating code from main.py though
with open("tasks.json", "r") as tasks, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
    task_list = json.load(tasks)
    birthday_list = json.load(birthdays)
    contact_list = json.load(contacts)


@pytest.fixture
def assistant():
    """Fixture to create a PersonalAssistant instance for testing."""
    # return PersonalAssistant(tasks_data.copy(), birthdays_data.copy(), contacts_data.copy())
    return PersonalAssistant(task_list, birthday_list, contact_list)


# Test add_task
@pytest.mark.smoke(reason="Add task functionality is important")
@pytest.mark.tasks_component
def test_add_task(assistant):
    assistant.add_task("Clean the house")
    assert "Clean the house" in assistant.get_tasks()


@pytest.mark.smoke(reason="Task list should not contain duplicates")
@pytest.mark.tasks_component
def test_add_task_duplicate(assistant):
    assistant.add_task("Buy groceries")
    assert assistant.get_tasks().count("Buy groceries") == 1  # Ensure no duplicates


@pytest.mark.smoke(reason="Input must be a string")
@pytest.mark.tasks_component
def test_add_task_invalid_type(assistant):
    with pytest.raises(TypeError) as excinfo:
        assistant.add_task(5)  # Expect a TypeError for non-string input
    assert "Task must be a string" in str(excinfo.value)
    print(f"\nEXCINFO: {excinfo.value} \
          \nEXCTYPE: {excinfo.type} \
          \nEXCTRACEBACK: {excinfo.traceback}\n")


# Test remove_task
@pytest.mark.smoke(reason="Delete task functionality is important")
@pytest.mark.tasks_component
def test_remove_task(assistant):
    assistant.remove_task("Finish report")
    assert "Finish report" not in assistant.get_tasks()


@pytest.mark.tasks_component
def test_remove_task_not_found(assistant):
    assert assistant.remove_task(
        "Go to the moon") == "The task is not in list!"


# Test get_tasks
@pytest.mark.smoke(reason="Fuctionality is important to prove task was added")
@pytest.mark.tasks_component
def test_get_tasks(assistant):
    assert assistant.get_tasks() == task_list


# Test add_birthday
@pytest.mark.smoke(reason="Add birthday fuctionality is important")
@pytest.mark.birthdays_component
def test_add_birthday(assistant):
    assistant.add_birthday("Emily", "03/28/1998")
    assert assistant.get_birthdays()["Emily"] == "03/28/1998"


@pytest.mark.smoke(reason="One birthdate per person")
@pytest.mark.birthdays_component
@pytest.mark.duplicates
def test_add_birthday_duplicate(assistant):
    assert assistant.add_birthday(
        "Brandy", "1/01/1985") == "A birthday already exists for Brandy."
    # changed the name from AI generated Alice to Brandy. Is this a real fix? How do I know?


# Test remove_birthday
@pytest.mark.smoke(reason="Delete birthday functionality is important")
@pytest.mark.birthdays_component
def test_remove_birthday(assistant):
    assistant.remove_birthday("Bob")
    assert "Bob" not in assistant.get_birthdays()


@pytest.mark.birthdays_component
def test_remove_birthday_not_found(assistant):
    assert assistant.remove_birthday(
        "Eve") == "The birthday for the given name could not be found"


# Test get_birthday
@pytest.mark.smoke(reason="Fuctionality is important to prove birthday was added")
@pytest.mark.birthdays_component
def test_get_birthday(assistant):
    assert assistant.get_birthday(
        "Brandy") == "Brandy's birthday is on 1/01/1985."
    # changed the name from Alice to Brandy, is it reading the acutal data?


@pytest.mark.birthdays_component
def test_get_birthday_not_found(assistant):
    assert assistant.get_birthday(
        "Frank") == "The birthday for the given name could not be found"


# Test add_contact
@pytest.mark.smoke(reason="Add contact functionality is important")
@pytest.mark.contacts_component
def test_add_contact(assistant):
    assistant.add_contact("Eve", "Web Developer")
    assert assistant.get_contacts()["Eve"] == "Web Developer"


@pytest.mark.smoke(reason="No duplicates")
@pytest.mark.contacts_component
def test_add_contact_duplicate(assistant):
    assert assistant.add_contact(
        "Anita", "Designer") == "\nAnita is already a contact."


# Test remove_contact
@pytest.mark.smoke(reason="Delete contact functionality is important")
@pytest.mark.contacts_component
def test_remove_contact(assistant):
    assistant.remove_contact("David")
    assert "David" not in assistant.get_contacts()


@pytest.mark.contacts_component
def test_remove_contact_not_found(assistant):
    assert assistant.remove_contact(
        # output must match remove_contact()
        "Grace") == "\nGrace is not in your contacts list."


# Test get_contact
@pytest.mark.smoke(reason="Fuctionality is important to prove contact was added")
@pytest.mark.contacts_component
def test_get_contact(assistant):
    assert assistant.get_contact(
        "Fieval") == "Name: Fieval\nOccupation: Cat"


@pytest.mark.contacts_component
def test_get_contact_not_found(assistant):
    assert assistant.get_contact(
        "Henry") == "Henry is not in your contact list."
