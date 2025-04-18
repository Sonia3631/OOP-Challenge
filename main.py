from pet import Pet

def pet_menu(pet):
    while True:
        print("\nWhat would you like to do with your pet?")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Train")
        print("5. Show Tricks")
        print("6. Get Status")
        print("7. Check Mood")
        print("8. Cuddle")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            food = input("What would you like to feed? (generic/treat): ")
            pet.eat(food)
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter a new trick: ")
            pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            pet.get_mood()
        elif choice == "8":
            pet.cuddle()
        elif choice == "9":
            print(f"Goodbye from {pet.name}! 🐾")
            break
        else:
            print("Invalid choice. Please select an option.")

# Create and interact with Snoopy
snoopy = Pet("Snoopy", pet_type="Beagle")
snoopy.get_status()

# Interactive pet menu
pet_menu(snoopy)