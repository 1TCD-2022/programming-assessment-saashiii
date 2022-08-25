"""
Filename: NZ Quiz
Author: Saashika 
Date: 1/07/22
Description: An interactive, easy-to-use quiz about NZ.
"""
"""
lists:
"""
VALID_CHOICE_ONE = ["t","true","T"]
VALID_CHOICE_TWO = ["f","false","F"]

APPROVED_NAMES = ["Adelaide","Thomas","Lia","Paul"]
NOT_APPROVED_NAMES = ["Ryle","Lydia","Trent","Amarantha"]

"""
Intro
"""

"""
score:
"""
score = 0
score = int(score)

"""
questions:
"""
while True:
   user_name = input("Hi there, hope you're having a good day. What's your name? Please make sure to enter your name with the correct spelling and capitilization! Good luck: ")
   if user_name in APPROVED_NAMES:
      print("Hi there, you're one of the approved names. Congrats, " + user_name)
   if user_name in NOT_APPROVED_NAMES:
      print("Sorry, you're not allowed in this quiz.")
      break
   else:
      print("Welcome to your quiz, " + user_name)
   enter = input("This is a quiz about NZ. When you type the correct answer you will be told your score. Press 't' for truth and 'f' for false. Press 'c' if you wish to continue. Press any other alphabet key to exit: ")
   if enter == "c":
      userchoice = input("Thanks for taking the quiz! Denis Glover wrote the poem The Magpies ")
   else:
      break
   if userchoice == "t" or "true":
      score = score + 1
      print("Your current score is " + str(score))
      userchoice = input("Good job! Kiri Te Kanawa is a Wellington-born opera ")
      while not userchoice in VALID_CHOICE_ONE:
         userchoice = input ("Incorrect, please enter another answer: ")
   if userchoice == "t" or "true":
      score = score + 1
      print("Your current score is " + str(score))
      userchoice = input("Well done! God Save the King was New Zealand’s national anthem up to and during WW2 ")
      while not userchoice in VALID_CHOICE_ONE:
         userchoice = input ("Incorrect, please enter another answer: ")
   if userchoice == "f" or "false":
      score = score + 1
      print("Your current score is " + str(score))
      userchoice = input("Fantastic job! Phar Lap was a New Zealand born horse who won the Melbourne Cup ")
      while not userchoice in VALID_CHOICE_TWO:
         userchoice = input ("Incorrect, please enter another answer: ")
   if userchoice == "t" or "true":
      score = score + 1
      print("Your current score is " + str(score))
      userchoice = input(" Wow! Queen Victoria was the reigning monarch of England at the time of the Treaty ")
      while not userchoice in VALID_CHOICE_ONE:
         userchoice = input ("Incorrect, please enter another answer: ")
   if userchoice == "t" or "true":
      score = score + 1
      print("Your current score is " + str(score))
      userchoice = input("Whoa, good job! Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80s ")
      while not userchoice in VALID_CHOICE_ONE:
         userchoice = input ("Incorrect, please enter another answer: ")
   if userchoice == "f" or "false":
      score = score + 1
      print("Your current score is " + str(score))
      userchoice = input("Thanks for continuing the quiz this far :) Te Rauparaha is credited with intellectual property rights of Kamate! ")
      while not userchoice in VALID_CHOICE_TWO:
         userchoice = input ("Incorrect, please enter another answer: ")
   if userchoice == "t" or "true":
      score = score + 1
      print("Your current score is " + str(score))
      userchoice = input("Almost done! The All Blacks are New Zealand’s top rugby team: ")
      while not userchoice in VALID_CHOICE_ONE:
         userchoice = input ("Incorrect, please enter another answer: ")
   if userchoice == "t" or "true": print("Well done! You have reached the end of the quiz with all answers correct :). Your current score is " + str(score))
   answer = str(input("Would you like to redo the quiz? Type 'yes' or 'no'. Please type carefully, any invalid answers will be interpretted as 'no' and the quiz will be terminated: "))
   if answer == "no":
      break
   if answer == "yes":
      continue
   else:
      print("Invalid answer, quiz ending")
      break
"""
end of quiz
"""
