import random

def start_game():
    # Introduction and initial setup
    print("Welcome to the adventure game!")
    player_name = input("What is your character's name? ")
    player_health = 100
    player_attack = 10
    player_defense = 5
    player_inventory = []

    # Main game loop
    while True:
        # Display current location and available options
        print("You are currently in the forest.")
        print("1. Go north")
        print("2. Go south")
        print("3. Check inventory")
        print("4. Fight")
        print("5. Quit game")

        # Get player input and handle it
        choice = input("What would you like to do? ")
        if choice == "1":
            # Go north
            pass
        elif choice == "2":
            # Go south
            pass
        elif choice == "3":
            # Check inventory
            if len(player_inventory) == 0:
                print("Your inventory is empty.")
            else:
                print("Your inventory contains:")
                for item in player_inventory:
                    print(item)
        elif choice == "4":
            # Fight
            enemy_name = "Goblin"
            enemy_health = 30
            enemy_attack = 5
            enemy_defense = 2
            while enemy_health > 0 and player_health > 0:
                # Player turn
                print(f"{enemy_name} has {enemy_health} health.")
                print("1. Light attack (low damage, high chance of hitting)")
                print("2. Heavy attack (high damage, low chance of hitting)")
                player_choice = input("What would you like to do? ")
                if player_choice == "1":
                    hit_chance = random.randint(1,10)
                    if hit_chance <= 8:
                        player_damage = player_attack - enemy_defense
                        enemy_health -= player_damage
                        print(f"You hit {enemy_name} for {player_damage} damage.")
                    else:
                        print(f"You missed {enemy_name}.")
                elif player_choice == "2":
                    hit_chance = random.randint(1,10)
                    if hit_chance <= 4:
                        player_damage = player_attack * 2 - enemy_defense
                        enemy_health -= player_damage
                        print(f"You hit {enemy_name} for {player_damage} damage.")
                    else:
                        print(f"You missed {enemy_name}.")
                else:
                    print("Invalid choice. Please try again.")
                if enemy_health <= 0:
                    print(f"{enemy_name} is defeated!")
                    break
                # Enemy turn
                enemy_damage = enemy_attack - player_defense
                player_health -= enemy_damage
                print(f"{enemy_name} attacks you for {enemy_damage} damage.")
                print(f"Your health is {player_health}.")
                if player_health <= 0:
                    print("You died!")
                    break
        elif choice == "5":
            # Quit game
            print("Thank you for playing!")
            break
        else:
            # Invalid input
            print("Invalid choice. Please try again.")
    # End of the game 
    print("Game Over!")

# Start the game
start_game()