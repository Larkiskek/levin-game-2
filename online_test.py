import socket
from multiprocessing import Process, Lock

class Exchanger():
	#описание общих методов обмена информацией, характерных для обоих последующих классов
	def __init__(self, destination):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.destination = destination
		self.relevance = dict()
		self.actually_actions = dict()


	def encoder(self, data):
		string = ''
		for word in data:
			string += str(word) + ' '
		return string.encode('utf-8')


	def decoder(self, string):
		data = []
		word = ''
		for char in string.decode('utf-8'):
			if char != ' ':
				word += char
			elif word != '':
				try:
					word = int(word)
				except ValueError:
					None
				finally:
					data.append(word)
					word = ''
		return data


	def relevance_check(self, msg):
		#print(msg)
		key = msg[0]
		msg.pop(0)
		try:
			if msg[0] > self.relevance[key]:
				self.relevance[key] = msg[0]
				relevance = True
			else:
				#print(msg[1], self.relevance[msg[0]])
				#print('outdated')
				relevance = False
		except KeyError:
			#print('Нетути таких имён: ', key)
			self.relevance[key] = msg[0]
			relevance  = True
		finally:
			msg.pop(0)
			if relevance:
				self.actually_actions[key] = msg
			return key


	def quick_get(self):
		self.sock.settimeout(0.001)
		#print('Not yet')
		try:
			(data, destination) = self.sock.recvfrom(1024)
		except socket.timeout:
			return ['empty']
			#print('emp')
		else:
			data = self.decoder(data)
			#print(data)
			if data[0] == 'confirm':
				data.pop(0)
				#print('YES!!!')
				#print(destination)
				#print('YYESS?')
				self.sock.sendto(self.encoder(['check', data[0], data[1]]), destination)
				#print([data[0], data[1]], 'control answer')
			if data[0] == 'connect':
				self.destination = destination
			if data[0] != 'check':
				return self.relevance_check(data) 
			else:
				return data
			#print(data)


	def long_get(self, key):
		data = 'empty'
		while data != key:
			data = self.quick_get()
		return  data


	def quick_send(self, array):
		try:
			if array[0] != 'check':
				self.relevance[array[0]] += 1
		except KeyError:
			self.relevance[array[0]] = 1
		finally:
			array.insert(1, self.relevance[array[0]])
			self.sock.sendto(self.encoder(array), self.destination)
			#print(array)

		#print('sended')

	def long_send(self, array):
		try:
			self.relevance[array[0]] += 1
		except KeyError:
			self.relevance[array[0]] = 1
		finally:
			array.insert(0, 'confirm')
			array.insert(2, self.relevance[array[1]])
			control_answer = ['check', array[1], array[2]]
			answer = ['empty']
			array = self.encoder(array)
			#print('send long send', array)

			while answer != control_answer:
				self.sock.sendto(array, self.destination)
				self.sock.settimeout(0.001)
				try:
					answer = self.quick_get()
					print(answer, control_answer, array)
				except socket.timeout:
					None
			#print('sended long answer', array)

	def close(self):
		self.sock.close()


class Server():
	#методы передачи игровых данных для сервера
	def __init__(self):
		self.status = 'server'
		self.ex = Exchanger(())
		self.bind()
		self.ex.long_get('connect')
		print(self.ex.destination)

	def bind(self):
		port = 9000
		while True:
			try:
				self.ex.sock.bind(('localhost', port))
				break
			except socket.error:
				print('Address already in use')
				port += 1
		self.my_addr = ('localhost', port)
		print(self.my_addr)

	#эти три надо переписать
	def change_data(self, game):
		p2_actions = self.ex.quick_get()
		if self.relevance_check(p2_actions):
			if p2_actions[0] == 'p2upd':
				self.p2_update(p2_actions, game.player2)

	def player_actions(self, game):
		return ['p2upd', self.relevance['p2upd'], game.using_keys, player.x, player.y]

	def p2_update(self, p2_actions, player2):
		player2.keys_dinamics(p2_actions[2])
		player2.x = p2_actions[3]
		player2.y = p2_actions[4]


class Client():
	#методы передачи игровых данных для клиента
	def __init__(self, server_addr):
		self.status = 'client'
		self.ex = Exchanger(server_addr)
		self.ex.long_send(['connect'])

'''
key = '2'#input()
if key == '1':
	timeout = 60
	host = 'localhost'
	port = 9092
	addr = (host, port)
	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server.bind(addr)

 

	while True:
		print ('Waiting for data ({0} seconds)...'.format(timeout))
		server.settimeout(timeout)

		try:
			d = server.recvfrom(1024)
		except socket.timeout: 
			print('Time is out. {0} seconds have passed'.format(timeout))
			break
		received = d[0]
		addr = d[1]
		print ('Received data: ' , received)
		print ('From: ' , addr)
		msg = input('Enter message to send: ')
		server.sendto(msg.encode('utf-8'), addr)
	server.close()

elif key == '0':
	host = 'localhost'
	port = 9092
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	msg = input('Enter message to send: ')
	client.sendto(msg.encode('utf-8'), (host, port))
	d = client.recvfrom(1024)
	reply = d[0]
	addr = d[1]
	print ('Server reply: ' + reply.decode('utf-8'))
	client.close()

#c = Client( ('localhost', 9001))
'''
key = input()
if key == '1':
	s = Server()
	print(1)
	for i in range(0, 3):
		print(s.ex.long_get('main'), 'in chat')
		print(s.ex.actually_actions)
		s.ex.long_send(['nemain', input()])
	s.ex.close()
else:
	c = Client(('localhost', 9001))
	for i in range(0, 3):
		c.ex.long_send(['main', input()])
		print(c.ex.long_get('nemain'), 'in chat')
	c.ex.close()
'''

def huy(arr):
	arr.insert(0, 'h')
	return arr
print(huy(['u', 'y']))
'''

