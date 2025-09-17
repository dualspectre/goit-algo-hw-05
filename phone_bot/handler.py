import re

# Regular expression pattern for validating phone numbers
pattern = r"^[+]?\d{9,12}$"

# Decorator for handling input errors in function parse_input
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("No command entered. Please enter the command correctly.\
                  \nDetails: add <name> <phone>, change <name> <phone>, phone <name>")
            return "", ""
    return inner

#function of parsing user input command
@input_error
def parse_input(user_input): 
    """
    Parses the user input command and returns the command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Decorator for handling input errors in function add_contact
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Usage: add <name> <phone>"
    return inner

#function of adding a contact
@input_error
def add_contact(args, contacts: dict) -> str:
    """
    Adds a new contact to the contacts dictionary.
    Input: args - list of arguments, contacts - dictionary of contacts

    Return: bool - True if contact was added, False otherwise
    """
    name, phone = args
    condition = bool(re.fullmatch(pattern, phone))
    if condition:
        if name in contacts:
            return "Contact already exists."
        else:
            contacts[name] = phone
            return "Contact added."
    else:
        return "Invalid phone number format. Please use a valid format (9-12 digits)."

# Decorator for handling input errors in function change_contact
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Usage: change <name> <phone>"
        except KeyError:
            return "Contact not found."
    return inner

#function of changing a contact
@input_error
def change_contact(args, contacts: dict) -> str:
    """
    Changes an existing contact in the contacts dictionary.
    Input: args - list of arguments, contacts - dictionary of contacts

    Return: str - status of change operation
    """
    
    name, phone = args            
    condition = bool(re.fullmatch(pattern, phone))
    if condition:
        if name not in contacts:
            raise KeyError
        else:
            contacts[name] = phone
            return "Contact changed."
    else:
        return "Invalid phone number format. Please use a valid format (9-12 digits)."

# Decorator for handling input errors in function show_phone_number
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return "Usage: phone <name>"
        except KeyError:
            return "Contact not found."
    return inner

#function of showing a contact's phone number
@input_error
def show_phone_number(args, contacts: dict) -> str:
    """
    Shows a contact's phone number.
    Input: args - list of arguments, contacts - dictionary of contacts

    Return: str - the contact's phone number or an error message
    """
    name = args[0]
    return f"{name}: {contacts[name]}"
    

#function of showing all contacts
def show_all_contacts(contacts: dict) -> str:
    """
    Shows all contacts in the contacts dictionary.
    Input: contacts - dictionary of contacts

    Return: str - all contacts or an error message
    """
    if not contacts:
        return "No contacts found."
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()