import draw
from tarakan import Tarakan as T
import random
import player_config
import math

import pygame

list_enemies = []
list_enemies.append([
0
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



class Map():
	def __init__ (self, diff):
		self.max_map_size = 11
		self.rooms = []
		self.now_location = [(self.max_map_size // 4)*2+1, (self.max_map_size // 4)*2+1]
		self.the_way = []
		self.next_room = [[1,0],[-1,0],[0,1],[0,-1]]
		self.level = diff
		self.mini_map = 1
		self.mini_map_time = 0

	def create_map(self):
		self.create_lattice()
		for i in range (0, 3):
			self.add_room('GOLD')
		self.add_room('BOSS')
		self.closing()



	def create_lattice(self):
		for i in range (0, self.max_map_size):
			self.rooms.append([])
			for j in range (0, self.max_map_size):
				self.rooms[i].append([])
				if (i == 0) or (j == 0) or (i == self.max_map_size-1) or (j == self.max_map_size-1) :
					self.rooms[i][j]= dict(status = 'close')
				elif i%2 == 1:
					self.rooms[i][j]= dict(status = 'maybe open')
				elif j%2 == 1:
					self.rooms[i][j]= dict(status = 'close')
				else:
					self.rooms[i][j]= dict(status = 'maybe open')
		self.rooms[self.now_location[0]][self.now_location[1]]['status'] = 'open'


	def add_room(self, name):
		while True:
			self.now_location[0] = random.randint(1, self.max_map_size-1)
			self.now_location[1] = random.randint(1, self.max_map_size-1)
			while self.rooms[self.now_location[0]][self.now_location[1]]['status'] != 'open':
				self.now_location[0] = random.randint(1, self.max_map_size-1)
				self.now_location[1] = random.randint(1, self.max_map_size-1)
			for j in range (0, 3):
				self.create_the_next_room() 
				if self.rooms[self.now_location[0]][self.now_location[1]]['status'] != 'maybe open':
					self.welcome_back()
					break
			if self.rooms[self.now_location[0]][self.now_location[1]]['status'] == 'maybe open':
				neighbors = 0
				for j in range (0, 4):
					if self.rooms[self.now_location[0]+self.next_room[j][0]][self.now_location[1]+self.next_room[j][1]]['status'] == 'open':
						neighbors += 1
				if neighbors == 1:
					self.rooms[self.now_location[0]][self.now_location[1]]['status'] = name
					self.the_way = []	
					break
				else:
					self.welcome_back()

	def create_the_next_room(self):
		delta = random.randint(0,3)
		self.rooms[self.now_location[0]][self.now_location[1]]['status'] = 'open'
		self.rooms[self.now_location[0]][self.now_location[1]]['difficalty'] = -1
		while self.rooms[self.now_location[0]+self.next_room[delta][0]][self.now_location[1]+self.next_room[delta][1]]['status'] == 'close':
			delta = random.randint(0,3)
		self.now_location[0] += self.next_room[delta][0]
		self.now_location[1] += self.next_room[delta][1]
		self.the_way.append(delta)
		

	def welcome_back(self):
		for i in range (0, len(self.the_way)):
			delta = self.the_way[len(self.the_way)- i-1]
			self.now_location[0] -= self.next_room[delta][0]
			self.now_location[1] -= self.next_room[delta][1]
			self.rooms[self.now_location[0]][self.now_location[1]]['status'] = 'maybe open'
		self.rooms[self.now_location[0]][self.now_location[1]]['status'] = 'open'
		self.the_way = []	


	def closing(self):
		self.now_location = [(self.max_map_size // 4)*2+1, (self.max_map_size // 4)*2+1]
		self.rooms[self.now_location[0]][self.now_location[1]]['difficalty'] = self.level
		self.difficalty(self.now_location[0], self.now_location[1])
		for i in range (0, self.max_map_size):
			for j in range (0, self.max_map_size):
				if self.rooms[i][j]['status'] == 'maybe open':
					self.rooms[i][j]['status'] = 'close'
				if self.rooms[i][j]['status'] == 'open':
					diff = self.rooms[i][j]['difficalty']
					self.rooms[i][j]['enemies']= [1, 
						[random.randint(0, 2*diff),
						random.randint(0, diff//2),
						random.randint(0, diff//3),
						random.randint(0, diff//3),
						0]]
				elif self.rooms[i][j]['status'] == 'BOSS':
					self.rooms[i][j]['enemies'] = [1, [0, 0, 0, 0, 1]]
				else :
					self.rooms[i][j]['enemies'] = [0]
		self.rooms[self.now_location[0]][self.now_location[1]]['status'] = 'open'
		self.rooms[self.now_location[0]][self.now_location[1]]['enemies'][0] = 0

	def difficalty(self, x, y):
		for i in range (0, 4):
			if self.rooms[x+self.next_room[i][0]][y+self.next_room[i][1]]['status'] == 'open':
				if self.rooms[x+self.next_room[i][0]][y+self.next_room[i][1]]['difficalty'] == -1:
					self.rooms[x+self.next_room[i][0]][y+self.next_room[i][1]]['difficalty'] = self.rooms[x][y]['difficalty'] + 1
					self.difficalty(x+self.next_room[i][0], y+self.next_room[i][1])	

	
		


	def print_map(self):
		for i in range (0, self.max_map_size):
			for j in range (0, self.max_map_size):
				print(self.rooms[i][j]['status'], self.rooms[i][j]['enemies'])
			print('\n')













class Room():
	def __init__ (self, data):
		self.gate = Gate()
		self.time_before_create_max = 50
		self.time_before_create = 2*self.time_before_create_max

		self.number_wave = 1
		self.list_enemies = data['enemies']
		self.enemy = Enemies()
		self.tarakanS = []
		self.items = []
		self.status = data['status']

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
							['SPEED UP',  1, ( 5,   0,   0,   0,    0,   0,   0,  0  ) ],
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

	def items_check(self, player, room):
		for item in self.items:
			x = item[3][0]
			y = item[3][1]
			if ( abs(player.x - x) < (25 + player.size) ) and ( abs(player.y - y) < (25 + player.size) ):
				player.taken_items.append(item[1])
				player.taken_items[0] += 1
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
				room['status'] = 'open'



class Gate():
	def __init__ (self):
		self.size = 100 
		self.wight = 10
		self.coordinates = [
			(2*win_wight -10, win_hight-self.size, 2*self.wight, 2*self.size ),
			(10, win_hight-self.size, 2*self.wight, 2*self.size),
			(win_wight-self.size, 2*win_hight-50, 2*self.size, 2*self.wight),
			(win_wight-self.size, 50, 2*self.size, 2*self.wight)]

		self.victory = 0

	def input(self, game):
		if ( game.player.x + game.player.size >= 2*win_wight -10 ) and ( abs(game.player.y - win_hight) < self.size - game.player.size ) and (game.map.rooms[game.map.now_location[0]+1][game.map.now_location[1]]['status'] != 'close'):
			game.map.now_location[0] += 1
			game.player.x = game.player.size + 50
			game.parameter = 'New room'
		if ( game.player.x - game.player.size <= 10 ) and ( abs(game.player.y - win_hight) < self.size - game.player.size ) and (game.map.rooms[game.map.now_location[0]-1][game.map.now_location[1]]['status'] != 'close'):
			game.map.now_location[0] -= 1
			game.player.x = 2*win_wight- game.player.size - 50
			game.parameter = 'New room'
		if ( abs(game.player.x - win_wight) < self.size - game.player.size ) and ( game.player.y + game.player.size >= 2*win_hight -50 ) and (game.map.rooms[game.map.now_location[0]][game.map.now_location[1]+1]['status'] != 'close'):
			game.map.now_location[1] += 1
			game.player.y = game.player.size + 150
			game.parameter = 'New room'
		if ( abs(game.player.x - win_wight) < self.size - game.player.size ) and ( game.player.y - game.player.size <= 50 ) and (game.map.rooms[game.map.now_location[0]][game.map.now_location[1]-1]['status'] != 'close'):
			game.map.now_location[1] -= 1
			game.player.y = 2*win_hight - game.player.size - 150
			game.parameter = 'New room'


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



def dr_map(x, y, win):
	the_map = Map()
	the_map.create_map()
	for i in range (0, the_map.max_map_size):
		for j in range (0, the_map.max_map_size):
			if the_map.rooms[i][j]['status'] == 'open':
				pygame.draw.rect(win, (255, 255, 255), (2*win_wight-200+i*15-x, 50+j*15+y, 15, 15))
			elif the_map.rooms[i][j]['status'] == 'GOLD' :
				pygame.draw.rect(win, (255, 255, 0), (2*win_wight-200+i*15-x, 50+j*15+y, 15, 15))
			elif the_map.rooms[i][j]['status'] == 'BOSS':
				pygame.draw.rect(win, (0, 0, 0), (2*win_wight-200+i*15-x, 50+j*15+y, 15, 15))
			else:
				pygame.draw.rect(win, (200, 200, 200), (2*win_wight-200+i*15-x, 50+j*15+y, 15, 15))
	pygame.draw.rect(win, (255, 0, 0), (2*win_wight-200-x+the_map.now_location[0]*15+5, 50+y+the_map.now_location[1]*15+5, 5, 5))


def test_map():
	win = pygame.display.set_mode((2*win_wight, 2*win_hight))
	#the_map = Map()
	#the_map.create_map()
	while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
		win.fill((240, 255 ,255))
		#pygame.time.delay(100)
		for i in range (0, 5):
			for j in range (0, 5):
				dr_map(200*i, 200*j, win)
		#dr_map(500, 0, win, the_map)
		#if pygame.key.get_pressed()[pygame.K_UP]:
			#the_map.add_room('GOLD')
		#if pygame.key.get_pressed()[pygame.K_DOWN]:
			#the_map.welcome_back()
		pygame.display.update()
		for i in range (0, 10000):
			pygame.time.delay(10)	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()



