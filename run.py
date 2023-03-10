import random

def start_game():
    # Introduction and initial setup
    print("Welcome to the thrilling adventure game! You are about to embark on an epic journey filled with challenging tasks and mysterious obstacles. Your goal is to complete each task and overcome every obstacle in order to successfully complete the game. Are you ready for the adventure of a lifetime? Let's begin!")
    player_name = input("What is your name? ")
    print(f"Welcome {player_name} to the thrilling adventure game! You find yourself standing at the edge of a dense forest. As you look ahead, you notice a signpost that lists several tasks that must be completed before you can continue on your journey. The tasks range from solving puzzles to finding hidden objects, and each one will test your skills and determination. Are you ready to take on the challenges that lie ahead? Take a deep breath, and let the adventure begin!")
    choice = input("Are you ready to continue? Type 'yes' or 'no': ")
    if choice == 'yes':
        player_health = 75
        player_attack = 12
        player_defense = 6
        player_inventory = ["A healing potion"]
        print(f"Here is some valid information about your character: \n Health: {player_health}\n Attack: {player_attack}\n Defense: {player_defense}\n Inventory: {player_inventory}\n")
        input("Press any key to enter the woods: ")
    else:
        print("Thanks for playing! Have a good day!")
        return
    # Create a list of items that can be picked up
    items = ["sword","shield","potion","dagger","axe"]

    # Main game loop
    item_count = 1
    while True:
        # Display current location and available options
        print("Choose wisely before you continue, what do you want to do?")
        
        print("1. Fight enemy")
        print("2. Solve riddle")
        print("3. Check inventory")
        print("4. Look for items")
        print("5. Quit game")
        # Get player input and handle it
        choice = input("What would you like to do? ")
        if choice == "4":
            # Look for items
            if random.randint(1,2) == 1:
                item = random.choice(items)
                player_inventory.append(item)
                item_count += 1
                print(f"You found a {item}! It has been added to your inventory.")
            else:
                print("You didn't find any items.")
        elif choice == "1":
            # Check if player has collected enough items
            if item_count < 2:
                print("You need to collect at least 2 items before you can fight the enemy.")
                continue
            # Fight enemy
            print("Oh, no! You bumped into a nasty forest goblin, you must defeat it before you continue!")
            enemy_name = "The forest goblin"
            enemy_health = 35
            enemy_attack = 15
            enemy_defense = 8
            while enemy_health > 0 and player_health > 0:
                # Player turn
                print(f"{enemy_name} has {enemy_health} health.")
                print("1. Light attack (low damage, high chance of hitting)")
                print("2. Heavy attack (high damage, low chance of hitting)")
                player_choice = input("What would you like to do? ")
                if player_choice == "1":
                    hit_chance = random.randint(1,10)
                    if hit_chance <= 12:
                        player_damage = player_attack - enemy_defense
                        enemy_health -= player_damage
                        print(f"You hit {enemy_name} for {player_damage} damage.")
                    else:
                        print(f"You missed {enemy_name}.")
                    print(f"Your health is {player_health}")
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
                print(f"{enemy_name} hit you for {enemy_damage} damage.")
                print(f"Your health is now {player_health}")
                if player_health <= 0:
                    print("You've been killed. Game over.")
                    if 'potion' in player_inventory:
                            choice = input("You have a healing potion in your inventory. Would you like to drink it? Type 'yes' or 'no': ")
                    if choice == 'yes':
                            player_health = 75
                            player_inventory.remove('potion')
                            print("You have been resurrected and your health has been restored.")
                            continue
                    else:
                            print("Thanks for playing! Have a good day!")
                    return
                else:
                        print("Thanks for playing! Have a good day!")
                        return
                # Exit the fight loop once one
                
        elif choice == "2":
            # Solve riddle
            riddle = "The riddle is: What starts with an E, ends with an E, but only contains one letter?"
            print("You come across a treasure chest and a sign with a riddle written on it, to open the chest you must answer correctly! ")
            print(riddle)
            print("1. Elephant")
            print("2. Envelope")
            print("3. Eagle")
            print("4. Edge")
            player_answer = input("What is your answer? ")
            if player_answer == "2":
                print("Correct! The chest is open! You collect the treasure inside!")
                riddle_solved = True
            else:
                print("Incorrect. The answer is Envelope")
            # Add treasure to player's inventory
                player_inventory.append("treasure")
        elif choice == "3":
            # Check inventory
            if len(player_inventory) == 0:
                print("Your inventory is empty.")
            else:
                print("Your inventory contains:")
                for item in player_inventory:
                    print(item)
        elif choice == "4":
            # Look for items
            # Randomly select an item from the list
            item_found = random.choice(items)
            print(f"You found a {item_found}!")
            # Add the item to player's inventory
            player_inventory.append(item_found)
        elif choice == "5":
            # Quit game
            print("Thank you for playing!")
            break
        else:
            # Invalid input
            print("Invalid choice. Please try again.")
    # End of the game 
    play_again = input("Do you want to give it another try? (yes/no) ")
    if play_again.lower() == "yes":
        start_game()
    else:
        print("Thanks for playing! See you next time.")
# Start the game
start_game()