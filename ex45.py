# For dedent() - make text dedent to same level
from textwrap import dedent
# For randint() - random numbers
from random import randint
# For sleep() - slow text
from time import sleep
# For exit() - quit game when dead
from sys import exit
# For clear()
from os import system, name


# Use to clear the screen of text (need to figure best use)
def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


class Engine(object):
    # DO I EVEN NEED THIS?
    pass


class Charecter(object):

    # NOT all charecters need these, but a lot will
    def __init__(self, name, health, strength, charisma):
        self.name = name
        self.health = health
        self.strength = strength
        self.charisma = charisma

    # CALL update_health(value) to increase / decrease health
    def update_health(self, value):
        self.health += value

    def attack(self):
        attack_amount = randint(0, self.strength)
        return attack_amount


class Player(Charecter):

    inventory = []
    visited_locations = []
    current_location = ""
    ghost_beaten = False

    inv_dict = {
        "ghost amulet" : "Enables you to talk to ghosts.",
        "filler item" : "A filler item of no use."
    }

    loc_dict = {
        "castle" : "The center piece of the estate. A grand build that can be seen from anywhere!"
    }

    def player_stats(self):
        print(f"Player Name: {self.name}")
        print(f"Player Health: {self.health}")
        print(f"Player Strength: {self.strength}")
        print(f"Player Charisma: {self.charisma}")

        while True:
            print(f"\nYou have visited: {self.visited_locations}\n")
            print("These locations can be fast travelled to.")
            print("If you would like more information type the location name. If not press enter.")

            choice = input("> ")

            if choice == "":
                print("SKIP")
                break
            elif choice in main_player.loc_dict.keys():
                print("\n")
                print(choice.capitalize())
                print(main_player.loc_dict.get(choice),"\n")
            else:
                print("I didn't get that, try again.")

        while True:
            print(f"Your inventory contains: {self.inventory}\n")
            print("If you would like extra information type the item name in. If not press enter.")

            choice = input("> ").lower()

            if choice == "":
                print("SKIP")
                break
            elif choice in main_player.inv_dict.keys():
                print("\n")
                print(choice.capitalize())
                print(main_player.inv_dict.get(choice),"\n")
            else:
                print("I didn't get that, try again.")


    # def append_inventory(self, item):
    #     self.inventory.append(item)


class Combat(object):

    def __init__(self, player, boss):
        self.player = player
        self.boss = boss

    def combat_start(self):
        main_player.visited_locations.append("castle")
        while self.player.health > 0 and self.boss.health > 0:

            player_attack = self.player.attack()
            monster_attack = self.boss.attack()

            print(f"{self.boss.name} is attacking you.")
            print(f"The {self.boss.name} attack is {monster_attack}")
            self.player.update_health(0 - monster_attack)
            print(f"Your health is now {self.player.health}\n")

            if self.player.health <= 0:
                Death.sorry(self)

            sleep(1)

            print("You are attacking")
            print(f"Your attack is {player_attack}")
            self.boss.update_health(0 - player_attack)
            print(f"{self.boss.name} health is now {self.boss.health}\n")

            if self.boss.health <= 0:
                print(f"{self.boss.name} is dead\n")
                break

            sleep(1)


class Castle(object):

    def start(self):
        print("Back at the castle")
        print("Going to the basement")
        Basement.start(self)


class Basement(object):

    def start(self):
        main_player.current_location = "basement"

        main_player.player_stats()

        if main_player.ghost_beaten == False:

            print(dedent("You open the door to the basement. You can hardly see more than 2 steps infront of you, but you make your way down regardless.\nß"))

            print(dedent("As you get closer to what you belive to be the bottom you feel the air growing colder and colder. The sensation of another presense is growing around you.\n"))

            print(dedent("As your foot hits touches the floor at the bottom of the stairs, you see a glowing dot floating infront of you. The Dot appears to be getting bigger the more you look at it - but you can't avert your stare.\n"))

            print(dedent("In an instance the dot flashes so bright you can see nothing. As your vision comes back you see a man stood before you, but he is not like any normal man, you can see through him, a glow comes from his outline and in his right hand he is holding a sword. A big one at that... \n"))

            print(dedent("You ready yourself. Do you run or do you face these demon knowing that what you need must surely be past him?\n"))

            print(dedent("RUN / FIGHT\n"))

            while True:
                choice = input("> ").lower()

                if choice == "run":
                    print(dedent("You turn and run back up the staircase as fast as your legs will take you. This is a fight you will face another day."))
                    Castle.start(self)
                elif choice == "fight":
                    print(dedent("You prepare your hand on your blade. You try to take the first strike but the ghost is to fast for you..."))
                    break
                else:
                    print("You don't seem to be making any sense... Try again RUN or FIGHT!")

            ghost = Charecter("Ghost", 100, 50, 0)

            event = Combat(main_player, ghost)
            event.combat_start()

            main_player.ghost_beaten = True

            main_player.inventory.append("Ghost Amulet")


            print("Linear story is go to basement, do mission, talk to person, go and find coffee, come back to basement, recieve item.\n")

            GameMap.travel_to(self, "basement", "ruins")
        else:
            print("Already beat the Ghost!")
            GameMap.travel_to(self, "basement", "ruins")


