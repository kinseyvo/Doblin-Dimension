from random import randint, randrange
from combat import cool_combat
import randomEnemy
from time import sleep

def level(my_player):
  '''Method that makes a level with random number of tiles to advance and randomly calls combat'''
  #Level 1,2,3
  i = 1
  while my_player.health > 0 and i != 4:
    print(f"\n\n------LEVEL {i}------")
  
    tiles = randrange(4,9,1)
    
    if i == 1:
      location = "Jungle"
    elif i == 2:
      location = "Factory"
      tiles = tiles + i * 2
    elif i == 3:
      location = "Abyssal Plains"
      tiles = tiles + i * 2
      
    print(f"You are now in The {location}")
    
    
    while (tiles > 0 and my_player.health > 0):
      print(f"\n**Spaces left to move: {tiles}**\n")
      sleep(0.45)
      the_enemy = randomEnemy.random_enemy_generator()
      fight_chance = randint(0,1)
      
      if fight_chance == 1:
        sleep(0.5)
        print(f"\nIt's a surprise attack! The {the_enemy.name} has spotted you!\n")
        sleep(0.65)
        print(f"It has {the_enemy.health} HP!\n")
        sleep(0.65)
        print("What will you do?")
        while the_enemy.health > 0 and my_player.health > 0:
          
          cool_combat(my_player, the_enemy)
          if my_player.health > 0:
            print("\nYou advance a space")
        if(my_player.health <= 0):
          print("\n\nGAME OVER!") #GAME OVER
        else:
          tiles = tiles - 1
      else:
        print("No enemy, you advance a space\n")
        tiles = tiles - 1
        sleep(0.5)
    i += 1