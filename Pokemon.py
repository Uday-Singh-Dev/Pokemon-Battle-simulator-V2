from tkinter import *
import time
import random
#imports--


#make status moves work
#add all the typing system for both players
#add status effects as in PARALYZE AND BURN and code there uses.
#add the main menu 
#add color to the buttons depending on their type
#add button to respawn
#add a two player mode

#******************************************
#global variables
xp = 0
typing = "normal"
Battle = True

#text engine variables
max_len = 50
Time = 0.05

damage_calculation = 2

move = 0
move_stat = 0

#random placeholder values for your opponents pokemon
e_pokemon = "bulbasaur"
e_level = 10
e_health = 45
e_defence = 4.9
e_attack = 4.9
e_speed = 4.5
e_evasion =4.5
e_special_attack = 6.5
e_special_defence = 6.5
e_type = "grass"
#random placeholder values for your pokemon
pokemon = "charmander"
level = 10
health = 39
defence = 4.3
attack = 5.2
# want these numbers to be randomlygenerated for variation between a set value
speed = 6.5
evasion = 6.5
special_attack = 6.2
special_defence = 5
type = "fire"

Pokemon_Info = [pokemon,health,defence,attack,speed,level,evasion,special_attack,special_defence,type]
#name,damage,accuracy
moves = ["scratch","ember","growl","metal claw"]
#accuracy,damage
moves_stats = [100,4,100,4.5,95,0,100,5]
#the move kind
moves_kind = ["normal","special","status","normal"]
#the move type
moves_type  = ["normal","fire","normal","metal"]


Foe_Pokemon_Info = [e_pokemon,e_health,e_defence,e_attack,e_speed,e_level,e_evasion,e_special_attack,e_special_defence,e_type]

opponents_moves = ["scratch","drain","growl","vinewhip"]
opponents_moves_stats = [95,4,100,4.5,95,0,100,5]
opponents_moves_kind = ["normal","special","status","special"]
opponents_moves_type = ["normal","grass","normal","grass"]

pokemon_health = Pokemon_Info[1]
Foe_health = Foe_Pokemon_Info[1]


#*******************************************

#screen creations
screen = Tk()
screen.title("Pokemon Simulator")
screen.geometry("505x330")


#creating the canvas for the battle scene
canvas_battle = Canvas(screen,bg = "pale green",height = 330,width = 500)

#creating the canvas the main menu
canvas_mainmenu = Canvas(screen,bg = "bisque",height = 330,width = 500)

#****************************************************
#all of the subroutines

#************************************  

#canvas_battle defintions
def miss_function2():
  global miss,move_acc,evade,Foe_Pokemon_Info
  miss = False
  evade = False
  miss_chance = random.randint(1,99)
  if miss_chance >= moves_stats[move_acc]:
    miss = True
    return
  evade_chance = random.randint(1,100)
  if evade_chance <= Foe_Pokemon_Info[6]:
    evade = True
    return
    
def miss_function():
  #add a chance of the opponnets pokemons move of missing
  global miss,move_acc,evade,Pokemon_Info
  miss = False
  evade = False
  miss_chance = random.randint(1,99)
  if miss_chance >= opponents_moves_stats[move_acc]:
    return
  evade_chance = random.randint(1,100)
  if evade_chance <= Pokemon_Info[6]:
    evade = True
    return
  
#can be used for both user and opponents attack
def hit_varying_critical():
  #varys the damage of the pokemon
  global damage
  damage_increase = damage / 10
  damage_multiplier = random.randint(1,3)
  damage_increase = damage_increase * damage_multiplier
  damage += damage_increase
  damage = damage // 1

