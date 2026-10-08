def display_menu():
    print("\n" + "=" * 50)
    print(" YANG Network Device Configuration Manager")
    print("=" * 50)

    print("1. Create Device")
    print("2. List Devices")
    print("3. Get Device")
    print("4. Update Device")
    print("5. Delete Device")
    print("6. Exit")


def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n[CREATE] Device creation will be implemented later.")

        elif choice == "2":
            print("\n[READ] Device listing will be implemented later.")

        elif choice == "3":
            print("\n[READ] Device lookup will be implemented later.")

        elif choice == "4":
            print("\n[UPDATE] Device update will be implemented later.")

        elif choice == "5":
            print("\n[DELETE] Device deletion will be implemented later.")

        elif choice == "6":
            print("\nExiting application...")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()