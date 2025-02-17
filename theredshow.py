"""
The Red Show - A Text-Based Adventure Game

Overview:
The Red Show is a thrilling and immersive text-based adventure game set in a mysterious and eerie circus. Players navigate through various attractions, each offering unique challenges and puzzles. The goal is to collect keys from each attraction to escape the circus, while managing their character's sanity levels.

Game Mechanics:
1. Attractions: The game features three main attractions - Haunted House, Big Top, and House of Mirrors. Each attraction has its own set of challenges and contributes to the story's progression.

2. Sanity System: Players have a 'sanity' meter which fluctuates based on their experiences and choices in the game. Encounters with clowns or failing challenges at attractions can reduce sanity. If sanity drops to zero, the game ends.

3. Movement and Encounters: Players choose between 'sneaking' or 'running' to move towards the next attraction. Sneaking reduces the chance of encounters but takes longer, while running increases encounter chances but is quicker.

4. Puzzle Solving: Each attraction presents puzzles or challenges that players must overcome to collect keys.

5. Random Elements: The game incorporates random elements such as the number of turns to reach an attraction, the type of challenge faced, and the outcomes of certain actions, adding a layer of unpredictability and replayability.

Objective:
The primary objective is to collect keys from all attractions and escape the circus. Players must strategically make choices to maintain their sanity while overcoming the challenges of each attraction.

Endgame:
The game concludes when the player either collects all keys and escapes, thus winning the game, or loses all sanity, resulting in a game over.
The Red Show offers an engaging narrative and gameplay that combines strategy, puzzle-solving, and chance, providing an intriguing experience for players who enjoy text-based adventure games.

"""

import random

def house_of_mirrors(sanity, keys_collected):
    print("\n--------------------------------")
    print("\tHouse of Mirrors")
    print("--------------------------------")
    print("Navigate through the maze by solving riddles, and find the key and escape before your sanity runs out!\n")
    
    # Initializes the boolean statement to track if the key has been found
    found_key = False
    
    # Dictionary of riddles where the key is the riddle and the value is the answer
    riddles = {
        "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind.": "Echo",
        "The more of this there is, the less you see. What is it?": "Darkness",
        "I'm tall when I'm young, and I'm short when I'm old. What am I?": "Candle"
    }
    
    # Loops until the key is found or sanity runs out
    while not found_key and sanity > 0:
        direction = input("Choose a direction (left/right/straight): ").lower()
        # Checks if the input is valid
        if direction not in ["left", "right", "straight"]:
            print("Invalid direction. Choose left, right, or straight.\n")
            continue
        
        # Randomly chooses an event between encountering a riddle or a clown
        event = random.choice(["riddle", "clown"])
        if event == "riddle":
            # Select a random riddle from the dictionary
            riddle, answer = random.choice(list(riddles.items()))
            print("\nYou encounter a mirror with a riddle:", riddle)
            user_answer = input("Your answer: ").capitalize()
            # Checks if the answer is correct
            if user_answer == answer:
                print("\nCorrect! You feel closer to the key.")
                # Randomly decides if the key is found
                found_key = random.choice([True, False])
            else:
                # Decreases sanity for a wrong answer
                print("\nIncorrect! The mirror disappears and you feel lost.")
                sanity -= 1
                print("Your sanity is now " + str(sanity) + ".\n")
        else:
            # Clown encounter decreases sanity
            print("\nA clown jumps out! You lose some sanity.")
            sanity -= 2
            print("Startled, your sanity drops to " + str(sanity) + ".\n")
            
        # Checks if sanity has dropped to 0 or below
        if sanity <= 0:
            print("You are unable to navigate your way through the maze and the reflection of yourself and clowns drive you to madness.")
            return sanity, keys_collected
            
        # If the key is found
        if found_key:
            print("\nYou've found a key and managed to escape the Hall of Mirrors!")
            keys_collected += 1
            # Regain some sanity after finding a key
            sanity += 5  
            print("Relief floods over you, restoring some sanity.")
            # Cap sanity at 10
            sanity = min(sanity, 10)
            print("Feeling rejuvenated, your sanity is now " + str(sanity) + ".\n")

    return sanity, keys_collected

