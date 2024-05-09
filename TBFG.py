import random
import webbrowser
import os
import pyautogui
def waitfortype():
    quartsec = int(3) / int(random.randint(1, 10))
    return quartsec
os.system("title TBFG - Enderman-brewer")
print("\033[1;32;40m You found me! Please support my other games. :D") # Easter egg, by chance, added just before easter.
# Defines important scripts
def ClearTerm(lcoloop): # Clears the termenal by flooding it with a set amount of $
    while lcoloop != 0:
        print("$")
        lcoloop = lcoloop - 1

def BotPickMove():
  global p1health
  global p2health
  """ This function takes in two health values (P1HealthAI and P2HealthAI) 
      and outputs a decision ("Attack" or "Defense") based on a simple AI.
  """
  disort = int(random.randint(1, 5))
  P1healthAI = p1health * disort
  disort = int(random.randint(1, 5))
  P2healthAI = p2health * disort
  """  
      Args:
          P1HealthAI: The health of player 1.
          P2HealthAI: The health of player 2.

      Returns:
          A string, either "Attack" or "Defense".
  """
  # Chooses attack if player 1 is healthier than player 2 
  # and defense otherwise 
  if p1healthAI > p2healthAI:
    return "Attack"
  else:
    return "Shield"




def listmoves(): # What do you think?
    print("$ List - shows this again.")
    print("$ Attack - Deals up to 100 damage with a 10% crit chance, allowing up to 200 damage, this is a rare case.")
    print("$ Shield - Halves your damage.")
    print("$ NO - Don't you dare...")

def p1movestart(): # Does checks for player 1 for start of the turn, may also have a few player 2 things.
    p1shield = False

def p2movestart(): # Does checks for player 2 for start of the turn, may also have a few player 1 things.
    p2shield = False

def rkrl(): # Maybe it's best unsaid... Wait, HOW DID I JU-
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)
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
print("$ Pick your mode:")
print("$ VS AI")
print("$ VS friend")
AIinput = input("$$ ")
if AIinput == "VS AI":
    vsAI = 1
elif AIinput == "VS friend":
    vsAI = 0
else:
    print("$ Invalid, press enter to exit, then try again.")
    input("$$ ")
    exit()
print("$ How much health do you want players to have? I reccomend 1000-2000")
health = int(input("$$ ")) # Defines health
p1health = health
p2health = health
print("$") # Blank line w/ theme.
p1roleselect = False
while p1roleselect == False:
    print("$")
    print("$ Player 1, please select a role:")
    print("$ None - Just allows attack and shield")
    print("Scientest - unfinished, allows moves like poison and failed volcano.")
    p1role = input("$$ ")
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
    p2role = input("$$ ")
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
        ClearTerm(1)
        print(f"$ It's player {turn}'s turn.")
        ClearTerm(1)
        print(f"$ You are on {p1health} health, your enemy is on {p2health} health.")
        print("$")
        p1choice = input("$$ ")
        if p1choice == "Attack":
            damage = random.randint(1, 100)
            crit = random.randint(1, 10)
            if crit == 1:
                damage = damage * 2
            if p2shield == True:
                damage = damage / 2
            print(f"$ You dealt {damage} damage to player 2.")
            p2health = p2health - damage
            turn = 2
        elif p1choice == "Shield":
            p1shield = True
            turn = 2
        elif p1choice == "List":
            listmoves()
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
        ClearTerm(1)
        print(f"$ It's player {turn}'s turn.")
        ClearTerm(1)
        print(f"$ You are on {p2health} health, your enemy is on {p1health} health.")
        print("$")
        if vsAI == 1:
            p2choice = BotPickMove()
            pyautogui.sleep(waitfortype)
            print(f"$$ {p2choice}")
        elif vsAI == 0:
            p2choice = input("$$ ")
        if p2choice == "Attack":
            damage = random.randint(1, 100)
            crit = random.randint(1, 10)
            if crit == 1:
                damage = damage * 2
            if p1shield == True:
                damage = damage / 2
            print(f"$ You dealt {damage} damage to player 1.")
            p1health = p1health - damage
            turn = 1
        elif p2choice == "Shield":
            p2shield = True
            turn = 1
        elif p2choice == "List":
            listmoves()
        elif p2choice == "NO":
            rkrl()
            print("Player 2 wins.")
            input("$ Press enter to exit.")
            exit()
        if p1health <= 0:
            print("Player 1 wins.")
            input("$ Press enter to exit.")
            exit()
