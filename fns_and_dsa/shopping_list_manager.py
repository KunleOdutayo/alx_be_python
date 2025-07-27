def shopping_list_manager():
    shopping_list = []

    while True:
        print("Shopping List Manager")
        print("1.Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # propmt for add item
            pass
        elif choice == '2':
            # prompt for remove item
            pass
        elif choice == '3':
            # Display shopping list
            pass
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    shopping_list_manager()