def haunted_house(sanity, keys_collected):
    print("\n------------------------------")
    print("\tHaunted House")
    print("------------------------------")
    print("Your task is to put the series of paintings in the correct narrative order.")
    print("You have 3 attempts to get it right, but be careful – each wrong attempt will cause in a loss of sanity.")

    # The correct order of the narrative depicted by the paintings
    correct_order = [
        "A knight setting out on a quest.",
        "The knight slaying a dragon.",
        "The knight finding a treasure.",
        "The knight returning home victorious."
    ]
    
    # Creatse a shuffled version of the paintings for the puzzle
    shuffled_paintings = correct_order[:]
    random.shuffle(shuffled_paintings)

    # Displays the shuffled paintings
    for i, painting in enumerate(shuffled_paintings, 1):
        print("Painting " + str(i) + ": " + painting)
        
    # Initializes the number of attempts the player has
    attempts = 3
    
    # Loops until num. of attempts runs out or sanity runs out
    while attempts > 0 and sanity > 0:
        print("\nEnter the numbers of the paintings in the correct order (one at a time):")
        player_order = []
        try:
            for i in range(4):
                # Collects the player's guess for the order
                number = int(input("Enter painting number " + str(i + 1) + ": ")) - 1  # Adjust for zero-indexing
                player_order.append(number)
                
            # Checks if the player's order matches the correct order
            is_correct = True
            for i in range(4):
                if shuffled_paintings[player_order[i]] != correct_order[i]:
                    is_correct = False
                    break
                
            # Check if the player's order matches the correct order
            if is_correct:
                print("Correct! A key is revealed.")
                keys_collected += 1
                # Regain some sanity after finding a key
                sanity += 5
                # Cap sanity at 10
                sanity = min(sanity, 10)
                print("You feel a sense of relief. Your sanity is now " + str(sanity) + ".\n")
                break
            else:
                # Reduces attempts and sanity if the order is incorrect
                print("Incorrect order. The atmosphere grows more oppressive: " + str(attempts-1) + " attempts left")
                attempts -= 1
                sanity -= 2
                print("You feel a sense of dread. Your sanity is now " + str(sanity) + ".")
        except ValueError:
            # Handles non-integer inputs
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            # Handles inputs outside the range 1-4
            print("Invalid number. Please enter a number from 1 to 4.")
            
        # Checks if sanity has dropped to 0 or below
        if sanity <= 0:
            print("You are unable to solve the puzzle and the paintings drive you to madness.")
            break
        
    # If all attempts are used without solving the puzzle
    if attempts == 0:
        print("You couldn't solve the puzzle. The mocking gaze of the paintings follows you as you leave.\n")

    return sanity, keys_collected

def big_top(sanity, keys_collected):
    print("\n------------------------")
    print("\tBig Top")
    print("------------------------")
    print("Walk the tightrope to reach the key hanging on the other side.")
    print("1. Hop - Advance quicker, more likely to lose balance.")
    print("2. Walk - Advance slower, least likely to lose balance.")
    print("3. Wait - Don't advance at all, regain some balance.")
    
    # Initializes balance level of the player
    balance = 5
    
    # Total steps needed to reach the key
    steps_needed = 15 
    
    # Loops while the player has balance and hasn't reached the key
    while balance > 0 and steps_needed > 0:
        action = input("Choose your action (hop/walk/wait): ").lower()
        
        # Movement actions
        if action == "hop":
            step = random.randint(2, 4)
            balance_change = random.randint(-3, -1)
        elif action == "walk":
            step = random.randint(1, 2)
            balance_change = random.randint(-2, 0)
        elif action == "wait":
            step = 0
            balance_change = random.randint(0, 2)
            # Random chance of a clown encounter that affects sanity
            if random.random() < 0.20: 
                # 20% chance of clown encounter
                print("While waiting, a clown appears below, startling you!")
                sanity -= 1
                print("A chill runs down your spine. Your sanity is now " + str(sanity) + ".")
        else:
            # Handles invalid input
            print("Invalid action. Choose hop, walk, or wait.\n")
            continue
        
        # Update steps needed and balance
        steps_needed -= step
        balance += balance_change
        # Cap the balance at 5
        balance = min(balance, 5) 
        
        # Informs the player of their progress
        print("You move forward " + str(step) + " steps. Balance remaining: " + str(balance) + "\n")
        
        # Checks if the player loses balance
        if balance <= 0:
            print("You lose your balance and fall! The shock shakes your sanity.")
            sanity -= 3
            print("Your mind reels from the fall. Your sanity is now " + str(sanity) + ".\n")
            break
        
    # Check if the player successfully reaches the key
    if steps_needed <= 0 and balance > 0:
        print("You've successfully crossed the tightrope and grabbed the key!")
        keys_collected += 1
        # Regain some sanity after finding a key
        sanity += 5
        print("The relief of success boosts your sanity.")
        # Cap sanity at 10
        sanity = min(sanity, 10)  
        print("Feeling emboldened, your sanity is now " + str(sanity) + ".\n")

    return sanity, keys_collected
    
def encounter_clown(sanity):
    print("\nA creepy clown jumps out at you!")
    # Randomly determines the amount of sanity lost due to the clown encounter
    sanity_loss = random.randint(1, 3)
    sanity -= sanity_loss
    print("You lose "+ str(sanity_loss) + " sanity. Current sanity: " + str(sanity))
    return sanity


def display_instructions():
    print("\n----------------------------------")
    print("\tGame Instructions:")
    print("----------------------------------")
    print("1. Explore the attractions to find the keys.")
    print("2. Stay diligent and solve puzzles to progress.")
    print("3. Make choices carefully as they affect your sanity.")
    print("4. Keep track of your sanity level. If it drops to zero, it's game over.")
    print("5. Use 'sneak' to move stealthily towards an attraction. This reduces the chance of encounters but takes longer.")
    print("6. Use 'run' to move quickly. This increases the chance of encounters but gets you to attractions faster.")
    print("7. Type 'help' anytime during the game for instructions.")
    print("8. Type 'exit' to quit the game.\n")

