level = {}

starting_position = (0, 0)

class Map:
  def __init__(self, name, x, y, intro, description)
    self.name = name
    self.x = x
    self.y = y
    self.intro = intro
    self.description = description
  
  def intro_text(self):
    return self.intro

  def adjacent_moves(self):
    north = tile_exists(self.x, self.y - 1).name
    south = tile_exists(self.x , self.y + 1).name
    east = tile_exists(self.x + 1, self.y).name
    west = tile_exists(self.x - 1, self.y).name
    moves = []

    if north != None:
      return moves
  def available_actions(self, **kwargs):
    if kwargs:
      moves = []
      for key, value in kwargs.items():
        if key == "in_battle":
            if value == True:
              pass
        if key == "in_town":
            if value == True:
              print("In town, from available actions")
              pass
      else:
        moves = self.adjacent_moves()
        return moves

class SpawnPoint(Map):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.name = "Spawn"
    self.intro = "A spawin"
    self.description = "Spawn place"
    super().__init__(
      name = self.name,
      x = self.x,
      y = self.y,
      intro = self.intro,
      description = self.description
    )
  
  def modify_player(self, player):
    pass

  

def load_tiles():
  with open("World.txt", "r") as f:
      rows = f.readlines()
    x_max = len(rows[0].split("\t"))
    for y in range(len(rows)):
        cols = rows[y].split("\t")

        try:
          for x in range(x_max):
            title_name = cols[x].replace("\n", "")

              if title_name == "":
                  level[(x, y)] = None
              else:
                  if title_name == "SpawnTile":
                        level[(x, y)] = SpawnTile(x, y)
                        global starting_position
                        starting_position = (x, y)
                    if title_name == "ForestTile":
                        level[(x, y)] = ForestTile(x, y)
                    if title_name == "MountainTile":
                        level[(x, y)] = MountainTile(x, y)
                    if title_name == "PlainsTile":
                        level[(x, y)] = PlainsTile(x, y)
                    if title_name == "FairyTile":
                        level[(x, y)] = FairyTile(x, y)
                    if title_name == "SwampTile":
                        level[(x, y)] = SwampTile(x, y)
                    if title_name == "ForestDungeon":
                        level[(x, y)] = ForestDungeon(x, y)
                    if title_name == "MountainDungeon":
                        level[(x, y)] = MountainDungeon(x, y)
                    if title_name == "PlainsDungeon":
                        level[(x, y)] = PlainsDungeon(x, y)
                    if title_name == "FairyDungeon":
                        level[(x, y)] = FairyDungeon(x, y)
                    if title_name == "SwampDungeon":
                        level[(x, y)] = SwampDungeon(x, y)
        except Exception as e:
            if e == IndexError:
                print("Index done not exist!!")
            else:
                print(e)
                quit()


def title_exist(x, y):
    return level.get((x, y))
