import random 

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, max_health=160):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = max_health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= random.randint(0,11)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here(mtask)
    def heal(self):
        if self.health < 150:
           self.health += 20
           print(f'{self.name} healed up with some bandages!')
        else:
            print('Player cannot heal beyond maximum health!')

    def spec_ability(self, opponent):
        opponent.health -= self.attack_power
        print(f'{self.name} uses their special ability on opponent!')
        


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=30,)  # Boost health and attack power

    # Add your power attack method here(mtask)
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} strikes {opponent.name} with his sword for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    #Warrior's special ability is his 'super uppercut'. 
    def spec_ability(self, opponent):
        opponent.health -= self.attack_power
        print(f'{self.name} uses the super uppercut to damage opponent! ')
     
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} strikes {opponent.name} with the magic wand for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")    

    # Add your cast spell method here(mtask)
    # mage's special ability is casting spells 
    def spec_ability(self, opponent):
        opponent.health -= self.attack_power*2
        print(f"{self.name} casts a spell on {opponent.name} for double damage!")
        

# Archer class (inherits from Character)(mtask-A ranged attacker with abilities to shoot arrows and evade attacks)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=15)
    
    def attack(self, opponent):
        opponent.health -= self.attack_power*3
        print(f"{self.name} shoots two arrows at {opponent.name}!")

    # Archers special ability is to evade the attack
    def spec_ability(self, opponent):
        self.health =+ 15
        print(f"{self.name} slides out the way swiftly to evade {opponent.name}'s attack!")


# Paladin class (inhertits from Character)(mtask)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=25,)

    def attack(self, opponent):
        opponent.health -= self.attack_power*2
        print(f"{self.name} hits {opponent.name} with a the Double Strike Attack!")

    # paladin's special ability is to sheild himself from the wizards attack
    def spec_ability(self, opponent):
        self.health += 15
        print(f'{self.name} sheilds himself from {opponent.name} attack!')        

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  
    print("4. Paladin")  
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.spec_ability(wizard)
            pass  # Implement this
        elif choice == '3':
            player.heal()# Call the heal method here(done)
            pass  # Implement this
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            print(f"{player.name} loses this round, better luck next time! ")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        print(f'Victory! {player.name} wins this round!')

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()