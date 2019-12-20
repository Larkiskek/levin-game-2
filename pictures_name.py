import pygame

def scale(n, pic):
	return pygame.transform.scale(pic, (pic.get_width()*n, pic.get_height()*n))

azazel_body = [
scale(4, pygame.image.load('pictures/1/39.png')),
scale(4, pygame.image.load('pictures/1/39.png')),
scale(4, pygame.image.load('pictures/1/39.png')),
scale(4, pygame.image.load('pictures/1/37.png')),
scale(10, pygame.image.load('pictures/1/38.png'))
]

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
[
pygame.image.load('pictures/1/10.png'),
pygame.image.load('pictures/1/11.png'),
pygame.image.load('pictures/1/12.png'),
pygame.image.load('pictures/1/13.png'),
pygame.image.load('pictures/1/14.png'),
pygame.image.load('pictures/1/15.png'),
pygame.image.load('pictures/1/16.png'),

pygame.image.load('pictures/1/1.png'),
pygame.image.load('pictures/1/2.png'),
pygame.image.load('pictures/1/3.png'),
],

[
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
],

[
pygame.image.load('pictures/1/21.png'),
pygame.image.load('pictures/1/20.png'),
pygame.image.load('pictures/1/19.png'),
pygame.image.load('pictures/1/19.png'),
pygame.image.load('pictures/1/18.png'),
pygame.image.load('pictures/1/18.png'),
pygame.image.load('pictures/1/17.png'),

pygame.image.load('pictures/1/4.png'),
pygame.image.load('pictures/1/5.png'),
pygame.image.load('pictures/1/6.png'),
],

[
pygame.image.load('pictures/1/21.png'),
pygame.image.load('pictures/1/20.png'),
pygame.image.load('pictures/1/19.png'),
pygame.image.load('pictures/1/19.png'),
pygame.image.load('pictures/1/18.png'),
pygame.image.load('pictures/1/18.png'),
pygame.image.load('pictures/1/17.png'),

pygame.image.load('pictures/1/4.png'),
pygame.image.load('pictures/1/5.png'),
pygame.image.load('pictures/1/6.png'),
]
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
