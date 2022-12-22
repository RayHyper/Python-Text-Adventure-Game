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
            print("\nA", self.name, "appears!")

        def fight(self):
            print("")
            print(self.name, "attacks!")
            print(self.name, "delt", self.attack, "damage!")
            player1.health -= self.attack
            print(self.name, "HP:", self.health)

        def state(self):
            print("[", self.name, "stats]")
            print("[Level:", self.level, "]")
            print("[Health:", self.health, "]")
            print("[Attack:", self.attack, "]")

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
            print("----Your Stats----")
            print("Level:", self.level)
            print("Health:", self.health)
            print("Attack:", self.attack)
            print("Inventory:", self.inventory)
            print("-----------------")

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
        print("[Guard] You are on your own now. But here I have some spare change.")
        change = 10
        print("Gained $" + str(change))
        player1.money += change

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
        print("-----------" + player1.name.title() + "-----------")
        print("Level:", player1.level)
        print("Attack:", player1.attack)
        print("Health:", player1.health)
        print("Money: $" + str(player1.money))
        print("Current location:", place)
        print("Inventory: ", player1.inventory)
        turing_town()
        '''
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
            '''

    def turing_town():
        place = "Turing Town"

        print("<==================WELCOME TO TURING TOWN==================>")
        print("You are at the heart of Turing Town.")
        print("[N] Turing shop")
        print("[E] Turing Dungeon")
        print("[W] Turing Casino")
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
            turing_casino()

    def turing_shop():
        cheap = ["Slime"]
        medium = ["Gob"]
        expensive = ["Snaketail"]

        shop = {"[1] Wooden Sword": 10,
                "[2] Potion": 5}

        print("<==============TURING SHOP==============>")
        print("[Shop Owner] Welcome, what can I get you?")
        print("[Current Balance]: $" + str(player1.money))
        for k, v in shop.items():
            print(k + " $" + str(v))
        print("[S] Sell")
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
                if "Wooden Sword" not in player1.inventory:
                    player1.inventory.append("Wooden Sword")
                print("Bought! -$10")
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
        if choice == "S":
            print("Your inventory:", player1.inventory)
            sell = input("Type item >").title()

            if (sell in cheap) and (sell in player1.inventory):
                player1.inventory.remove(sell)
                random_price = random.randint(5, 10)
                player1.money += random_price
                print("Sold for $" + str(random_price))
                turing_shop()

            elif (sell in medium) and (sell in player1.inventory):
                player1.inventory.remove(sell)
                random_price = random.randint(10,50)
                player1.money += random_price
                print("Sold for $" + str(random_price))
                turing_shop()

            elif (sell in expensive) and (sell in player1.inventory):
                player1.inventory.remove(sell)
                random_price = random.randint(50,500)
                player1.money += random_price
                print("Sold for $" + str(random_price))
                turing_shop()

            else:
                print("Invalid")
                turing_shop()

        else:
            print("Invalid")
            turing_shop()

    def turing_casino():
        play_again = True
        print("<==============CASINO==============>")
        print("[Dealer] Welcome to the Turing Casino!")
        print("What would you like to play?")
        print("[D] Doors Betting")
        print("[E] Exit")

        choice = input(">").upper()
        if choice == "D":
            while play_again == True:
                goat = random.randint(1, 3)
                while True:
                    print("You have $" + str(player1.money))
                    bet = int(input("How much do you want to bet: "))

                    if bet > player1.money:
                        print("Invalid Amount")
                    else:
                        break
                print("You bet $" + str(bet))

                print("There will be 3 doors.")
                print("If you pick the right one you will double your money.")
                print("1 [.]     2 [.]     3 [.]")

                my_choice = int(input(">"))
                if goat == 1:
                    print("1 [x]     2 [.]     3 [.]")
                    if goat == my_choice:
                        print("You got it right!")
                        print("Gained +$" + str(bet * 2))
                        player1.money += bet * 2
                    else:
                        print("You lose..")
                        print("Lost -$" + str(bet))
                        player1.money -= bet
                elif goat == 2:
                    print("1 [.]     2 [x]     3 [.]")
                    if goat == my_choice:
                        print("You got it right!")
                        print("Gained +$" + str(bet * 2))
                        player1.money += bet * 2
                    else:
                        print("You lose..")
                        print("Lost -$" + str(bet))
                        player1.money -= bet

                elif goat == 3:
                    print("1 [.]     2 [.]     3 [x]")
                    if goat == my_choice:
                        print("You got it right!")
                        print("Gained +$" + str(bet * 2))
                        player1.money += bet * 2
                    else:
                        print("You lose..")
                        print("Lost -$" + str(bet))
                        player1.money -= bet

                again = input("Play Again?(Y/N):").upper()
                if again == "N":
                    turing_town()
        turing_town()

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

        print("[E] Exit")

        choice = input(">").upper()

        if choice == "1" or choice == "LEVEL 1" and player1.level >= 1:
            print("Entering Slime Attack")
            slime_attack()
        elif (choice == "2" or choice == "LEVEL 2") and (player1.level >= 2):
            print("Entering Goblin raider")
            goblin_raider()
        elif (choice == "3" or choice == "LEVEL 3") and (player1.level >= 3):
            print("Entering Snake Frenzy")
            snake_frenzy()
        elif choice == "E":
            turing_town()
        else:
            print("It is locked.")
            turing_dungeon()

    def slime_attack():
        slime_rand_attack = random.randint(1,10)
        random_hp = random.randint(5, 20)
        slime1 = Monster(health=random_hp, attack=slime_rand_attack, loot="Slime", level=2, name="Blue Slime")
        slime1.output()
        slime1.state()

        while slime1.health >= 0 and player1.health >= 0:
            random_num = random.randint(1, 100)
            player_random = random.randint(1, 100)
            print("")
            player1.stats()
            print("[A] Attack")
            print("[H] Heal")

            choice = input(">").upper()
            if choice == "H":
                player1.heal()
            elif choice == "A":
                print("You attack!")
                if player_random > 20:

                    slime1.health -= player1.attack
                    print("You dealt", player1.attack, "damage.")
                elif player_random < 10:
                    print("You missed.....")
                else:
                    print("Critical Hit")
                    slime1.health -= player1.attack + player1.attack
                    print("You dealt", player1.attack + player1.attack, "damage.")

            if random_num > 50 and slime1.health > 0:
                slime1.fight()
            elif random_num < 40 and slime1.health > 0:
                slime_random = random.randint(1, slime1.attack)
                print("")
                print(slime1.name, "attacks!")
                print(slime1.name, "delt", slime_random, "damage!")
                player1.health -= slime_random
                print(slime1.name, "HP:", slime1.health)

            else:
                print(slime1.name, "missed..")
                print(slime1.name, "HP:", slime1.health)

        if player1.health <= 0:
            print("You lose....")

        else:
            print("You win!")
            print("Gained 1 level!")
            player1.level += 1
            player1.inventory.append(slime1.loot)
            turing_town()

    def goblin_raider():
        random_goblin = random.randint(20, 50)
        random_hp = random.randint(20,70)
        goblin1 = Monster(health=random_hp, attack=random_goblin, loot="Gob", level=5, name="Green Goblin")
        goblin1.output()
        goblin1.state()

        while goblin1.health >= 0 and player1.health >= 0:
            random_num = random.randint(1, 100)
            player_random = random.randint(1, 100)
            print("")
            player1.stats()
            print("[A] Attack")
            print("[H] Heal")

            choice = input(">").upper()
            if choice == "H":
                player1.heal()
            elif choice == "A":
                print("You attack!")
                if player_random > 20:

                    goblin1.health -= player1.attack
                    print("You dealt", player1.attack, "damage.")
                elif player_random < 10:
                    print("You missed.....")
                else:
                    print("Critical Hit")
                    goblin1.health -= player1.attack + player1.attack
                    print("You dealt", player1.attack + player1.attack, "damage.")

            if random_num > 60 and goblin1.health > 0:
                goblin1.fight()
            elif random_num < 50 and goblin1.health > 0:
                slime_random = random.randint(1, goblin1.attack)
                print("")
                print(goblin1.name, "attacks!")
                print(goblin1.name, "delt", slime_random, "damage!")
                player1.health -= slime_random
                print(goblin1.name, "HP:", goblin1.health)

            else:
                print(goblin1.name, "missed..")
                print(goblin1.name, "HP:", goblin1.health)

        if player1.health <= 0:
            print("You lose....")

        else:
            print("You win!")
            print("Gained 2 level!")
            player1.level += 2
            player1.inventory.append(goblin1.loot)
            turing_town()

    def snake_frenzy():
        random_hp = random.randint(100,200)
        attack_random = random.randint(50, 200)
        snake1 = Monster(health=random_hp, attack=attack_random, loot="Snaketail", level=50, name="Mighty Snake")
        snake1.output()
        snake1.state()

        while snake1.health >= 0 and player1.health >= 0:
            random_num = random.randint(1, 100)
            player_random = random.randint(1, 100)
            print("")
            player1.stats()
            print("[A] Attack")
            print("[H] Heal")

            choice = input(">").upper()
            if choice == "H":
                player1.heal()
            elif choice == "A":
                print("You attack!")
                if player_random > 20:

                    snake1.health -= player1.attack
                    print("You dealt", player1.attack, "damage.")
                elif player_random < 10:
                    print("You missed.....")
                else:
                    print("Critical Hit")
                    snake1.health -= player1.attack + player1.attack
                    print("You dealt", player1.attack + player1.attack, "damage.")

            if random_num < 60 and snake1.health > 0:
                snake1.fight()
            elif random_num > 90 and snake1.health > 0:
                slime_random = random.randint(1, snake1.attack)
                print("")
                print(snake1.name, "attacks!")
                print(snake1.name, "delt", slime_random, "damage!")
                player1.health -= slime_random
                print(snake1.name, "HP:", snake1.health)

            else:
                print(snake1.name, "missed..")
                print(snake1.name, "HP:",snake1.health)

        if player1.health <= 0:
            print("You lose....")

        else:
            print("You win!")
            print("Gained 2 level!")
            player1.level += 2
            player1.inventory.append(snake1.loot)
            turing_town()

    play()


if __name__ == "__main__":
    main()
