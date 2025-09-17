import handler

def main():
    print("Welcome to the Phone Bot!")
    contacts = {}

    while True:
        user_input = input("Please enter a command: ")
        
        cmd, *args = handler.parse_input(user_input)

        # Command handling
        if cmd in ["exit", "close"]:
            print("Good bye!")
            break
            # hello command actions
        elif cmd == "hello":
            print("Hello! Can i help you")
        
        # add command actions
        elif cmd == "add":
            print(handler.add_contact(args, contacts))
        
        # change command actions                
        elif cmd == "change":
            print(handler.change_contact(args, contacts))
                
            # phone command actions
        elif cmd == "phone":
            print(handler.show_phone_number(args, contacts))
        
        # all command actions
        elif cmd == "all":
            print(handler.show_all_contacts(contacts))
            
            # help command actions
        elif cmd == "help":
            print("\nAvailable commands: add, change, phone, all, exit, close\
                \nadd <name> <phone> - add a new contact\
                \nchange <name> <phone> - change an existing contact\
                \nphone <name> - show a contact's phone number\
                \nall - show all contacts\
                \nclose, exit - close the application\
                \n<phone> must have 9-12 digits and can started with +")
        
        # unknown command actions
        else:
            print("Unknown command")
        

if __name__ == "__main__":
    main()
