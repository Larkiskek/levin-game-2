import socket

class Server():
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(('', 9095)) # номер порта ( хост пустой )
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
		if True:
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
			self.close()


	def close(self):
		self.conn.close()
		print('close')



class Client():
	def __init__(self, host):
		self.sock = socket.socket()
		self.sock.connect((host, 9095))

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
		if True:
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
			self.close()

	def send(self, data):
		self.sock.send((str(data) + '\n').encode())


	def close(self):
		self.sock.close()
		print('close')

