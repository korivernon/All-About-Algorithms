import random
import sys
import pygame

'''
I'm going to make this prettier... change the game more because I'm not a huge fan of it at the moment...
- https://www.youtube.com/watch?v=_lSNIrR1nZU
'''
def initializeGame():
   pygame.init()

   WIDTH = 800
   HEIGHT = 600

   RED = (255,0,0)
   BLUE = (0,0,255)
   YELLOW = (255,255,0)
   BACKGROUND_COLOR = (0,0,0)

   player_size = 50
   player_pos = [WIDTH/2, HEIGHT-2*player_size]

   enemy_size = 50
   enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
   enemy_list = [enemy_pos]

   SPEED = 10

   screen = pygame.display.set_mode((WIDTH, HEIGHT))

   game_over = False

   score = 0

   clock = pygame.time.Clock()

   myFont = pygame.font.SysFont("monospace", 35)

   def set_level(score, SPEED):
           if score < 20:
                   SPEED = 15
           elif score < 40:
                   SPEED = 20
           elif score < 60:
                   SPEED = 30
           else:
                   SPEED = 40
           return SPEED
           # SPEED = score/5 + 1


   def drop_enemies(enemy_list):
           delay = random.random()
           if len(enemy_list) < 10 and delay < 0.1:
                   x_pos = random.randint(0,WIDTH-enemy_size)
                   y_pos = 0
                   enemy_list.append([x_pos, y_pos])

   def draw_enemies(enemy_list):
           for enemy_pos in enemy_list:
                   pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

   def update_enemy_positions(enemy_list, score):
           for idx, enemy_pos in enumerate(enemy_list):
                   if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
                           enemy_pos[1] += SPEED
                   else:
                           enemy_list.pop(idx)
                           score += 1
           return score

   def collision_check(enemy_list, player_pos):
           for enemy_pos in enemy_list:
                   if detect_collision(enemy_pos, player_pos):
                           return True
           return False

   def detect_collision(player_pos, enemy_pos):
           p_x = player_pos[0]
           p_y = player_pos[1]

           e_x = enemy_pos[0]
           e_y = enemy_pos[1]

           if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
                   if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
                           return True
           return False

   while not game_over:

           for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                           sys.exit()

                   if event.type == pygame.KEYDOWN:

                           x = player_pos[0]
                           y = player_pos[1]

                           if event.key == pygame.K_LEFT:
                                   x -= player_size
                           elif event.key == pygame.K_RIGHT:
                                   x += player_size

                           player_pos = [x,y]

           screen.fill(BACKGROUND_COLOR)

           drop_enemies(enemy_list)
           score = update_enemy_positions(enemy_list, score)
           SPEED = set_level(score, SPEED)

           text = "Score:" + str(score)
           label = myFont.render(text, 1, YELLOW)
           screen.blit(label, (WIDTH-200, HEIGHT-40))

           if collision_check(enemy_list, player_pos):
                   game_over = True
                   break

           draw_enemies(enemy_list)

           pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

           clock.tick(30)

           pygame.display.update()

def wordbank(file = "bank.csv"):
   f = open(file, "r", encoding = "ISO-8859-1")
   word = []
   definition = []
   blank_2 = []
   alt = [] #alternate word
   study = []
   for line in f:
      lst = line.split(",")
      #print(lst)
      word.append(lst[0])
      definition.append(lst[1])
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

def award_points():
   #If the answer in check_answer() is correct, award points
   pass

def graphics():
   #Idk. make it a game son.
   pass

def stringify(index,definition):
   return "What is the answer to the following? \n\n"+definition[index]+"\n\nYour answer: "

def dontMindMe(word,definition,alt,blnk2,study):
   print("Used Indexes: ", used_indexes)
   print("Word Printing: ", word[aQhold].lower()) #printing the question for testing
   print("Printing Alternate List: ", alt[aQhold])
   
def main():
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
      inp = input(stringify(aQhold,definition))
      
      check = check_answer(inp,word,aQhold,alt)
      

      ###
      if check_answer(inp,word,aQhold,alt):
         check = True
      else:
         check = False
         print("wrong...",word[aQhold].lower(),"is not equal","check is equal to",inp)
      ##

      points+= awardPoints(check,word,definition,study,points,tries,aQhold)
      print("Points",points)
      
      
      if check == False:
         correct = False
         while tries >=0 and correct != True:
            print("No, please try again, "+str(tries)+" remaining.\n")
            inp = input(stringify(aQhold,definition))
      
            check = check_answer(inp,word,aQhold,alt)

            ###
            if check_answer(inp,word,aQhold,alt):
               check = True
            else:
               check = False
               print("wrong...",word[aQhold].lower(),"is not equal","check is equal to",inp)
            #
            print("Points",awardPoints(check,word,definition,study,points,tries,aQhold))
            
            if check == False:
               tries -= 1
            else:
               correct = True
         #reset tries
main()
