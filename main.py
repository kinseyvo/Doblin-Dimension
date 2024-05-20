from starterFunctions import animated_marker, levelLoad
from player import*
from level import level
from time import sleep

"""def classChoice_test():
      print("What is Your Name?\n\n")
      name = input('>')
      if not (name):
        name = "Tuffy"
      print("What class would you like to play as? There is the Knight, Assassin, and the Mage.\n")
      print("1. Knight\n2. Assassin\n3. Mage\n")
      x = input()
      x = x.lower()
    
      if x == "1" or x == "knight":
        return Knight(classType = x, name = name, potion = 2)
        
      elif x == "assassin" or x == "2":
        return Assassin(self.classType,self.name,self.potion)
        
      elif x == "mage" or x == "3":
        return Mage(self.classType,self.name,self.potion)
        
      else:
        print("Try Again: ")
        classChoice_test();
"""

def main():
    
    animated_marker()
    
    print("\nHi, Welcome to Doblin Dimension!")
    #my_player = classChoice_test()
    my_player = Player()
    my_player = Player.classChoice(my_player)
    
    
    print(f"Now, {my_player.classType} {my_player.name}, you are now ready for adventure!\n")
    
    
    levelLoad()
    
    #Level 1-3
    level(my_player)
    
    if my_player.health > 0:
      print("Congratualtions, You've Won!")
    
    
if __name__ == "__main__":
  main()