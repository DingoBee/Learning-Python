def fast_travel():
    while True:
        # This should never really be a thing... the start of the game will add a location immediatly
        if len(ex45.main_player.visited_locations) <= 0:
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

def travel_to(self, *argv):
    travel_list = []

    for arg in argv:
        travel_list.append(arg)

    for place in travel_list:
        print(f"- Go to {place.upper()}")
    print("- Fast Travel")

    deciding = True
    while deciding:
        print("Where do you want to go?")
        choice  = input("> ")

        choice = choice.lower()

        # fast traval access, will reprint the list again if you quit
        if "fast" in choice:
            fast_travel()
            for place in travel_list:
                print(f"- Go to {place.upper()}")
            print("- Fast Travel")
        elif choice not in travel_list:
            print("Sorry, try again.")
        else:
            deciding = False
            run = GameMap.map.get(choice)
            run.start()
