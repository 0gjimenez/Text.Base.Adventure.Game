import items, enemies

class MapTile:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def intro_text(self):
    raise NotImplementedError()
  
  def modify_player(self, player):
    raise NotImplementedError

class StartingTile(MapTile):
  def intro_text(self):
    return ""
    
  def modify_player(self, player):
    #Room has no action on player
    pass
class LootTile(MapTile):
  def __init__(self x, y, item):
    self.item = item
    super().__init__(x, y)
    
  def add_loot(self, player):
    player.inventory.append(self.item)
    
  def modify_player(self, player):
    self.add_loot(player)
    
class EnemyTile(MapTile):
  def __init__(self, x, y, enemy):
    self.enemy = enemy
    super().__init__(x, y)
    
  def modify_player(self, the_player):
    if self.enemy.is_alive():
      the_player.hp = the_player.hp - self.enemy.damage
      print("Enemy does {} damage. Y have {} HP remaining.".format(self.enemy.damge, the_player.hp))

class biome(MapTile):
  def intro_text(self):
    return"""blank"""
  
  def modify_player(self, player):
    pass

class weapons(LootTile):
  def __init__(self, x, y):
    super().__init__(x, y, items.blank())

  def intro_text(self):
    return """ """

class PlainsTile(biome(MapTile)):

class PlainsDungeonTile(EnemyTile):
  super().__init__(x, y, enemies.fillinenemy())

class MountainTile(biome(MapTile)):

class MountainDungeonTile(EnemyTile):
  super().__init__(x, y, enemies.fillinenemy())

class FairyTile(biome(MapTile)):

class FairyDungeonTile(EnemyTile):
  super().__init__(x, y, enemies.fillinenemy())

class ForestTile(biome(MapTile)):

class SwampTile(biome(MapTile)):

class SwampDungeonTile(EnemyTile):
  super().__init__(x, y, enemies.fillinenemy())


_world = {}
starting_position = (0, 0)
  
def load_tiles():
  """Parses a file that describes the world space into the _world object"""
  with open('World.txt', 'r') as f:
    rows = f.readlines()
  x_max = len(rows[0].split('\t')) # Assumes all rows contain the same 
    for y in range(len(rows)):
      cols = rows[y].split('\t')
      for x in range(x_max):
        tile_name = cols[x].replace('\n', '') #Windows users may need to replace '\r\n'
        if tile_name == 'SpawnTile':
          global starting_position
          starting_position = (x, y)
        _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name) (x,y)

def tile_exists(x, y);
    return _world.get((x, y))