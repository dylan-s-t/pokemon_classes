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
    print("{name} now has {health} health".format(name = self.name, health = self.health))
      
  
  def regain_health(self, health_gain):
    self.health += health_gain
    print("{name} now has {health} health".format(name = self.name, health = self.health))
  
  def knock_out(self):
    self.is_knocked_out = True
    print("{name} is now knocked out".format(name = self.name))
    
  def revive(self):
    if self.is_knocked_out == True:
      self.is_knocked_out = False
      print("{name} is revived!".format(name = self.name))
    else:
      print("{name} is not knocked out and does not need reviving!".format(name = self.name))
    
    
  