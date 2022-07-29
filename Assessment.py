"""
Filename: NZ Quiz
Author: Saashika 
Date: 1/07/22
Description: An interactive, easy-to-use quiz about NZ.
"""
VALID_CHOICE_ONE = ["t"]
VALID_CHOICE_TWO = ["f"]

"""
Intro
"""
while user_name = input("Hi there, hope you're having a good day. What's your name? ")

print("Welcome to your quiz, " + user_name)

enter = input("This is a quiz about nz. Press 't' for truth and 'f' for false. Press 'c' if you wish to continue: ")

enter == "c":
    userchoice = input("Denis Glover wrote the poem The Magpies ")
    while not userchoice in VALID_CHOICE_ONE:
       userchoice = input ("Incorrect, please enter another answer: ")
if userchoice == "t":
    userchoice = input("Kiri Te Kanawa is a Wellington-born opera ")
    while not userchoice in VALID_CHOICE_ONE:
       userchoice = input ("Incorrect, please enter another answer: ")
if userchoice == "t":
    userchoice = input("God Save the King was New Zealand’s national anthem up to and during WW2 ")
    while not userchoice in VALID_CHOICE_ONE:
       userchoice = input ("Incorrect, please enter another answer: ")
if userchoice == "f":
    userchoice = input("Phar Lap was a New Zealand born horse who won the Melbourne Cup ")
    while not userchoice in VALID_CHOICE_TWO:
       userchoice = input ("Incorrect, please enter another answer: ")
if userchoice == "t":
    userchoice = input("Queen Victoria was the reigning monarch of England at the time of the Treaty ")
    while not userchoice in VALID_CHOICE_ONE:
       userchoice = input ("Incorrect, please enter another answer: ")
if userchoice == "t":
    userchoice = input("Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80s ")
    while not userchoice in VALID_CHOICE_ONE:
       userchoice = input ("Incorrect, please enter another answer: ")
if userchoice == "f":
    userchoice = input("Te Rauparaha is credited with intellectual property rights of Kamate! ")
    while not userchoice in VALID_CHOICE_TWO:
       userchoice = input ("Incorrect, please enter another answer: ")
if userchoice == "t":
    userchoice = input("The All Blacks are New Zealand’s top rugby team ")
    while not userchoice in VALID_CHOICE_ONE:
       userchoice = input ("Incorrect, please enter another answer: ")
if userchoice == "t": print("Well done! You have reached the end of the quiz with all answers correct :)")
