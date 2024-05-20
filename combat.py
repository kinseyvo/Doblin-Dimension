from starterFunctions import healingAnimation
from random import randrange
from time import sleep

def cool_combat(player, enemy):

  while player.health > 0 and enemy.health > 0:
    while True:
      option = input("\nBattle Menu: \n Attack \t Defend\n Heal \t\t Run\n\n >").lower()
      print('\n')
      
      if option not in("attack", "defend", "heal", "run"):
        print("Not a valid option")
      else:
        break
    if (option == "attack"):
      
      if ((randrange(1,4,1)) == 3):
        print(f"\nThe {enemy.name} has Dodged your Attack\nHe Counter-Attacks!")
        player.health = player.health - enemy.attack
        if player.health > 0:
          print(f"\nPlayers's Health is Now: {player.health}")
        else:
          print("You Have Suffered a Fatal Blow... You slowly begin to loss consciousness and your life slowly flashes before your eyes...")
        
      else:
        sleep(0.4)
        print(f"{attackNames(player, enemy)}")
        enemy.health = enemy.health - player.attack
        if enemy.health > 0:
          print(f"\nEnemy's Health is Now: {enemy.health}")
          sleep(0.4)
        else:
          print(f"Congrats! {enemy.name} has been defeated!")
          break
        
    elif (option == "defend"):
      player.defend()
      if (player.defense < enemy.attack):
        damage = enemy.attack - player.defense
        player.health = player.health - damage
        print(f"You defended the {enemy.name}'s attack!")
        if player.health > 0:
          print(f"\nPlayers's Health is Now: {player.health}")
        else:
            print("You Have Suffered a Fatal Blow... You slowly begin to loss consciousness and your life slowly flashes before your eyes...") 
      else:
         print("You took 0 damage.")
      player.reset_defense()
    
    elif (option == "heal"):
        if player.potion > 0:
          healingAnimation()
          print("\n")
          player.health += 20
          player.potion -= 1
          print(f"Players's Health is Now: {player.health}")
          sleep(0.45)
          print(f"You have {player.potion} left")
        else:
          print("You are out of potions!")

    elif (option == "run"):
      if ((randrange(1,6,1)) == 2):
        print("You Got Away From the Fight! Hurray!")
        enemy.health = 0
      else:
        enemy.attack = enemy.attack + 5
        print(f"You weren't able to get away and the {enemy.name} is now ENRAGED!!! Enemy Attacked Increased to {enemy.attack}")
        sleep(0.5)
        if ((randrange(1,6,1)) == 3):
          print(f"\nThe {enemy.name} Strikes Back at You! \n As You Try to Run Away...\n")
          player.health = player.health - enemy.attack
          if player.health > 0:
            print(f"\nPlayers's Health is Now: {player.health}")
            sleep(0.5)
          else:
            print("You Have Suffered a Fatal Blow... You slowly begin to loss consciousness and your life slowly flashes before your eyes...")
    

def attackNames(player, enemy):
    attacks = [f"You struck the {enemy.name}'s shoulder with your {player.weapon}!", f"You struck the {enemy.name}'s right flank with your {player.weapon}!", f"You struck the {enemy.name}'s chest with your {player.weapon}!", f"You pierced the {enemy.name}'s lower flank with your {player.weapon}!"]
    rand_idx = randrange(len(attacks))
    random_attack = attacks[rand_idx]
    return random_attack