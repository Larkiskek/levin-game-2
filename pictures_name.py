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

[scale(4, pygame.image.load('pictures/1/30.png')), -30], 
[scale(4, pygame.image.load('pictures/1/31.png')), -20],
[scale(4, pygame.image.load('pictures/1/32.png')), -10],
[scale(4, pygame.image.load('pictures/1/33.png')), 0],
[scale(4, pygame.image.load('pictures/1/34.png')), 0],
[scale(4, pygame.image.load('pictures/1/33.png')), 0],
[scale(4, pygame.image.load('pictures/1/32.png')), -10],
[scale(4, pygame.image.load('pictures/1/31.png')), -20]

]


azazel_head = [
[
scale(4, pygame.image.load('pictures/1/28.png')),
scale(4, pygame.image.load('pictures/1/27.png')),
scale(4, pygame.image.load('pictures/1/26.png')),
scale(4, pygame.image.load('pictures/1/25.png')),
scale(4, pygame.image.load('pictures/1/24.png')),
scale(4, pygame.image.load('pictures/1/23.png')),
scale(4, pygame.image.load('pictures/1/22.png')),

scale(4, pygame.image.load('pictures/1/7.png')),
scale(4, pygame.image.load('pictures/1/8.png')),
scale(4, pygame.image.load('pictures/1/9.png')),
],

[
scale(4, pygame.image.load('pictures/1/10.png')),
scale(4, pygame.image.load('pictures/1/11.png')),
scale(4, pygame.image.load('pictures/1/12.png')),
scale(4, pygame.image.load('pictures/1/13.png')),
scale(4, pygame.image.load('pictures/1/14.png')),
scale(4, pygame.image.load('pictures/1/15.png')),
scale(4, pygame.image.load('pictures/1/16.png')),

scale(4, pygame.image.load('pictures/1/1.png')),
scale(4, pygame.image.load('pictures/1/2.png')),
scale(4, pygame.image.load('pictures/1/3.png')),
],

[
scale(4, pygame.image.load('pictures/1/28.png')),
scale(4, pygame.image.load('pictures/1/27.png')),
scale(4, pygame.image.load('pictures/1/26.png')),
scale(4, pygame.image.load('pictures/1/25.png')),
scale(4, pygame.image.load('pictures/1/24.png')),
scale(4, pygame.image.load('pictures/1/23.png')),
scale(4, pygame.image.load('pictures/1/22.png')),

scale(4, pygame.image.load('pictures/1/7.png')),
scale(4, pygame.image.load('pictures/1/8.png')),
scale(4, pygame.image.load('pictures/1/9.png')),
],

[
scale(4, pygame.image.load('pictures/1/21.png')),
scale(4, pygame.image.load('pictures/1/20.png')),
scale(4, pygame.image.load('pictures/1/19.png')),
scale(4, pygame.image.load('pictures/1/19.png')),
scale(4, pygame.image.load('pictures/1/18.png')),
scale(4, pygame.image.load('pictures/1/18.png')),
scale(4, pygame.image.load('pictures/1/17.png')),

scale(4, pygame.image.load('pictures/1/4.png')),
scale(4, pygame.image.load('pictures/1/5.png')),
scale(4, pygame.image.load('pictures/1/6.png')),
],

[
scale(4, pygame.image.load('pictures/7/17.png')),
scale(4, pygame.image.load('pictures/7/18.png')),
scale(4, pygame.image.load('pictures/7/19.png')),
scale(4, pygame.image.load('pictures/7/19.png')),
scale(4, pygame.image.load('pictures/7/20.png')),
scale(4, pygame.image.load('pictures/7/20.png')),
scale(4, pygame.image.load('pictures/7/21.png')),

scale(4, pygame.image.load('pictures/7/4.png')),
scale(4, pygame.image.load('pictures/7/6.png')),
scale(4, pygame.image.load('pictures/7/5.png')),
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

lazer = [
0,
pygame.transform.scale(pygame.image.load('pictures/5/3.png'), (pygame.image.load('pictures/5/3.png').get_width()//2, pygame.image.load('pictures/5/3.png').get_height()//2)),
pygame.transform.scale(pygame.image.load('pictures/5/2.png'), (pygame.image.load('pictures/5/3.png').get_width()//2, pygame.image.load('pictures/5/3.png').get_height()//2)),
pygame.transform.scale(pygame.image.load('pictures/5/4.png'), (pygame.image.load('pictures/5/3.png').get_width()//2, pygame.image.load('pictures/5/3.png').get_height()//2)),
pygame.transform.scale(pygame.image.load('pictures/5/1.png'), (pygame.image.load('pictures/5/3.png').get_width()//2, pygame.image.load('pictures/5/3.png').get_height()//2))
]


items = [
scale(4, pygame.image.load('pictures/3/64496.png')),
scale(4, pygame.image.load('pictures/3/allstatsup.png')),
scale(4, pygame.image.load('pictures/3/brimstone.png')),
scale(4, pygame.image.load('pictures/3/dmgup.png')),
scale(4, pygame.image.load('pictures/3/heart.png')),
scale(4, pygame.image.load('pictures/3/speedup.png')),
scale(4, pygame.image.load('pictures/3/tearsup.png'))
]

menu = scale(4, pygame.image.load('pictures/6/a.png'))
death = scale(1, pygame.image.load('pictures/6/i.png'))
victory  = scale(1, pygame.image.load('pictures/6/h.png'))

rooms = [
pygame.image.load('pictures/6/3.jpg'),
scale(3, pygame.image.load('pictures/6/b.png')),
scale(3, pygame.image.load('pictures/6/d.png')),
scale(3, pygame.image.load('pictures/6/g.png')),
scale(3, pygame.image.load('pictures/6/e.png'))
]

health = pygame.image.load('pictures/8/3.png')

bullet = scale(1, pygame.image.load('pictures/8/1.png'))
