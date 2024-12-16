from views.cli_view import main_menu
from views.gui_view import start_gui

def main():
    print("Choose interface:")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")

    choice = input("Enter your choice: ")

    if choice == "1":
        main_menu()  # Ejecuta la vista CLI
    elif choice == "2":
        start_gui()  # Ejecuta la vista GUI
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
