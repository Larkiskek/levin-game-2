import draw
from tarakan import Tarakan as T
import random
import player_config

list_enemies = []
list_enemies.append([
0,
[0, 0, 0, 0, 0]
])
#первая комната
list_enemies.append([
1,
[0, 2, 2, 0, 0]
])
#вторая комната
list_enemies.append([
1,
[0, 0, 3, 1, 0]
])
#третья комната
list_enemies.append([
3,
[5, 1, 0, 0, 0],
[0, 0, 3, 3, 0],
[10,1, 0, 1, 0]
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
		self.items = []

	def create_enemies(self, list_enemies):
			self.enemy.generate(self.list_enemies[self.number_wave])
			self.tarakanS = self.enemy.list
			self.number_wave +=1


	def output(self, game):
		if self.time_before_create == 0:
			self.gate.input(game)

	def create_items(self):
		self.list_items  = [
							#   name      №    S   HP   LD   LCD   LR   BD  BCD  BS 
							#   default	       7    3    5    1   100   30   30   5
							['LAZER UP',  0, ( 0,   0,   0,   1,    0,   0,   0,  0  ) ],
							['SPEED UP',  1, ( 1,   0,   0,   0,    0,   0,   0,  0  ) ],
							['BULLET UP', 2, ( 0,   2,   0,   0,    0,   0,   3,  0  ) ],
							['LAZER UP',  3, ( 0,   1,   2,   1,    0,   0,   0,  0  ) ],
							['SPEED UP',  4, ( 0,   0,   0,   0,    0,   7,   2,  1  ) ],
							['BULLET UP', 5, ( 0,   0,   0,   0,    0,   0,   0,  3  ) ],
							['люблю сон', 6, ( 0,   2,   1,   1,    0,   0,   0,  0  ) ]
							]
		for i in range (0, 2):
			number = random.randint(0, 6-i)
			item = self.list_items[ number ]
			item.append((win_wight +200*i-100, win_hight))  
			self.items.append(item)
			del self.list_items[number]

	def items_check(self, player):
		for item in self.items:
			x = item[3][0]
			y = item[3][1]
			if ( abs(player.x - x) < (25 + player.size) ) and ( abs(player.y - y) < (25 + player.size) ):
				player.speed += item[2][0]
				player.health += item[2][1]				
				player.lazer_characters['damage'] += item[2][2]
				player.rate_of_lazer_fire += item[2][3]
				player.lazer_characters['lenght'] += item[2][4]
				player.bullet_characters['damage'] += item[2][5]
				player.shoot_cd_max -= item[2][6]
				if player.shoot_cd_max < 1:
					player.shoot_cd_max = 1
				player.bullet_characters['speed'] += item[2][7]
				self.items = []
				player.lazer = player_config.Lazer(player)






class Gate():
	def __init__ (self):
		self.size = 100 
		self.wight = 10
		self.coordinates = (0, 500-self.size, 2*self.wight, 2*self.size)
		self.victory = 0

	def input(self, game):
		self.coordinates = (2*win_wight -10 -self.wight, win_hight-self.size, 2*self.wight, 2*self.size )
		if ( game.player.x + game.player.size >= 2*win_wight -10 ) and ( game.player.y + game.player.size - self.size < win_hight ) and ( game.player.y - game.player.size + self.size > win_hight ):
			game.parameter = 'New room'
			game.player.x = game.player.size + 10


class Enemies():
	def __init__(self):
		     #   [ type, wight, hight,  HP,  speed,       color,     jump_duration,  jump_cd, jump_speed,  shift_x, shift_y]
		self.S  = (  0,     40,    40,   50,     2,    (   0, 255, 0),       40,          100,       10,      0,      0    )
		self.M  = (  1,     70,    70,  100,     3,    ( 255, 165, 0),        0,          500,       0,       0,      0    )
		self.L  = (  2,    100,    80,  200,     4,    ( 255,  69, 0),        0,          100,       0,       0,      0    )
		self.XL = (  3,    200,   200,  500,     4,    ( 139,   0, 0),       40,          500,       4,       0,      0    )
		self.BOSS=(  4,    550,   500, 3000,   2.5,    ( 139,  69,19),        0,          500,       0,       0,     30   )
		self.characters = [self.S, self.M, self.L, self.XL, self.BOSS]

		self.list = []

	def generate(self, set):
		for i in range (0, 5):
			for j in range (0, set[i]):
				x = win_wight
				y = win_hight
				while ((abs(x-win_wight) < 100) and (abs(y-win_hight) < 100)): 
					x = random.randint(70, (2*win_wight - 70))
					y = random.randint(170,(2*win_hight - 70))
				self.list.append( T(x, y, self.characters[i]))



