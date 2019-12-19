import draw
from tarakan import Tarakan as T
import random


list_enemies = []
list_enemies.append([
0,
[0, 0, 0, 0, 0]
])
#первая комната
list_enemies.append([
3,
[0, 2, 2, 0, 0],
[0, 0, 3, 1, 0],
[3, 1, 0, 0, 0]
])
#вторая комната
list_enemies.append([
1,
[0, 0, 3, 1, 0]
])
#третья комната
list_enemies.append([
1,
[3, 1, 0, 0, 0]
])
#Босс - комната
list_enemies.append([
1,
[0, 0, 0, 0, 1]
])










win_wight = 500
win_hight = 500









class Room():
	def __init__ (self, i):
		self.number = i
		self.gate = Gate()
		self.time_before_create_max = 50
		self.time_before_create = 2*self.time_before_create_max

		self.number_wave = 1
		self.list_enemies = list_enemies[self.number]
		self.enemy = Enemies()
		self.tarakanS = []

	def create_enemies(self, list_enemies):
			self.enemy.generate(self.list_enemies[self.number_wave])
			self.tarakanS = self.enemy.list
			self.number_wave +=1


	def output(self, game):
		if self.time_before_create == 0:
			self.gate.input(game)

	def items():
		pass





class Gate():
	def __init__ (self):
		self.size = 100 
		self.wight = 10
		self.coordinates = (0, 500-self.size, 2*self.wight, 2*self.size)
		self.victory = 0

	def input(self, game):
		self.coordinates = (2*win_wight -10 -self.wight, win_hight-self.size, 2*self.wight, 2*self.size )
		if ( game.player.x + game.player.half_wight >= 2*win_wight -10 ) and ( game.player.y + game.player.half_hight - self.size < win_hight ) and ( game.player.y - game.player.half_hight + self.size > win_hight ):
			game.parameter = 'New room'
			game.player.x = game.player.half_wight + 10


class Enemies():
	def __init__(self):
		     #   [ type, wight, hight,  HP,  speed,       color,     jump_duration,  jump_cd, jump_speed]
		self.S  = (  0,     40,    40,   50,     2,    (   0, 255, 0),       40,          100,       10)
		self.M  = (  1,     60,    60,  100,     3,    ( 255, 165, 0),        0,          500,       0 )
		self.L  = (  2,     80,    80,  200,     4,    ( 255,  69, 0),        0,          100,       0 )
		self.XL = (  3,    120,   120,  500,     3,    ( 139,   0, 0),       40,          500,       4 )
		self.BOSS=(  4,    500,   500, 3000,     2,    ( 139,  69,19),        0,            0,       0 )
		self.characters = [self.S, self.M, self.L, self.XL, self.BOSS]

		self.list = []

	def generate(self, set):
		for i in range (0, 5):
			for j in range (0, set[i]):
				x = win_wight
				y = win_hight
				while ((abs(x-win_wight) < 100) and (abs(y-win_hight) < 100)): 
					x = random.randint(70, (win_wight - 70))
					y = random.randint(170,(win_hight - 70))
				self.list.append( T(x, y, self.characters[i]))


class Item():
	def __init__(self):
		pass

