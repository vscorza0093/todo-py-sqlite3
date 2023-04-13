import input_manager


def ApplicationTitle():
    print("\nWelcome to ToDo Application\n")


def ApplicationLoop():
    application_loop = True
    while application_loop:
        print("Main Menu")
        print("1 - Create, Update or Delete\n2 - List\n3 - Conclude task\n4 - Exit application")
        application_loop = input_manager.TestUserInput(input())
        print("\n")


if __name__ == '__main__':
    ApplicationTitle()
    ApplicationLoop()


