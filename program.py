import random
import sys
#import pygame

def wordbank(file = "bank.csv"):
   f = open(file, "r")
   word = []
   definition = []
   blank_2 = []
   alt = [] #alternate word
   study = []
   for line in f:
      lst = line.split(",")
      #print(lst)
      word.append(lst[0])
      definition.append(lst[1].replace("- ",","))
      alt.append(lst[2].lower().split("-"))
      blank_2.append(lst[3])
      study.append(lst[4].strip())
   table = [word, definition, alt, blank_2, study]
   return table

def awardPoints(checkAnswer,word,definition,study,points,tries,index):
   if checkAnswer == False:
      points -= (2-tries)*len(definition[index])
   elif checkAnswer == True:
      points += (tries*(len(word[index])*len(definition[index])))

   if (points>=10000):
      #initializeGame()
      pass
   else:
      pass

   return points

def check_answer(guess,word,index,alt):
   #Check if the answer passed in is correct

   for i in alt[index]:
      if (guess == i) == True:
         return True
      else:
         pass

   if str(word[index]).lower()==guess.lower():
      return True
   elif guess in alt[index]:
      return True
   else:
      return False

def randomize_question(definition,used_indexes):
   questionIndex = random.randint(1,len(definition)-1)

   check = True
   while check:
      if questionIndex in used_indexes:
         questionIndex = random.randint(1,len(definition)-1)
      else:
         check = False
   return questionIndex
def print_points(points,questions):
   pointsbox = 0;
   for i in range(len(str(points))):
      pointsbox+=1
   print("\033[1;33;40m+------"+(pointsbox)*"-"+"---+\033\033[1;35;40m----------------"+(len(str(questions)))*"-"+"--+\033[0m")
   print("\033[1;33;40m| Points",points,"|\033\033[1;35;40m Questions Left: "+str(questions)+" |\033[0m")
   print("\033[1;33;40m+------"+(pointsbox)*"-"+"---+\033\033[1;35;40m----------------"+(len(str(questions)))*"-"+"--+\033[0m")

##   print("\033[1;35;40m----------------"+(len(str(questions)))*"-"+"--+\033[0m")
##   print("\033[1;35;40m Questions Left: "+str(questions)+" |\033[0m")
##   print("\033[1;35;40m----------------"+(len(str(questions)))*"-"+"--+\033[0m")
   
def award_points():
   #If the answer in check_answer() is correct, award points
   pass

def graphics():
   #Idk. make it a game son.
   pass

def stringify(index,definition):
   return "+----------------------------------+\nWhat is the answer to the following? \n\n\033[1;37;40m"+definition[index]+"\033[0m\n+----------------------------------+\nYour Answer: "

def dontMindMe(word,definition,alt,blnk2,study):
   print("Used Indexes: ", used_indexes)
   print("Word Printing: ", word[aQhold].lower()) #printing the question for testing
   print("Printing Alternate List: ", alt[aQhold])

def main():
   print("\033[1;34;40m +-------------------Beginning Game-------------------+\033[0m")
   # print(wordbank("bank.csv"))
   table = wordbank("bank.csv")
   word = table[0]
   definition = table[1]
   alt = table[2]
   blnk2 = table[3]
   study = table[4]
   #don't ask the same question twice in one session
   used_indexes = []
   check = False
   points = 0
   pointsbox = 0

   testMe = False #change if you want to run testing.

   while len(used_indexes) != len(definition):
      if testMe == True:
         dontMindMe(word,definition,alt,blnk2,study)
      else:
         pass
      #Ask Question
      askQuestion = randomize_question(definition,used_indexes)
      aQhold = askQuestion

      used_indexes.append(aQhold)
      #how many tries are used
      tries = 2

      #asks the question and user input
      print_points(points,len(word)-len(used_indexes))

      inp = input(stringify(aQhold,definition))
      
      check = check_answer(inp,word,aQhold,alt)

      if False == check_answer(inp,word,aQhold,alt):
         print("\033[1;31;40mWrong...",word[aQhold].lower(),"is not equal","check is equal to",inp+"\033[0m")

      points+= awardPoints(check,word,definition,study,points,tries,aQhold)

      if check == False:
         correct = False
         while tries >=0 and correct != True:
            print("\033[1;31;40mWNo, please try again, "+str(tries)+" remaining.\033[0m")

            inp = input(stringify(aQhold,definition))

            check = check_answer(inp,word,aQhold,alt)
            ###
            if check_answer(inp,word,aQhold,alt):
               check = True
            else:
               check = False
               print("\033[1;31;40mWrong...",word[aQhold].lower(),"is not equal","check is equal to",inp+"\033[0m")
            #
            points+= awardPoints(check,word,definition,study,points,tries,aQhold)
            
            if check == False:
               tries -= 1
            else:
               correct = True
         #reset tries
main()
