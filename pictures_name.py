import pygame

def scale(n, pic):
	return pygame.transform.scale(pic, (pic.get_width()*n, pic.get_height()*n))

body = pygame.image.load('pictures/1/39.png')
body = scale(4, body)

time_wings = 0

azazel_wings = [
#вперёд

scale(4, pygame.image.load('pictures/1/30.png')),
scale(4, pygame.image.load('pictures/1/31.png')),
scale(4, pygame.image.load('pictures/1/32.png')),
scale(4, pygame.image.load('pictures/1/33.png')),
scale(4, pygame.image.load('pictures/1/34.png')),
scale(4, pygame.image.load('pictures/1/33.png')),
scale(4, pygame.image.load('pictures/1/32.png')),
scale(4, pygame.image.load('pictures/1/31.png'))

]


azazel_head = [
pygame.image.load('pictures/1/28.png'),
pygame.image.load('pictures/1/27.png'),
pygame.image.load('pictures/1/26.png'),
pygame.image.load('pictures/1/25.png'),
pygame.image.load('pictures/1/24.png'),
pygame.image.load('pictures/1/23.png'),
pygame.image.load('pictures/1/22.png'),

pygame.image.load('pictures/1/7.png'),
pygame.image.load('pictures/1/8.png'),
pygame.image.load('pictures/1/9.png'),
]



tarakan_pictures = [

[scale(2, pygame.image.load('pictures/4/103201.png')), 
scale(2, pygame.image.load('pictures/4/103200.png'))],

[scale(3, pygame.image.load('pictures/4/100900.png')),
scale(3, pygame.image.load('pictures/4/100899.png')),
scale(3, pygame.image.load('pictures/4/100898.png'))],

[scale(4, pygame.image.load('pictures/4/100901.png')),
scale(4, pygame.image.load('pictures/4/100902.png')),
scale(4, pygame.image.load('pictures/4/100903.png'))],

[scale(8, pygame.image.load('pictures/4/64681.png')),
scale(8, pygame.image.load('pictures/4/64682.png'))],

[scale(10, pygame.image.load('pictures/2/9.png'))]

]
