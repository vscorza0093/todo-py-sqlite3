import main
import create_update_delete_category as category_manager
import create_update_delete_tasks as task_manager
import list_categories
import list_tasks
import conclude_task


def CreateUpdateDeleteOptions():
    print("\nCreate, Update, Delete")
    print("\nT - Tasks\nC - Categories")
    user_input = input().lower()
    match user_input:
        case 't':
            CreateUpdateDeleteTasks()
        case 'c':
            CreateUpdateDeleteCategories()
        case other:
            print("Invalid input")
            main.ApplicationLoop()


def CreateUpdateDeleteTasks():
    print("\nC - Create Task\nU - Update Task\nD - Delete Task")
    user_input = input().lower()
    print("\n")
    match user_input:
        case 'c':
            task_manager.GetNewTaskData()
        case 'u':
            task_manager.UpdateTaskByIdOrByName()
        case 'd':
            task_manager.DeleteTaskByIdOrByName()


def CreateUpdateDeleteCategories():
    print("\nC - Create Category\nU - Update Category\nD - Delete Category")
    user_input = input().lower()
    print("\n")
    match user_input:
        case 'c':
            category_manager.GetNewCategoryData()
        case 'u':
            category_manager.UpdateCategory()
        case 'd':
            category_manager.DeleteByIdOrByName()


def ListOptions():
    print("\nList options")
    print("T - List tasks\nC - List categories")
    user_input = input().lower()
    print("\n")
    match user_input:
        case 't':
            ListTasks()
        case 'c':
            ListCategories()


def ListTasks():
    print("\nList tasks\n")
    list_tasks.ListAllTasks()


def ListCategories():
    print("\nList categories\n")
    list_categories.ListAllCategories()


def ConcludeTasks():
    print("\nConclude tasks\n")
    conclude_task.ConcludeByIdOrByName()
