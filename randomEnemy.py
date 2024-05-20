import random
from player import Enemy

def random_enemy_generator():
  """This code is intended to make random enemies, can have weighted values"""
  enemyList = ["Goblin", "Doblin", "Orc", "Troll", "Elf"]
  randomEnemy = random.choices(enemyList, weights=(20, 10, 2, 5, 2), k=1)
  randomEnemy = randomEnemy[0]
  if randomEnemy == "Goblin":
    return Enemy(health = random.randint(20,30), attack = random.randint(5,10),  name = randomEnemy, defense = random.randint(1,4))
  elif randomEnemy == "Doblin":
    return Enemy(health = random.randint(40,60), attack = random.randint(10,20), name = randomEnemy, defense = random.randint(2,8))
  elif randomEnemy == "Orc":
    return Enemy(health = random.randint(100,110), attack = random.randint(100,150), name = randomEnemy, defense = random.randint(20,25))
  else:
    return Enemy(health = 30, attack = 10, name = randomEnemy, defense = 5)