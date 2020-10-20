import pickle, time, os, random


fileName = "Credentials.txt"
credentialJson = {} 


def encrypt(text,s):
  result = ""
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      result += chr((ord(char) + s-65) % 26 + 65)
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)
  return result


def SignIn():
  Username = input("What is your Username \n")
  Password = input("What is your Password \n")

  
  


def SignUp():
    global credentialJson, fileName
    print("What do you want your Username and Password to be")
    newUsername = input("New Username \n")
    newPassword = input("New Password \n")

    
    
    file = open(fileName,'a')
    file.write(encrypt(newUsername,len(newUsername)) + "|" + encrypt(newPassword,len(newPassword)) + "|" + 0)
    file.write("\n")
    file.close()
    

#Game

def Play(player1Name, player2Name, Cards):
    print("Playing")
    player1CardNumRan = random.randint(0,len(Cards))
    player2CardNumRan = random.randint(0,len(Cards))

    player1Card = Cards[player1CardNumRan]
    player2Card = Cards[player2CardNumRan]

    
    player1CardColour = player1Card[0]
    player2CardColour = player2Card[0]

    player1CardNum = player1Card[1]
    player2CardNum = player2Card[1]



    print("Player 1 Card Colour:", player1CardColour, " | ", "Player 1 Card Num:",player1CardNum)
    print("Player 2 Card Colour:", player2CardColour," | ", "PLayer 2 Card Num:",player2CardNum)

    if(player1CardColour == player2CardColour):
      print("Card Colours are the same")
      if(player1CardNum > player2CardNum):
        print("Player One Wins")
      else:
        print("Player Two Wins")
    else:
      if(player1CardColour == "red" and player2CardColour == "black"):
        print("Player One Wins")
      if(player2CardColour == "red" and player1CardColour == "black"):
        print("Player Two Wins")
      if(player1CardColour == "yellow" and player2CardColour == "red"):
        print("Player One Wins")
      if(player2CardColour == "yellow" and player1CardColour == "red"):
        print("Player Two Wins")
      if(player1CardColour == "black" and player2CardColour == "yellow"):
        print("Player One Wins")
      if(player2CardColour == "black" and player1CardColour == "yellow"):
        print("Player Two Wins")


        






#Game Setup

colours = ["red","yellow","black"]
maxCardNum = 10
Cards = []


def GameSetup(player1Name, player2Name):
    global colours, maxCardNum, Cards
    print("Setup")
    numOfCards = 30
    for i in range(0,numOfCards):
        pickedColour = random.choice(colours)
        pickedInt = random.randint(0,maxCardNum)
        Cards.append([pickedColour,pickedInt])
    Play(player1Name,player2Name,Cards)
    
        



#Temp Sign in system

def SignInSystem():
    player1Name = input("What is player ones name \n")
    player2Name = input("What is player twos name \n")


    if(player1Name != "" and player2Name != "" and player1Name != player2Name):
        GameSetup(player1Name,player2Name)
    else:
        print("Player Names are empty please enter a name OR your names are the same \n")
        SignInSystem()












SignUp()

