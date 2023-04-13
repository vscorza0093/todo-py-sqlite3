import main
import menu_manager


def TestUserInput(user_input):
    try:
        int_user_input = int(user_input)
        ValidUserInput(int_user_input)
    except ValueError:
        print("\nInvalid Input\n")
        InvalidUserInput()


def ValidUserInput(user_input):
    match user_input:
        case 1:
            menu_manager.CreateUpdateDeleteOptions()
        case 2:
            menu_manager.ListOptions()
        case 3:
            menu_manager.ConcludeTasks()
        case 4:
            print("\nThanks for using\n")
            exit()
        case other:
            print("\nInvalid Input\n")
            main.ApplicationTitle()
            main.ApplicationLoop()


def InvalidUserInput():
    main.ApplicationTitle()
    main.ApplicationLoop()

