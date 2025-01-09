def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            item = input("what item would you like to add")
            if item:
                shopping_list.append(item)
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("what item would you like to remove")
            shopping_list.remove(remove_item)
        elif choice == '3':
            # Display the shopping list
            for elements in shopping_list:
                print(i)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
