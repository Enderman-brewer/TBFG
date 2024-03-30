import random
print("You found me! Please support my other games. :D") # Easter egg, by chance, added just before easter.
# Defines important scripts
def ClearTerm(lcoloop): # Clears the termenal by flooding it with a set amount of $
    while lcoloop != 0:
        print("$")
        lcoloop = lcoloop - 1

def listmoves(): # What do you think?
    print("$ List - shows this again.")
    print("$ Attack - Deals up to 100 health with a 10% crit chance, allowing up to 200 damage, this is a rare case.")
    print("$ Shield - Halves your damage.")
    print("$ NO - Don't you dare...")

def p1movestart(): # Does checks for player 1 for start of the turn, may also have a few player 2 things.
    p1shield = False

def p2movestart(): # Does checks for player 2 for start of the turn, may also have a few player 1 things.
    p2shield = False

def rkrl(): # Maybe it's best unsaid... Wait, HOW DID I JU-
    print("----- .---- .---- ----- .---- ----- ----- ----- / ----- .---- .---- .---- ----- .---- ----- ----- / ----- .---- .---- .---- ----- .---- ----- ----- / ----- .---- .---- .---- ----- ----- ----- ----- / ----- .---- .---- .---- ----- ----- .---- .---- / ----- ----- .---- .---- .---- ----- .---- ----- / ----- ----- .---- ----- .---- .---- .---- .---- / ----- ----- .---- ----- .---- .---- .---- .---- / ----- .---- .---- .---- ----- .---- .---- .---- / ----- .---- .---- .---- ----- .---- .---- .---- / ----- .---- .---- .---- ----- .---- .---- .---- / ----- ----- .---- ----- .---- .---- .---- ----- / ----- .---- .---- .---- .---- ----- ----- .---- / ----- .---- .---- ----- .---- .---- .---- .---- / ----- .---- .---- .---- ----- .---- ----- .---- / ----- .---- .---- .---- ----- .---- ----- ----- / ----- .---- .---- .---- ----- .---- ----- .---- / ----- .---- .---- ----- ----- ----- .---- ----- / ----- .---- .---- ----- ----- .---- ----- .---- / ----- ----- .---- ----- .---- .---- .---- ----- / ----- .---- .---- ----- ----- ----- .---- .---- / ----- .---- .---- ----- .---- .---- .---- .---- / ----- .---- .---- ----- .---- .---- ----- .---- / ----- ----- .---- ----- .---- .---- .---- .---- / ----- .---- .---- .---- ----- .---- .---- .---- / ----- .---- .---- ----- ----- ----- ----- .---- / ----- .---- .---- .---- ----- .---- ----- ----- / ----- .---- .---- ----- ----- ----- .---- .---- / ----- .---- .---- ----- .---- ----- ----- ----- / ----- ----- .---- .---- .---- .---- .---- .---- / ----- .---- .---- .---- ----- .---- .---- ----- / ----- ----- .---- .---- .---- .---- ----- .---- / ----- .---- .---- ----- ----- .---- ----- ----- / ----- .---- ----- .---- ----- ----- ----- .---- / ----- .---- .---- .---- ----- .---- .---- .---- / ----- ----- .---- .---- ----- .---- ----- ----- / ----- .---- .---- .---- ----- .---- .---- .---- / ----- ----- .---- .---- .---- ----- ----- .---- / ----- .---- ----- .---- ----- .---- .---- .---- / ----- .---- .---- ----- ----- .---- .---- .---- / ----- .---- ----- .---- .---- ----- ----- ----- / ----- .---- .---- ----- ----- ----- .---- .---- / ----- .---- ----- .---- ----- ----- ----- .---- / ----- ----- .---- ----- ----- .---- .---- ----- / ----- .---- .---- .---- ----- ----- ----- ----- / ----- .---- .---- .---- ----- ----- ----- ----- / ----- ----- .---- .---- .---- .---- ----- .---- / ----- .---- .---- .---- .---- ----- ----- .---- / ----- .---- .---- ----- ----- .---- .---- .---- / ----- .---- ----- .---- ----- .---- ----- .---- / ----- .---- ----- .---- .---- ----- ----- ----- / ----- .---- .---- ----- ----- ----- .---- ----- / ----- .---- .---- ----- .---- .---- ----- .---- / ----- .---- ----- .---- ----- .---- .---- ----- / ----- ----- .---- .---- ----- ----- .---- ----- / ----- .---- ----- .---- .---- ----- .---- ----- / ----- .---- ----- .---- .---- ----- ----- ----- / ----- .---- ----- ----- .---- ----- ----- .---- / ----- .---- .---- ----- ----- .---- .---- .---- / ----- .---- ----- .---- .---- ----- .---- ----- / ----- ----- .---- .---- ----- ----- .---- ----- / ----- ----- .---- .---- .---- ----- ----- .---- / ----- .---- .---- .---- ----- .---- ----- .---- / ----- .---- .---- ----- ----- ----- .---- ----- / ----- .---- .---- ----- .---- .---- ----- .---- / ----- .---- ----- ----- ----- .---- ----- .---- / ----- .---- .---- ----- ----- .---- .---- .---- / ----- .---- ----- .---- .---- ----- .---- ----- / ----- ----- .---- .---- ----- ----- .---- ----- / ----- .---- .---- ----- .---- .---- ----- ----- / ----- ----- .---- .---- ----- ----- .---- ----- / ----- .---- ----- .---- .---- ----- .---- ----- / ----- .---- ----- .---- ----- ----- .---- .---- / ----- .---- ----- ----- ----- ----- .---- ----- / ----- ----- .---- .---- ----- .---- ----- .---- / ----- .---- .---- ----- ----- ----- .---- ----- / ----- ----- .---- .---- ----- ----- .---- .---- / ----- .---- ----- .---- ----- .---- ----- .---- / ----- .---- .---- ----- ----- .---- .---- .---- / ----- .---- .---- ----- ----- .---- ----- ----- / ----- .---- ----- .---- .---- ----- ----- ----- / ----- .---- ----- ----- ----- ----- ----- .---- / ----- ----- .---- ----- ----- .---- ----- .---- / ----- ----- .---- .---- ----- ----- .---- .---- / ----- .---- ----- ----- ----- .---- ----- -----")