def intro():
    print("Shrouded in a cloak of eerie mist, you find yourself lost within 'The Red Show'. Heart pounding, you search for an escape amidst the twisted tents and haunting melodies.\n")

# Prologue
print("-----------------------------------------")
print("\tWelcome to The Red Show...")
print("-----------------------------------------")
print("\nIn the forgotten outskirts of an abandoned town, lies a circus tent, draped in crimson and shadows.")
print("The air is thick with a sense of dread and the distant echoes of eerie laughter.")
print("You find yourself standing at the entrance of The Red Show, a circus known for its horrors and mysteries.")
print("\nLegend has it that The Red Show was once a place of joy, but now it is cursed, inhabited by malevolent clowns.")
print("Your goal is to escape this nightmarish circus, but the only way out is through the Main Gate, locked with three keys.")
print("\nThese keys are hidden in different attractions of the circus: the Haunted House, the Big Top, and the House of Mirrors.")
print("But beware, the clowns are on the prowl, and your sanity is at stake. Losing all your sanity means losing yourself to the circus forever.")

# Game Variables

# List of available attractions
attractions = ["Haunted House", "Big Top", "House of Mirrors"]
# Counter for keys collected by the player
keys_collected = 0
# Starting sanity level of the player
sanity = 10  
# Boolean statement to control the main game loop
game_running = True
# Randomly determines the turns to reach the next attraction
turns_to_next_attraction = random.randint(2, 3)  
# Randomly selects the next attraction
next_attraction = random.choice(attractions)
 # Boolean statement to notify player about next attraction
attraction_notified = False

# Initial Introduction
display_instructions()
intro()

# Main game loop
while game_running:
    if turns_to_next_attraction > 0:
        # Inform the player of the next attraction being approached 
        if not attraction_notified:
            print("The next attraction you approach is the " + next_attraction + ".")
            attraction_notified = True

        # Choose action to reach next attraction
        action = input("Choose your action (sneak/run): ").lower()
        if action == "sneak":
            turns_to_next_attraction -= 1
            if turns_to_next_attraction > 0:
                print("Moving sneakily, you are " + str(turns_to_next_attraction) + " turns away from the next attraction.\n")
            # 15% chance of clown encounter
            if random.random() < 0.15:  
                sanity = encounter_clown(sanity) 
                # Checks if player's sanity reached zero
                if sanity <= 0:  
                    break
        elif action == "run":
            turns_to_next_attraction = 0
            # 70% chance of clown encounter
            if random.random() < 0.70: 
                sanity = encounter_clown(sanity) 
                # Checks if player's sanity reached zero
                if sanity <= 0:
                    break
                print("Despite the encounter, you make it to the attraction.\n")
            else:
                print("\nYou swiftly run to the next attraction and manage to reach it without any casualties.\n")
        elif action == "help":
            # Displays game instructions again
            display_instructions()
            continue
        elif action == "exit":
            # End the game if desired
            print("You chose to leave the circus... You wake up realizing that this was all a figment of your imagination")
            game_running = False
            continue
        else:
            print("That is not a valid option\n")
            continue
        
    # Player reaches an attraction
    if turns_to_next_attraction == 0 and sanity > 0:
        # Player reaches an attraction
        current_attraction = next_attraction
        print("You have reached the " + current_attraction + ".")
        search = input("Do you want to search for a key here? (yes/no): ").lower()
        if search == "yes":
            # Stores the current number of keys before the attraction
            keys_before = keys_collected 
            # Directs to the specific attraction's function
            if current_attraction == "Haunted House":
                sanity, keys_collected = haunted_house(sanity, keys_collected)
            elif current_attraction == "Big Top":
                sanity, keys_collected = big_top(sanity, keys_collected)
            elif current_attraction == "House of Mirrors":
                sanity, keys_collected = house_of_mirrors(sanity, keys_collected)
                
            # Checks if player's sanity reaches zero
            if sanity <= 0:
                break

            # If a key is collected, it removes the attraction from the list
            if keys_collected > keys_before:
                attractions.remove(current_attraction)  

            # Chooses the next attraction and reset variables for next journey
            if attractions:
                next_attraction = random.choice(attractions)
            turns_to_next_attraction = random.randint(2, 3)
            attraction_notified = False
        else:
            print("You decide to move on.")
            if attractions:
                next_attraction = random.choice(attractions)
            turns_to_next_attraction = random.randint(2, 3)
            attraction_notified = False

    # Checks if all keys have been collected
    if keys_collected == 3:
        print("You've found all the keys! You rush to the gate and turn them inside of the keyhole, resulting in the gates to open.")
        print("Congratulations on beating & escaping The Red Show")
        break

# Game Conclusion
if sanity <= 0:
    print("Overwhelmed by fear, you succumb to the madness of the circus.")
print("\nGame over. Thank you for playing The Red Show!")