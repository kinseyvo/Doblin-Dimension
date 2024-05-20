from time import sleep

class Player():
    def __init__(self):
        self.classType = ""
        self.name = ""
        self.health = 0
        self.weapon = 0
        self.attack = 0
        self.defense = 0
        self.crit_chance = 0
        self.potion = 2
      
    def defend(self):
        self.defense = self.defense * 2
    def reset_defense(self):
        self.defense //= 2  

    def classChoice(self):
       print("What is Your Name?\n\n")
       self.name = input('>')
       if not (self.name):
         self.name = "Tuffy"
       print("What class would you like to play as? There is the Knight, Assassin, and the Mage.\n")
       print("1. Knight\n2. Assassin\n3. Mage\n")
       x = input()
       x = x.lower()
    
       if x == "1" or x == "knight":
         self.classType = "Knight"
         return Knight(self.classType,self.name,self.potion)
        
        
       elif x == "assassin" or x == "2":
         self.classType = "Assassin"
         return Assassin(self.classType,self.name,self.potion)
        
        
       elif x == "mage" or x == "3":
         self.classType = "Mage"
         return Mage(self.classType,self.name,self.potion)
        
        
       else:
         print("Try Again: ")
         self.classChoice();


class Enemy(Player):
  def __init__(self, health, attack, name, defense):
    self.health = health
    self.attack = attack
    self.name = name
    self.defense = defense

class Knight(Player):
  def __init__(self, classType, name, potion):
    self.classType = classType
    self.name = name
    self.health = 100
    self.weapon = "sword"
    self.attack = 15
    self.defense = 8
    self.crit_chance = 5
    self.potion = potion

class Assassin(Player):
  def __init__(self, classType, name, potion):
    self.classType = classType
    self.name = name
    self.health = 50
    self.weapon = "daggers"
    self.attack = 20
    self.defense = 5
    self.crit_chance = 50
    self.potion = potion
    

class Mage(Player):
  def __init__(self, classType, name, potion):
    self.classType = classType
    self.name = name
    self.health = 70
    self.weapon = "staff"
    self.attack = 30
    self.defense = 1
    self.crit_chance = 60
    self.potion = potion