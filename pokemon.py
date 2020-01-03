import math

class Pokemon:
  def __init__(self, name, health, ptype, level):
    self.name = name
    self.type = ptype
    self.level = level
    self.health = health
    self.max_health = level * 10
    self.is_knocked_out = False
    
  def lose_health(self, health_lost):
    self.health -= health_lost
    if self.health <= 0:
      self.health = 0
      self.knock_out()
    print("{name} now has {health} health.".format(name = self.name, health = self.health))
      
  def regain_health(self, health_gain):
    self.health += health_gain
    if self.health > self.max_health:
      self.health = self.max_health
    print("{name} now has {health} health.".format(name = self.name, health = self.health))
  
  def knock_out(self):
    self.is_knocked_out = True
    print("{name} is now knocked out".format(name = self.name))
    
  def revive(self):
    if self.is_knocked_out == True:
      self.is_knocked_out = False
      print("{name} is revived!".format(name = self.name))
    else:
      print("{name} is not knocked out and does not need reviving!".format(name = self.name))
      
  def attack(self, other_poke):
    if self.is_knocked_out == False:
      other_type = other_poke.type
      if self.type == "Fire" and other_type == "Fire":
        damage_mult = 1
      elif self.type == "Grass" and other_type == "Grass":
        damage_mult = 1
      elif self.type == "Water" and other_type == "Water":
        damage_mult = 1
      elif self.type == "Fire" and other_type == "Grass":
        damage_mult = 2
      elif self.type == "Grass" and other_type == "Fire":
        damage_mult = 0.5
      elif self.type == "Grass" and other_type == "Water":
        damage_mult = 2
      elif self.type == "Water" and other_type == "Grass":
        damage_mult = 0.5
      elif self.type == "Water" and other_type == "Fire":
        damage_mult = 2
      elif self.type == "Fire" and other_type == "Water":
        damage_mult = 0.5

      damage_dealt = math.ceil(damage_mult * self.level)
      print("{attack_poke} deals {damage_dealt} damage to {def_poke}!".format(attack_poke = self.name, damage_dealt = damage_dealt, def_poke = other_poke.name))
      other_poke.lose_health(damage_dealt)
    
class Trainer:
  def __init__(self, name, potions, pokemons, current_pokemon):
    self.name = name
    self.potions = potions
    if len(pokemons) <= 6:
      self.pokemons = pokemons
    self.current_pokemon = current_pokemon
    
  def use_potion(self, potion):
    if self.potions.get(potion):
      poke_to_heal = self.pokemons[self.current_pokemon]
      poke_to_heal.regain_health(self.potions[potion])
      if poke_to_heal.health > poke_to_heal.max_health:
        poke_to_heal.health = poke_to_heal.max_health
      print("{name} was healed by {potion} for {heal_hp} hp and now has {health} hp".format(name = poke_to_heal.name, potion = potion, heal_hp = self.potions[potion], health = poke_to_heal.health))
  
  def attack_trainer(self, other_trainer):
    their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
    attack_poke = self.pokemons[self.current_pokemon]
    print("{}'s {} has attacked {}'s {}".format(self.name, attack_poke.name, other_trainer.name, their_pokemon.name))
    attack_poke.attack(their_pokemon)
    
  def switch_pokemon(self, new_pokemon):
    if new_pokemon < len(self.pokemons) and self.pokemons[new_pokemon].is_knocked_out == False:
      self.current_pokemon = new_pokemon

charzard = Pokemon("Charzard", 20, "Fire", 3)
blastoise = Pokemon("Blastoise", 100, "Water", 10)
leafeon = Pokemon("Leafeon", 79, "Grass", 9)
bulbasaur = Pokemon("Bulbasaur", 40, "Water", 4)

dylan = Trainer("Dylan", {"healx": 20, "healy": 40}, [charzard, blastoise], 0)

nick = Trainer("Nick", {"healz": 50}, [leafeon, bulbasaur], 0)

nick.use_potion("healz")
nick.switch_pokemon(1)

dylan.attack_trainer(nick)

    
  