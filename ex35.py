

prompt = "> "
def gold_room():
    print("You're in a gold room. How much do you want to take?")

    choice = input(prompt)
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, try to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("""There is a bear here.\nThe bear has a bunch of honey.
    How are you going to move the bear?""")
    bear_moved = False

    while True:
        choice = input(prompt)

        if choice == "take honey":
            dead("The bear look at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("Bear has moved from the door.\nYou can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear got pissed off!")
        elif choice == "open room" and bear_moved:
            gold_room()
        else:
            print("I got no idea what you means.")

def evil_room():
    print("Here you see the great evil DANTIN.")
    print("Do you flee for your life or eat you head?")

    choice = input(prompt)

    if "flee" in choice:
        start()
    elif "head" in choice:
        print("Well, that's tasty!")
    else:
        evil_room()

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.\nWhich one do you choose?")
    choice = input(prompt)

    if choice == "left":
        bear_room()
    elif choice == "right":
        evil_room()
    else:
        print("You're are lost until you starve.")

def dead(why):
    print(why, "Good job!")
    exit()

start()
