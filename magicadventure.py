import random
import time


def main():
    class Monster:
        def __init__(self, health, attack, loot, level, name):
            self.health = health
            self.attack = attack
            self.name = name
            self.loot = loot
            self.level = level
            self.name = name

        def output(self):
            print("A", self.name, "appears!")
            print("HP:", self.health)
            print("Attack:", self.attack)

        def fight(self):
            print(self.name, "attacks!")
            print(self.name, "delt", self.attack, "damage!")
            player1.health -= self.attack
            print(self.name, "HP:", self.health)

        def state(self):
            print(self.name)
            print("HP:", self.health)
            print("Attack:",self.attack)



    class Player:

        def __init__(self, health, attack, potion, inventory, name, money, level):
            self.health = health
            self.attack = attack
            self.inventory = inventory
            self.name = name
            self.potion = potion
            self.money = money
            self.level = level

        def stats(self):
            print("----Stats----")
            print("Level:", self.level)
            print("Health:", self.health)
            print("Attack:", self.attack)
            print("Inventory:", self.inventory)
            print("-------------")

        def heal(self):
            if "Potion" in self.inventory:
                self.health += self.potion
                self.inventory.remove("Potion")
            else:
                print("Don't have healing item")

    player1 = Player(health=100, attack=0, potion=10, inventory=[], name="", money=0, level=1)

    def play():

        print("Welcome to Magic Adventure!")
        player1.name = input("What is your name?: ")
        print("\n[Welcome", player1.name, "to the world of Magic!]")
        print("[You can explore the world, fight monsters and meet new people!]")
        print(" _   |~  _")
        print("[_]--'--[_]")
        print("| |--`--| |")
        print("| | /^\ | |")
        print("|_|_|I|_|_|")

        print("\n[Loading]")
        #   for i in range(6,0):
        #    print(i , " ", end ="")
        # time.sleep(1)

        print("\n<==================START==================>")
        print("Story starts..")
        print("You wake up confused and cold.")
        print("You can hear birds chirping and the sounds of trees swaying in the wind.")
        print("You look around and see that you are in a forest.")
        print("There are many trees around you and a pathway.")
        print("Your can't remember how you got here but you decided to walk towards the pathway.")
        print("The pathway is grey made with stones and leads outside the forest.")
        print("You walk on the pathway.")
        print("1 hour later you are still walking.")
        print("You keep walking and you made it out of the forest.")
        print("You see a big castle with a single guard standing in the front.")
        print("The guard is wearing shiny armour and is standing still.")
        print("The guard does not appear to have any weapons.")
        print("\nWhat do you do?")
        print("[1] Try to walk past the guard.")
        print("[2] Go speak to the guard.")

        choice = int(input(">"))

        if choice == 1:
            print("[Action] You try to walk past the guard.")
            print("[Guard] Hey you there. Come here!")
            print("[Action] You stop and walk towards the guard.")
            print("[" + player1.name + "] " + "Hello sorry. What is this place?")

        elif choice == 2:
            print("[Action] You walk slowly and approach the guard.")
            print("[" + player1.name + "] " + "Hey what is this place?")

        print("[Guard] You are in Turing Town. You are new right?")
        print("[Guard] Most adventurers start off at the wizard's house, but it appears you did not.")
        print("[Guard] Well I can't help you, I'm just a guard doing my job.")
        print("[Guard] You are on your own now.")

        option()

    def option():
        print("\nWhat do you do?")
        print("[1] Attack the guard.")
        print("[2] Keep walking.")
        choice = int(input(">"))

        if choice == 1:
            print("[Action] You curl your fist and swing at the guard.")
            print("[Guard] hey whatT ARE YOU.")
            print("[Guard] The guard dodges your swing and punches you right in the head.")
            print("You fall to the ground.")
            print("You died.")

        elif choice == 2:
            print("You keep walking to the right of the castle")
            print("You see a sign on the sidewalk and read it.")
            map()

    def map():

        print("\n<==================MAP==================>")
        print("[North] Turing Town")
        print("[East] Golden Shield Town")
        print("[South] Maple Town")
        print("[West] Seven berries Town")

        print("_____________________________/  North Turing town /_____________________")
        print("                          [===]                                           ")
        print("                            |                                                ")
        print("                        [You are here]                                         ")
        print("    West   <---                                             ---> East ")
        print("  Seven berries town                                       Golden Shield Town ")
        print(" _______________________     South Maple Town   __________________________")
        print("                       /                       /")

        print("Where do you want to go? Type the direction.")
        choice2 = input(">").upper()

        if choice2 == "N" or choice2 == "NORTH":
            turing_town()

    def stat(place):
        choice = ""
        while choice != "e":
            print("[S] Stats")
            print("[M] Money")
            print("[L] Location")
            print("[E] Exit")

            choice = input(">").upper()

            if choice == "E":
                if place == "Turing Town":
                    turing_town()

            elif choice == "S":
                player1.stats()
            elif choice == "L":
                print("Location is", place)
            elif choice == "M":
                print("You have $" + str(player1.money))

    def turing_town():
        place = "Turing Town"

        print("<==================WELCOME TO TURING TOWN==================>")
        print("You are at the heart of Turing Town.")
        print("[N] Turing shop")
        print("[E] Turing Dungeon")
        print("[W] Turing Magical Meals")
        print("[I] Inventory")
        print("[S] Go back")

        choice = input(">").upper()

        if choice == "S":
            map()
        elif choice == "I":
            stat(place)
        elif choice == "N":
            turing_shop()
        elif choice == "E":
            turing_dungeon()
        elif choice == "W":
            print("Magical Meals")

    def turing_shop():
        shop = {"[1] Wooden Sword": 10,
                "[2] Potion": 5}

        print("<==============TURING SHOP==============>")
        print("[Shop Owner] Welcome, what can I get you?")
        for k, v in shop.items():
            print(k + " $" + str(v))
        print("[E] Exit")

        choice = input(">").upper()

        if choice == "E":
            print("Have a nice day!")
            turing_town()

        if choice == "1":
            print("----Stats----")
            print("Wooden Sword")
            print("Attack Damage: 5")
            buy = input("Want to buy? (Y/N): ").upper()
            if buy == "Y" and player1.money >= 10:
                print("Bought! -$10")
                player1.inventory.append("Wooden Sword")
                player1.money -= 10
                player1.attack += 5
                turing_shop()
            elif buy == "N":
                print("Ok have a nice day!")
                turing_shop()
            else:
                print("Not enough money....")
                turing_shop()

        if choice == "2":
            print("----Stats----")
            print("Potion")
            print("Heal: 10")
            buy = input("Want to buy? (Y/N): ").upper()
            if buy == "Y" and player1.money >= 5:
                print("Bought! -$5")
                player1.inventory.append("Potion")
                player1.money -= 5
                turing_shop()
            elif buy == "N":
                print("Ok have a nice day!")
                turing_shop()
            else:
                print("Not enough money....")
                turing_shop()

    def turing_dungeon():
        print("<==============TURING DUNGEON==============>")
        print("[Dungeon Master] Hey, welcome to the dungeon young fella!")

        if player1.level >= 1:
            print("[Level 1] Slime attack")
        if player1.level >= 2:
            print("[Level 2] Goblin raider")
        else:
            print("[LOCKED] Goblin raider")

        if player1.level >= 5:
            print("[Level 3] Snake frenzy")
        else:
            print("[LOCKED] Snake frenzy")

        choice = input(">").upper()

        if choice == "1" or choice == "LEVEL 1" and player1.level >= 1:
            print("Entering Slime Attack")
            slime_attack()
        elif (choice == "2" or choice == "LEVEL 2") and (player1.level >= 2):
            print("Entering Goblin raider")
        elif (choice == "3" or choice == "LEVEL 3") and (player1.level >= 3):
            print("Entering Snake Frenzy")
        else:
            print("It is locked.")
            turing_dungeon()

    def slime_attack():
        slime1 = Monster(health=20, attack=1, loot="Slime", level=1, name="Blue Slime")
        slime1.output()

        while slime1.health !=0 or player1.health != 0:
            print("[A] Attack")
            print("[H] Heal")
            print("[S] Stats")

            choice = input(">").upper()
            if choice == "S":
                player1.stats()
            elif choice == "H":
                player1.heal()
            elif choice == "A":
                print("You attack!")
                slime1.health -= player1.attack
                print("You dealt", player1.attack, "damage.")

            slime1.fight()



    play()


if __name__ == "__main__":
    main()