# Clearing the terminal
looping = int(500)
ClearTerm(looping)

# Prints intro
print("$ Hello players, this is a Text Based Fighting Game, aka, TBFG.")
print("$ This game is built to run in the terminal using the python based inviroment, this game is intended for 2 players...")
print("$ But I can't tell you what to do, have 2 teams, be 1 player just having fun, I dont care.")
print("$")
print("$")
print("$")
print("$ But please don't use my code without permission and/or without putting me in credits.") # Please include my creator in the credits if you are not asking for permission. By the way, I am Stoflen. St-off-lin, a charactor made by Enderman_brewer... He made this game.

# Defines settings
print("$ How much health do you want players to have? I reccomend 1000-2000")
health = int(input("$ ")) # Defines health
p1health = health
p2health = health
print("$") # Blank line w/ theme.
p1roleselect = False
while p1roleselect == False:
    print("$")
    print("$ Player 1, please select a role:")
    print("$ None - Just allows attack and shield")
    print("Scientest - unfinished, allows moves like poison and failed volcano.")
    p1role = input("$ ")
    if p1role == "None":
        p1roleselect = True
    elif p1role == "Scientest":
        p1roleselect = True

p2roleselect = False
while p2roleselect == False:
    print("$")
    print("$ Player 2, please select a role:")
    print("$ None - Just allows attack and shield")
    print("Scientest - unfinished, allows moves like poison and failed volcano.")
    p2role = input("$ ")
    if p2role == "None":
        p2roleselect = True
    elif p2role == "Scientest":
        p2roleselect = True
ClearTerm(50)

# Gameplay loop
listmoves()
win = False
turn = random.randint(1, 2)
p1shield = False
p2shield = False
while win == False:
    if turn == 1:
        print(f"$ It's player {turn}'s turn.")
        print("$")
        p1choice = input("$ ")
        if p1choice == "Attack":
            damage = random.randint(1, 100)
            crit = random.randint(1, 10)
            if crit == 1:
                damage = damage * 2
            if p2shield == True:
                damage = damage / 2
            print(f"You dealt {damage} damage to player 2.")
            p2health = p2health - damage
            turn = 2
        elif p1choice == "Shield":
            p1shield = True
            turn = 2
        elif p1choice == "List":
            listmoves
        elif p1choice == "NO":
            rkrl()
            print("Player 2 wins.")
            input("$ Press enter to exit.")
            exit()
        if p2health <= 0:
            print("Player 1 wins.")
            input("$ Press enter to exit.")
            exit()
    elif turn == 2:
        print(f"$ It's player {turn}'s turn.")
        print("$")
        p2shield = False
        p2choice = input("$ ")
        if p2choice == "Attack":
            damage = random.randint(1, 100)
            crit = random.randint(1, 10)
            if crit == 1:
                damage = damage * 2
            if p1shield == True:
                damage = damage / 2
            print(f"You dealt {damage} damage to player 1.")
            p1health = p1health - damage
            turn = 1
        elif p2choice == "Shield":
            p2shield = True
            turn = 1
        elif p2choice == "List":
            listmoves()
        elif p2choice == "NO":
            rkrl()
            print("Player 1 wins.")
            input("$ Press enter to exit.")
            exit()
        if p1health <= 0:
            print("Player 2 wins.")
            input("$ Press enter to exit.")
            exit()

