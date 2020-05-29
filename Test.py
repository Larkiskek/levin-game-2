import pygame
import pictures_name
pygame.init()


class Car(pygame.sprite.Sprite):
	def __init__(self, filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename).convert_alpha()
		self.rect = self.image.get_rect(center=(500, 500))

def main():
	win = pygame.display.set_mode((1000, 1000))
	win.fill((240, 255 ,255))
	obj = Car('pictures/1/28.png')
	win.blit(obj.image, obj.rect)
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		obj.update()
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('Sprite:         ', time2 - time1)
	obj.kill()

	win.fill((240, 255 ,255))
	obj = pygame.image.load('pictures/1/28.png')
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		win.blit(obj, obj.get_rect(center=(500, 500)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('Just blit():    ', time2 - time1)

	win.fill((240, 255 ,255))
	obj = pygame.image.load('pictures/1/28.png').convert_alpha()
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		win.blit(obj, obj.get_rect(center=(500, 500)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('Convert blit(): ', time2 - time1)

	win.fill((240, 255 ,255))
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		win.blit(pygame.image.load('pictures/1/28.png'), pygame.image.load('pictures/1/28.png').get_rect(center=(500, 500)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('No variable:    ', time2 - time1)

	win.fill((240, 255 ,255))
	heads =  [pygame.image.load('pictures/1/28.png'),
	pygame.image.load('pictures/1/28.png'),
	pygame.image.load('pictures/1/28.png'),
	pygame.image.load('pictures/1/28.png'),
	pygame.image.load('pictures/1/28.png')]
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		win.blit(heads[i%5], heads[i%5].get_rect(center=(500, 500)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('Array:          ', time2 - time1)

	win.fill((240, 255 ,255))
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		win.blit(pictures_name.azazel_head[0][i%10], pictures_name.azazel_head[0][i%10].get_rect(center=(500, 500)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('Array OF:       ', time2 - time1)

	win.fill((240, 255 ,255))
	obj = pygame.image.load('pictures/1/28.png').convert_alpha()
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		win.blit(obj, obj.get_rect(center=(500, 500)))
		win.blit(obj, obj.get_rect(center=(400, 500)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('2Con blit():    ', time2 - time1)

	win.fill((240, 255 ,255))
	obj = pygame.image.load('pictures/1/28.png').convert_alpha()
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('Clear:          ', time2 - time1)

	win.fill((240, 255 ,255))
	obj = pictures_name.rooms[0].convert()
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		win.blit(obj, obj.get_rect(center=(500, 500)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('BG picture:     ', time2 - time1)

	win.fill((240, 255 ,255))
	obj = pictures_name.rooms[0].convert_alpha()
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		win.blit(obj, obj.get_rect(center=(500, 500)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('BGCA picture:   ', time2 - time1)

	win.fill((240, 255 ,255))
	obj = pygame.image.load('pictures/1/28.png').convert_alpha()
	x = 500
	y = 500
	time1 = pygame.time.get_ticks()
	for i in range (0, 2000):
		if i%10 == 0:
			if pygame.key.get_pressed()[pygame.K_d]:
				x += 1
			if pygame.key.get_pressed()[pygame.K_a]:
				x -= 1
			if pygame.key.get_pressed()[pygame.K_w]:
				y -= 1
			if pygame.key.get_pressed()[pygame.K_s]:
				y += 1
		win.blit(obj, obj.get_rect(center=(x, y)))
		pygame.display.update()
	time2 = pygame.time.get_ticks()
	print('With keys:      ', time2 - time1)

	time1 = pygame.time.get_ticks()
	for i in range (0, 10000):
		None
	time2 = pygame.time.get_ticks()
	print('Nothing:        ', time2 - time1)
	#while True:
		#pygame.time.delay(10)
		#for event in pygame.event.get():
			#if event.type == pygame.QUIT:
				#exit()
		#if pygame.key.get_pressed()[pygame.K_d]:
			#obj.rect.x += 1
		#if pygame.key.get_pressed()[pygame.K_a]:
			#obj.rect.x -= 1
		#if pygame.key.get_pressed()[pygame.K_w]:
			#obj.rect.y -= 1
		#if pygame.key.get_pressed()[pygame.K_s]:
			#obj.rect.y += 1
		#if pygame.key.get_pressed()[pygame.K_z]:
			#break
		#pygame.display.update()
		#obj.update()
	print(pygame.time.get_ticks())
main()