class Ruins(object):

    def start(self):
        print("In the Ruins")


class Tavern(object):

    def start(self):
        print("At the Tavern")


class Woods(object):

    def start(self):
        print("In the Woods")


class Death(object):

    def sorry(self):
        print("You have died.")
        exit(1)


class GameMap(object):

    map = {
        'castle' : Castle(),
        'basement' : Basement(),
        'ruins' : Ruins(),
        'tavern' : Tavern(),
        'woods' : Woods()
    }


    def travel_to(self, *argv):
        travel_list = []

        for arg in argv:
            travel_list.append(arg)

        for place in travel_list:
            print(f"- Go to {place.upper()}")
        print("- Fast Travel")
        print("- View Stats")

        deciding = True
        while deciding:
            print("\nWhere do you want to go?\n")
            choice  = input("> ")

            choice = choice.lower()

            # fast traval access, will reprint the list again if you quit
            if "fast" in choice:
                GameMap.fast_travel()
                for place in travel_list:
                    print(f"- Go to {place.upper()}")
                print("- Fast Travel")
                print("- View Stats")
            elif "stats" in choice:
                main_player.player_stats()
                for place in travel_list:
                    print(f"- Go to {place.upper()}")
                print("- Fast Travel")
                print("- View Stats")
            elif choice not in travel_list:
                print("Sorry, try again.\n")
            else:
                deciding = False
                run = GameMap.map.get(choice)
                run.start()


    def fast_travel():
        while True:
            # This should never really be a thing... the start of the game will add a location immediatly
            if len(main_player.visited_locations) <= 0:
                print("You haven't got anywhere to fast travel to yet.")
                break
            else:
                print(f"You have been to {main_player.visited_locations}")
                print("Where do you want to go?")
                print("If you don't want to travel anywhere. Type 'Quit'")
                choice = input("> ")

                if choice.lower() == "quit":
                    print("Quitting fast travel.")
                    break
                elif choice.lower() == main_player.current_location:
                    print(f"You are already in {choice}")
                    print("Try going somewhere else.")
                elif choice.lower() in GameMap.map.keys() and choice.lower() in main_player.visited_locations:
                    print(f"Ok, we will go to {GameMap.map[choice]}")
                    GameMap.map[choice].start()
                else:
                    print("Sorry, I didn't get that! Try again...")


# START of the game
print(dedent("Hello, what's your name?"))
player_name = input("Player Name: ")

# PLAYER chooses what stat set they want to start with
print(dedent("\nTell me about yourself?\n"))

print(dedent("""
      Health - Reflects how much damage you can take. Default 100.\n
      Strength - The higher your strength the harder you can hit.\n
      Charisma - Talking to people can reveal secrets, the higher this stat the more likely people are to talk.\n
      """))

print(dedent("I'm CAUTIOUS in what I do. Health + 50, Strength + 25, Charisma +25\n"))

print(dedent("I'm a STRONG person, ask questions later. Health + 20, Strength + 75, Charisma + 5\n"))

print(dedent("I'm a CHARISMATIC person. Health + 30, Strength + 20, Charisma + 50\n"))

while True:
    choice = input("I am... ")

    if choice.lower() == "cautious":
        main_player = Player(player_name, 150, 25, 25)
        break
    elif choice.lower() == "strong":
        main_player = Player(player_name, 120, 75, 5)
        break
    elif choice.lower() == "charismatic":
        main_player = Player(player_name, 130, 20, 50)
        break
    else:
        print("Sorry can you say that again. Are you CAUTIOUS, STRONG or CHARISMATIC?")

print("These are your player stats. You can check out visited locations and your inventory as well. If you would like extra information on either a place or an item just type it into the console.")

print("\n")

test_start = Castle()
test_start.start()