import socket
from tarakan import Tarakan as T
import pygame

class Server():
	def __init__(self):
		self.status = 'server'
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,  socket.IPPROTO_TCP)
		self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		self.sock.bind(('', 9091)) # номер порта ( хост пустой )
		self.sock.listen(1) # количество подключений
		(self.conn, self.addr) = self.sock.accept()
		#print( 'connected: ', self.addr)

	def get(self):
		data = ''
		while True:
			char = self.conn.recv(1)
			if not char:
				break
			char = char.decode()
			if char == '\n':
				break
			data += char
		return data


	def send(self, data):
		self.conn.send((str(data) + '\n').encode())

	def send_save(self, player, maps):
			self.send(player.health)
			self.send(len(player.taken_items))
			for item in player.taken_items:
				self.send(str(item) + '\n')
			self.send(maps.now_location[0])
			self.send(maps.now_location[1])
			self.send(player.x)
			self.send(player.y)
			for i in range (0, maps.max_map_size):
				for j in range (0, maps.max_map_size):
					room = maps.rooms[i][j]
					self.send( room['status'])
					self.send( room['enemies'][0])
					for k in range (0, room['enemies'][0]):
						for l in range (0, 5):
							self.send( room['enemies'][k+1][l])


	def change_data(self, game):
		#time0 = pygame.time.get_ticks()
		#time = pygame.time.get_ticks()
		game.player2.keys_dinamics(self.get())
		game.player2.x = int(self.get())
		game.player2.y = int(self.get())
		#time4 = pygame.time.get_ticks() - time
		#timestrsend = ''
		self.send(game.using_keys)
		self.send(game.player.x)
		self.send(game.player.y)
		#time1 = pygame.time.get_ticks() - time0
		#time = pygame.time.get_ticks()

		self.send(game.player2.health)

		self.send(len(game.room.tarakanS))
		for tar in game.room.tarakanS:
			self.send(tar.x)
			self.send(tar.y)
			self.send(tar.type)
		#time2 = pygame.time.get_ticks() -time
		
		#self.send(game.parameter)
		'''
		timesum = pygame.time.get_ticks() - time0
		print('server')
		print('get keys: ', time1)
		print('get len:  ', time2)
		print('send:     ', timestrsend)
		print('send keys:', time4)
		print('sum:      ', timesum, '\n')
		'''


	def close(self):
		self.conn.close()
		print('close')



class Client():
	def __init__(self, host):
		self.status = 'client'
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,  socket.IPPROTO_TCP)
		self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		self.sock.connect((host, 9091))

	def get(self):
		data = ''
		while True:
			char = self.sock.recv(1)
			if not char:
				break
			char = char.decode()
			if char == '\n':
				break
			data += char
		return data



	def get_save(self, player, maps):
			player.health = int(self.get())
			lenght =  int(self.get())
			for i in range (0, lenght):
				player.get_item(scene.list_items[int(self.get())])
			maps.now_location[0] = int(self.get())
			maps.now_location[1] = int(self.get())
			player.x = int(self.get())
			player.y = int(self.get())
			for i in range (0, maps.max_map_size):
				for j in range (0, maps.max_map_size):
					maps.rooms[i][j]['status'] = self.get()
					maps.rooms[i][j]['enemies'] = [0]
					maps.rooms[i][j]['enemies'][0] = int(self.get())
					for k in range (0, maps.rooms[i][j]['enemies'][0]):
						maps.rooms[i][j]['enemies'].append([0, 0, 0, 0, 0])
						for l in range (0, 5):
							maps.rooms[i][j]['enemies'][k+1][l] = int(self.get())

	def change_data(self, game):
		#time0 = pygame.time.get_ticks()
		#time = pygame.time.get_ticks()
		self.send(game.using_keys)
		self.send(game.player.x)
		self.send(game.player.y)
		#time4 = pygame.time.get_ticks() - time
		#timestrget = ''
		#timestrassign = ''
		game.player2.keys_dinamics(self.get())
		game.player2.x = int(self.get())
		game.player2.y = int(self.get())
		game.player.health = int(self.get())
		#time1 = pygame.time.get_ticks() - time0
		#time = pygame.time.get_ticks()
		lenght = int(self.get())
		#time2 = pygame.time.get_ticks() -time
		if lenght == len(game.room.tarakanS):
			#случай, когда никого не удалили
			for tar in game.room.tarakanS:
				#time = pygame.time.get_ticks()
				tar.x = int(self.get()) #int(self.get())
				tar.y = int(self.get()) #int(self.get())
				self.get()
				#timestrassign += str(pygame.time.get_ticks() - time) + ' '
		else:
			game.room.tarakanS = []
			for i in range(0, lenght):
			#а вот тут удалили:
				game.room.tarakanS.append(T(int(self.get()), #координата x
					int(self.get()),                         #координата y
					game.room.enemy.characters[int(self.get())])) #тип врага
		#game.parameter = self.get()
		'''
		timesum = pygame.time.get_ticks() - time0
		print('client')
		print('get keys: ', time1)
		print('get len:  ', time2)
		print('get:      ', timestrget)
		print('assign:   ', timestrassign)
		print('send keys:', time4)
		print('sum:      ', timesum, '\n')
		'''

	def send(self, data):
		self.sock.send((str(data) + '\n').encode())


	def close(self):
		self.sock.close()
		#print('close')

'''
def sr():
	s = Server()
	for i in range(0, 3):
		s.send(input())
		print(s.get())
	s.close()

def cl(addr):
	c= Client(addr)
	for i in range(0, 3):
		print(c.get())
		c.send(input())
	c.close()

#cl('46.242.65.11')
sr()
'''