def foes_damage():
  global Pokemon_Info,Foe_Pokemon_Info,pokemon_health,damage,move,move_damage,miss,evade,Battle
  if Battle == False:
    return
  
  text_animation("",Foe_Pokemon_Info[0]+" used\n "+opponents_moves[move],0,"black")
  if miss == True:
    text_animation("",Foe_Pokemon_Info[0]+" missed",0,"black")
    return
  if evade == True:
    text_animation("",Pokemon_Info[0]+" evaded\n the attack",0,"black")
    return

  #grabbing the coordinates of the pokemons health bar
  x0,y0,x1,y1 = canvas_battle.coords(Pokemon_health_bar)
  #calculating the damage the opponents pokemon does
  if opponents_moves_kind[move] == "special":
    damage_x = opponents_moves_stats[move_damage] *   Foe_Pokemon_Info[7]
    damage = (damage_x // Pokemon_Info[8]) * 2
  elif opponents_moves_kind[move] == "normal":
    damage_x = opponents_moves_stats[move_damage] *   Foe_Pokemon_Info[3]
    damage = (damage_x // Pokemon_Info[2]) * 2
  elif opponents_moves_kind[move] == "status":
    damage = 0
  damage = damage * (Foe_Pokemon_Info[5] / Pokemon_Info[5])
  #changes the amount of damage for variation
  hit_varying_critical()
  #minuses that damage to your pokemons health
  pokemon_health -= damage
  #calculates the difference between pokemon health and the visual health
  health_diff = 198 / Pokemon_Info[1]
  #multiplys the damage by that health difference to accurately repersent int value of pokemon health
  damage = damage * health_diff
  #adds the changes to health to the health

    
  #checks if health is below 0 and if so will set it to constantly be 0
  if x1 < 300:
    x1 = 297.5
    pokemon_health = 0

  
  #the damage animation
  damage_increment = damage / 10
  for i in range(0,50):
    if x1 < 300:
      pokemon_health = 0
      x1 = 297.5
      break

    x1 -= damage_increment
    canvas_battle.coords(Pokemon_health_bar,x0,y0,x1,y1)
    screen.update()
    time.sleep(0.1)
  #configures the health bar to visually show the value of your pokemons health
  canvas_battle.coords(Pokemon_health_bar,x0,y0,x1,y1)
  #configures the value of the health bar depending on what the pokemon health is
  Pokemon_health_label.config(text = str(pokemon_health)+"/"+str(Pokemon_Info[1]))
  canvas_battle.update()
  
def users_damage():
  global Pokemon_Info,Foe_Pokemon_Info,Foe_health,damage,move,move_damage,miss,evade,Battle
  if Battle == False:
    return
  
  text_animation("",Pokemon_Info[0]+" used\n "+moves[move],0,"black")
  if miss == True:
    text_animation("",Pokemon_Info[0]+" missed",0,"black")
    return
  if evade == True:
    text_animation("",Foe_Pokemon_Info[0]+" evaded\n the attack",0,"black")
    return

  #grabbing the coordinates of the pokemons health bar
  x0,y0,x1,y1 = canvas_battle.coords(Opponents_Health_Bar)
  #calculating the damage the opponents pokemon does
  if moves_kind[move] == "special":
    damage_x = moves_stats[move_damage] *Pokemon_Info[7]
    damage = (damage_x // Foe_Pokemon_Info[8]) * Pokemon_Info[6]
  elif moves_kind[move] == "normal":
    damage_x = moves_stats[move_damage] * Pokemon_Info[3]
    damage = (damage_x // Foe_Pokemon_Info[2]) * 2
  elif moves_kind[move] == "status":
    damage = 0
  damage = type_system(damage,moves_type[move],Foe_Pokemon_Info[9])
  damage = damage * (Pokemon_Info[5] / Foe_Pokemon_Info[5])
  #changes the amount of damage for variation
  hit_varying_critical()
  #minuses that damage to your pokemons health
  Foe_health -= damage
  #calculates the difference between pokemon health and the visual health
  health_diff = 150 / Foe_Pokemon_Info[1]
  #multiplys the damage by that health difference to accurately repersent int value of pokemon health
  damage = damage * health_diff
  #adds the changes to health to the health

  #checks if health is below 0 and if so will set it to constantly be 0


  #the damage animation
  damage_increment = damage / 10
  for i in range(0,50):
    if x1 < 22:
      Foe_health = 0
      x1 = 21
      canvas_battle.coords(Opponents_Health_Bar,x0,y0,x1,y1)
      break

    x1 -= damage_increment
    canvas_battle.coords(Opponents_Health_Bar,x0,y0,x1,y1)
    screen.update()
    time.sleep(0.1)
  #configures the health bar to visually show the value of your pokemons health
  canvas_battle.coords(Opponents_Health_Bar,x0,y0,x1,y1)
  #configures the value of the health bar depending on what the pokemon health is
  canvas_battle.update()


#this is the opponents attack
def move_choosing():
  global move,move_damage,move_acc
  number = random.randint(0,len(opponents_moves))         
  if number == 0:
    move = 0
    move_damage = 1
    move_acc = 0
  elif number == 1:
    move = 1
    move_damage = 3
    move_acc = 2
  elif number == 2:
    move = 2
    move_damage = 5
    move_acc = 4
  elif number == 3:
    move = 3
    move_damage = 7
    move_acc = 6
    
def Foes_attack():
  miss_function()
  foes_damage()


def dead_checking():
  global pokemon_health, Foe_health,Battle
  if Foe_health <= 0 :
    #cant detect if player pokemon one shots opponents pokemon
    victory()
    xp_gain()
    deactivate_button()
    Battle = False
    return
  elif pokemon_health <= 0:
    print("dead")
    deactivate_button()
    Lose()
    Battle = False
    return


def fight_sequence():
  global Battle
  Battle = True
  deactivate_button()
  Buttons_Back()
  if Pokemon_Info[4] > Foe_Pokemon_Info[4]:
    User_attack()
    type_text()
    dead_checking()
    if Battle == True:
      move_choosing()
      Foes_attack()
      type_text()
      dead_checking()
  elif Foe_Pokemon_Info[4] > Pokemon_Info[4]:
    move_choosing()
    Foes_attack()
    type_text()
    dead_checking()
    if Battle == True:
      User_attack()
      type_text()
      dead_checking()
  text_animation("","What will\n"+Pokemon_Info[0]+" do?",0,"black")
  if Battle == True:
    reactivate_button()
  screen.update()
  return


def User_attack():
  miss_function2()
  users_damage()

def Pokemon_Attack_Button():
  Attack_Button1.place(x =280,y =265)
  Attack_Button2.place(x =390,y =295)
  Attack_Button3.place(x =390,y =265)
  Attack_Button4.place(x = 280, y =295)
  Pokemon_Attack_Button.place_forget()
  Bag_Button.place_forget()
  Run_Away_Button.place_forget()
  Pokemon_Button.place_forget()



#the different attacks of the pokemon
def Attack_Button1():
  global move,move_damage,move_acc
  move = 0
  move_damage = 1
  move_acc = 0
  fight_sequence()
  
def Attack_Button2():
  global move,move_damage,move_acc
  move = 1
  move_damage = 3
  move_acc = 2
  fight_sequence()
  
def Attack_Button3():
  global move,move_damage,move_acc
  move = 2
  move_damage = 5
  move_acc = 4
  fight_sequence()
  
def Attack_Button4():
  global move,move_damage,move_acc
  move = 3
  move_damage = 7
  move_acc = 6
  fight_sequence()

#text engine
def text_animation(speaker,text,true,text_color):
  #displays text in an animation
  global max_len,Next_line,text_length,act_text,Time,Battle
  if Battle == False:
    return
  deactivate_button()
  if true == 1:
    #checks if the editor wants a person saying the text or the narrator saying it
    text = speaker+": "+text
  text_length = len(text)
  if text_length > max_len:
    #checks if text is over max length
    print("too many character in the string")
    return
  act_text = ""
  for i in range(0,text_length):
      #getting the characters of the text one by one to display an animation
    text_p = text[i]
    act_text += text_p
      #checking if person wants to skip the text animation
      #changes the text and colors it based on the editors parameters
    Pokemon_Action_Label.config(text = act_text,fg = text_color)
      #updates the game to display the new text
    canvas_battle.update()
      #waiting time so there is a delay between each letter
    time.sleep(Time)
  time.sleep(0.5)



#this will deactivate the buttons in the fight scene
def Buttons_Back():
  #will un pack the different attacks of the pokemon
  Attack_Button1.place_forget()
  Attack_Button2.place_forget()
  Attack_Button3.place_forget()
  Attack_Button4.place_forget()
  Pokemon_Attack_Button.place(x =280,y =265)
  Bag_Button.place(x = 390, y =265)
  Run_Away_Button.place(x = 390, y =295)
  Pokemon_Button.place(x = 280, y =295)
  canvas_battle.update()

def deactivate_button():
  Pokemon_Attack_Button.config(state = "disabled",disabledforeground = "grey")
  Run_Away_Button.config(state = "disabled",disabledforeground = "grey")
  Pokemon_Button.config(state = "disabled",disabledforeground = "grey")
  Bag_Button.config(state = "disabled",disabledforeground = "grey")

  canvas_battle.update()
  
def reactivate_button():
  Pokemon_Attack_Button.config(state = "active")
  Run_Away_Button.config(state = "active")
  Pokemon_Button.config(state = "active")
  Bag_Button.config(state = "active")

def victory():
  text_animation("","Foe "+Foe_Pokemon_Info[0]+"\n fainted",0,"black")
  text_animation("","You won the\n battle, congrats",0,"black")

def Lose():
  print("here")
  text_animation("","your "+Pokemon_Info[0]+"\n fainted",0,"black")
  text_animation("","You payed 'money'\n to foe",0,"black")
#xp equation = (Enemy_level / Pokemon_level) * 10
def xp_gain():
  global Pokemon_Info,Foe_Pokemon_Info,xp,xp_bar_gain

  #the amount of xp gained
  xp_gain = (Foe_Pokemon_Info[5] / Pokemon_Info[5]) * 10
  print(xp_gain)
  if xp_gain <= 30:
    xp_gain = 30
  xp_remainder = 0
  #xp required to level up
  xp_required = Pokemon_Info[5]*10
  if xp_gain > xp_required:
    xp_remainder = xp_gain - xp_required
  xp_difference = 198 / xp_required
  #max = 198
  #difference between xp bar and xp required to level up
  #adding xp gain to xp
  xp += xp_gain
  #getting coordinates of xp bar
  x0,y0,x1,y1 = canvas_battle.coords(Pokemon_xp_bar)
  #calcuating the xp bar gains
  xp_bar_gain = xp_gain * xp_difference
  xp_bar_remainder = xp_bar_gain - 198
  #updating xp bar
  if xp_bar_gain > 198:
    xp_bar_gain == 198
  xp_gain_increment = xp_bar_gain / 10
  for i in range(0,10):
    x1 += xp_gain_increment
    canvas_battle.coords(Pokemon_xp_bar,x0,y0,x1,y1)
    canvas_battle.update()
    time.sleep(0.1)

  if xp_remainder == 0:
    return
  level_up(i,xp_bar_remainder,x1,xp_remainder)

def Level_up_stats():   #still have to increase stats 
  Pokemon_level_label.config(text ="Lvl "+str(Pokemon_Info[5]))
  Pokemon_current_stats.config(fg = "black")
  Pokemon_current_stats.place(x=375,y=55)
  canvas_battle.update()
  text_animation("","Your "+Pokemon_Info[0]+"\n leveled up!",0,"black")
  time.sleep(3)
  upgrade_stats()#update level label on pokemon
  Pokemon_current_stats.place(x=375,y=55)
  canvas_battle.update()
  time.sleep(3)
  Pokemon_current_stats.place_forget()
  
def upgrade_stats():
  Pokemon_Info[1] **= 1.02
  Pokemon_Info[1] = round(Pokemon_Info[1],1)
  Pokemon_Info[2] **= 1.02
  Pokemon_Info[2] = round(Pokemon_Info[2],1)
  Pokemon_Info[3] **= 1.02
  Pokemon_Info[3] = round(Pokemon_Info[3],1)
  Pokemon_Info[4] **= 1.02
  Pokemon_Info[4] = round(Pokemon_Info[4],1)
  Pokemon_Info[7] **= 1.02
  Pokemon_Info[7] = round(Pokemon_Info[7],1)
  Pokemon_Info[8] **= 1.02
  Pokemon_Info[8] = round(Pokemon_Info[8],0)
  Pokemon_current_stats.config(text ="Health:"+ str(Pokemon_Info[1])+"\nDefence:"+str(Pokemon_Info[2])+"\nAttack:"+str(Pokemon_Info[3])+"\nSpeed:"+str(Pokemon_Info[4])+"\nSp.Attack:"+str(Pokemon_Info[7])+"\nSp.Defence:"+str(Pokemon_Info[8]),font=("Helvetica",0),bg = "white",fg = "green")



def level_up(i,xp_bar_remainder,x1,xp_remainder):
  global Pokemon_Info,xp,xp_bar_gain
  LevelUp2 = False
  Pokemon_Info[5] += 1
  xp = xp_remainder
  x0,y0,x1,y1 = canvas_battle.coords(Pokemon_xp_bar)
  x1 -= xp_bar_gain
  x1_reset = x1
  canvas_battle.coords(Pokemon_xp_bar,x0,y0,x1,y1)
  canvas_battle.update()
  Level_up_stats()
  #add level up stats here
  if xp_bar_remainder > 198:
    xp_bar_remainder = 198
    LevelUp2 = True
    
  xp_remainder_increment = xp_bar_remainder / 10
  for i in range(0,10):
      x1 += xp_remainder_increment
      canvas_battle.coords(Pokemon_xp_bar,x0,y0,x1,y1)
      canvas_battle.update()
      time.sleep(0.1)
    
  if LevelUp2 == True:
    Pokemon_Info[5] += 1
    x0,y0,x1,y1 =canvas_battle.coords(Pokemon_xp_bar)
    x1 = x1_reset
    xp = 0
    canvas_battle.coords(Pokemon_xp_bar,x0,y0,x1,y1)
    canvas_battle.update()
    Level_up_stats()

def type_text():
  global typing
  if typing == "effective":
    text_animation("","It was super effective!",0,"green")
  elif typing == "deffective":
    text_animation("","It wasnt very effective",0,"red")

def damage_effective(damage):
  global typing
  damage *= 2
  typing = "effective"
  return damage
def damage_deffective(damage):
  global typing
  damage /= 2
  typing = "deffective"
  return damage
def type_system(damage,move,defenders_type):
  global typing
  typing = "normal"
  #damage is the parameter damage passed on from main code. attackers_type and defenders type will be the arguments stored in the array.
  if move == "normal":
    if defenders_type == "ghost":
      damage = 0
      #have to add that to text 
    if defenders_type == "rock":
      damage = damage_deffective(damage)
    if defenders_type == "steel":
      damage = damage_effective(damage)
    
  if move == "fire":
    if defenders_type == "grass":
      damage = damage_effective(damage)
      print("effective")
    elif defenders_type == "bug":
      damage = damage_effective(damage)
    elif defenders_type == "ice":
      damage = damage_effective(damage)
    elif defenders_type == "steel":
      damage = damage_effective(damage)
      
    elif defenders_type == "fire":
      damage = damage_deffective(damage)
    elif defenders_type == "water":
      damage = damage_deffective(damage)
    elif defenders_type == "rock":
      damage = damage_deffective(damage)
    elif defenders_type == "dragon":
      damage = damage_deffective(damage)
  
  if move == "water":
    if defenders_type == "fire":
      damage = damage_effective(damage)
    elif defenders_type == "ground":
      damage = damage_effective(damage)
    elif defenders_type == "rock":
      damage = damage_effective(damage)

    elif defenders_type == "water":
      damage = damage_deffective(damage)
    elif defenders_type == "grass":
      damage = damage_deffective(damage)
    elif defenders_type == "dragon":
      damage = damage_deffective(damage)
  
  if move == "grass":
    if defenders_type == "water":
      damage = damage_effective(damage)
    elif defenders_type == "ground":
      damage = damage_effective(damage)
    elif defenders_type == "rock":
      damage = damage_effective(damage)
      
    elif defenders_type == "fire":
      damage = damage_deffective(damage)
    elif defenders_type == "grass":
      damage = damage_deffective(damage)
    elif defenders_type == "poison":
      damage = damage_deffective(damage)
    elif defenders_type == "flying":
      damage = damage_deffective(damage)
    elif defenders_type == "bug":
      damage = damage_deffective(damage)
    elif defenders_type == "dragon":
      damage = damage_deffective(damage)
    elif defenders_type == "steel":
      damage = damage_deffective(damage)
      
  if move == "electric":
    if defenders_type == "water":
      damage = damage_effective(damage)
    elif defenders_type == "flying":
      damage = damage_effective(damage)

    elif defenders_type == "grass":
      damage = damage_deffective(damage)
    elif defenders_type == "electric":
      damage = damage_deffective(damage)
    elif defenders_type == "dragon":
      damage = damage_deffective(damage)
    elif defenders_type == "ground":
      damage = 0
  
  if move == "ice":
    if defenders_type == "grass":
      damage = damage_effective(damage)
    elif defenders_type == "ground":
      damage = damage_effective(damage)
    elif defenders_type == "flying":
      damage = damage_effective(damage)
    elif defenders_type == "dragon":
      damage = damage_effective(damage)

    elif defenders_type == "fire":
      damage = damage_deffective(damage)
    elif defenders_type == "water":
      damage = damage_deffective(damage)
    elif defenders_type == "ice":
      damage = damage_deffective(damage)
    elif defenders_type == "steel":
      damage = damage_deffective(damage)

  if move == "fighting":
    if defenders_type == "normal":
      damage = damage_effective(damage)
    elif defenders_type == "ice":
      damage = damage_effective(damage)
    elif defenders_type == "rock":
      damage = damage_effective(damage)
    elif defenders_type == "dark":
      damage = damage_effective(damage)
    elif defenders_type == "steel":
      damage = damage_effective(damage)

    elif defenders_type == "poison":
      damage = damage_deffective(damage)
    elif defenders_type == "flying":
      damage = damage_deffective(damage)
    elif defenders_type == "psychic":
      damage = damage_deffective(damage)
    elif defenders_type == "bug":
      damage = damage_deffective(damage)
    elif defenders_type == "fairy":
      damage = damage_deffective(damage)

  if move == "poison":
    if defenders_type == "grass":
      damage = damage_effective(damage)
    elif defenders_type == "fairy":
      damage = damage_effective(damage)

    elif defenders_type == "poison":
      damage = damage_deffective(damage)
    elif defenders_type == "ground":
      damage = damage_deffective(damage)
    elif defenders_type == "rock":
      damage = damage_deffective(damage)
    elif defenders_type == "ghost":
      damage = damage_deffective(damage)
    elif defenders_type == "steel":
      damage = 0

  if move == "ground":
    if defenders_type == "fire":
      damage = damage_effective(damage)
    elif defenders_type == "electric":
      damage = damage_effective(damage)
    elif defenders_type == "poison":
      damage = damage_effective(damage)
    elif defenders_type == "rock":
      damage = damage_effective(damage)
    elif defenders_type == "steel":
      damage = damage_effective(damage)

    elif defenders_type == "grass":
      damage = damage_deffective(damage)
    elif defenders_type == "flying":
      damage = 0
  


  
  return damage
#********************************************
#canvas objects


#*******************************
#canvas_battle objects

#placeholder for your information
Pokemon_information_box = canvas_battle.create_rectangle(0,0,250,85,fill = "white",outline = "black")
canvas_battle.move(Pokemon_information_box,250,175)

#A label too show your pokemons maxium hp and current hp
Pokemon_health_label = Label(canvas_battle,text =str(pokemon_health)+"/"+str(Pokemon_Info[1]))

Pokemon_health_label.place(x =385,y =240)

#Name of your pokemon
Pokemon_name_label = Label(canvas_battle,text =Pokemon_Info[0],font =("bold",15))
Pokemon_name_label.place(x =255,y =180)

#The level of the pokemon you are fighting with
Pokemon_level_label = Label(canvas_battle,text ="Lvl "+str(Pokemon_Info[5]))
Pokemon_level_label.place(x =462,y =180)

#Placeholder for where the health bar goes
Pokemon_health_bar_holder = canvas_battle.create_rectangle(0,0,200,17,fill = "black",outline = "black")
canvas_battle.move(Pokemon_health_bar_holder,297,210)

#the health-bar of the pokemon
Pokemon_health_bar = canvas_battle.create_rectangle(0,0,198,15,fill = "red",outline = "red")
canvas_battle.move(Pokemon_health_bar,297.5,211)

#a label to show where hp goes
HP_label = Label(canvas_battle,text = "HP",bg = "white",font =("bold",8))
HP_label.place(x = 278,y = 210)

#a placeholder for the xp of the pokemon
Pokemon_xp_bar_placeholder = canvas_battle.create_rectangle(0,0,200,8,fill = "light grey",outline = "black")
canvas_battle.move(Pokemon_xp_bar_placeholder,297,229)

#the xp of your pokemon
Pokemon_xp_bar = canvas_battle.create_rectangle(0,0,0,5,fill = "yellow",outline = "yellow")
canvas_battle.move(Pokemon_xp_bar,298,230)

#Trangle pointer to show where your pokemon info is.
Your_Triangle_Pointer = canvas_battle.create_polygon(40,40,70,25,70,40,fill ="white",outline = "black")
canvas_battle.move(Your_Triangle_Pointer,180,170)

#Rectangle to improve UI
Rectangle_UI_Fight = canvas_battle.create_rectangle(12,12,525,77,fill = "midnight blue",outline = "midnight blue")
canvas_battle.move(Rectangle_UI_Fight,-20,250)


#rectangle to hold text for what happens during the fight
Rectangle_Text_Holder = canvas_battle.create_rectangle(12,12,275,73,fill = "Yellow",outline = "black")
canvas_battle.move(Rectangle_Text_Holder,-8,252)

Rectangle_Text_Holder2 = canvas_battle.create_rectangle(12,12,270,67,fill = "white",outline = "midnight blue",)
canvas_battle.move(Rectangle_Text_Holder2,-6,255)

#The floor your pokemon stands on.
Your_Pokemon_Floor = canvas_battle.create_oval(50,90,200,150,fill = "green",outline = "dark green",width = 5)
canvas_battle.move(Your_Pokemon_Floor,-20,75)



Pokemon_current_stats = Label(canvas_battle,text ="Health:"+ str(Pokemon_Info[1])+"\nDefence:"+str(Pokemon_Info[2])+"\nAttack:"+str(Pokemon_Info[3])+"\nSpeed:"+str(Pokemon_Info[4])+"\nSp.Attack:"+str(Pokemon_Info[7])+"\nSp.Defence:"+str(Pokemon_Info[8]),font=("Helvetica",0),bg = "white")

#The text to display what the pokemon does in the two boxes made previously
Pokemon_Action_Label = Label(canvas_battle,text = "What will \n"+str(Pokemon_Info[0])+" do?",font =("bold",15),bg = "white")
Pokemon_Action_Label.place(x =10,y =270)


#Attack button to bring up the moves your pokemon can do
Pokemon_Attack_Button = Button(canvas_battle,text = "Fight",bg = "tomato",activebackground= "firebrick1",width = 10,command = Pokemon_Attack_Button)
Pokemon_Attack_Button.place(x =280,y =265)


#Button to run away from battle
Run_Away_Button = Button(canvas_battle,text = "run",bg = "steelblue1",activebackground="dodgerblue2",width = 10)
Run_Away_Button.place(x =390,y =295)
#works correctly. when pokemon center made dont reset health to 200 keep the same.all


#Button to access your bag
Bag_Button = Button(canvas_battle,text = "Bag",bg ="orange",activebackground="darkorange1",width = 10)
Bag_Button.place(x =390,y =265)


#Button to access and equip different pokemon
Pokemon_Button = Button(canvas_battle,text = "Pokemon",bg = "forest green",activebackground="dark green",width = 10)
Pokemon_Button.place(x =280,y=295)

#all of the different attacks of your pokemon
Attack_Button1 = Button(canvas_battle,text =moves[0],command =Attack_Button1,width= 10)
Attack_Button1.place(x = 270, y =235)
Attack_Button1.place_forget()

Attack_Button2 = Button(canvas_battle,text =moves[1],command =Attack_Button2,width= 10)
Attack_Button2.place(x = 380, y =265)
Attack_Button2.place_forget()

Attack_Button3 = Button(canvas_battle,text =moves[2],command =Attack_Button3,width= 10)
Attack_Button3.place(x = 380, y =235)
Attack_Button3.place_forget()

Attack_Button4 = Button(canvas_battle,text =moves[3],command =Attack_Button4,width= 10)
Attack_Button4.place(x = 270, y =265)
Attack_Button4.place_forget()




#the foes canvas_battle objects

#the floor your opponents pokemon stands on
Opponent_Pokemon_Floor = canvas_battle.create_oval(50,90,200,150,fill = "green",outline = "dark green",width = 5)
canvas_battle.move(Opponent_Pokemon_Floor,250,0)
canvas_battle.tag_lower(Opponent_Pokemon_Floor)

#box where the opponents pokemon information goes
Oppenents_UI = canvas_battle.create_rectangle(12,12,200,75,fill ="white",outline = "black")

Opponents_Triangle_Pointer = canvas_battle.create_polygon(40,25,40,40,70,40,fill = "white",outline = "black")
canvas_battle.move(Opponents_Triangle_Pointer,160,10)


#opponents pokemon label to show the name of his pokemon
Opponents_Pokemon_Label = Label(canvas_battle,text =Foe_Pokemon_Info[0],font =("bold",13))
Opponents_Pokemon_Label.place(x =18,y =18)


#Opponents pokemon level
Opponents_Pokemon_Level_Label = Label(canvas_battle,text = "Lvl "+str(Foe_Pokemon_Info[5]))
Opponents_Pokemon_Level_Label.place(x =135,y =18)

#placeholder for your opponents health_bar
Oppenents_Health_Placeholder = canvas_battle.create_rectangle(0,0,152,20.5,fill = "black",outline = "black")
canvas_battle.move(Oppenents_Health_Placeholder,20,47)

#Opponents full health
Opponents_Health_Bar = canvas_battle.create_rectangle(0,0,150,19,fill = "red",outline = "red")
canvas_battle.move(Opponents_Health_Bar,21,47.5)




#********************************
#canvas mainmenu

#testing
canvas_battle.pack()
screen.mainloop()
