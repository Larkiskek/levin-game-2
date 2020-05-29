import pygame
import scene

pygame.display.set_mode((1000, 1000))

def adapt(scale, convtype, name):
	pic = pygame.image.load(name)
	scale = int(scale *10)
	pic = pygame.transform.scale(pic, (pic.get_width()*scale//10, pic.get_height()*scale//10))
	if convtype == 'a':
		return pic.convert_alpha()
	else:
		return pic.convert()

azazel_body = [
adapt(4, 'a', 'pictures/1/39.png'),
adapt(4, 'a', 'pictures/1/39.png'),
adapt(4, 'a', 'pictures/1/39.png'),
adapt(4, 'a', 'pictures/1/37.png'),
adapt(10, 'a', 'pictures/1/38.png')
]

azazel_wings = [
#вперёд

[adapt(4, 'a', 'pictures/1/30.png'), -30], 
[adapt(4, 'a', 'pictures/1/31.png'), -20],
[adapt(4, 'a', 'pictures/1/32.png'), -10],
[adapt(4, 'a', 'pictures/1/33.png'), 0],
[adapt(4, 'a', 'pictures/1/34.png'), 0],
[adapt(4, 'a', 'pictures/1/33.png'), 0],
[adapt(4, 'a', 'pictures/1/32.png'), -10],
[adapt(4, 'a', 'pictures/1/31.png'), -20]

]


azazel_head = [
[
adapt(4, 'a', 'pictures/1/28.png'),
adapt(4, 'a', 'pictures/1/27.png'),
adapt(4, 'a', 'pictures/1/26.png'),
adapt(4, 'a', 'pictures/1/25.png'),
adapt(4, 'a', 'pictures/1/24.png'),
adapt(4, 'a', 'pictures/1/23.png'),
adapt(4, 'a', 'pictures/1/22.png'),

adapt(4, 'a', 'pictures/1/7.png'),
adapt(4, 'a', 'pictures/1/8.png'),
adapt(4, 'a', 'pictures/1/9.png'),
],

[
adapt(4, 'a', 'pictures/1/10.png'),
adapt(4, 'a', 'pictures/1/11.png'),
adapt(4, 'a', 'pictures/1/12.png'),
adapt(4, 'a', 'pictures/1/13.png'),
adapt(4, 'a', 'pictures/1/14.png'),
adapt(4, 'a', 'pictures/1/15.png'),
adapt(4, 'a', 'pictures/1/16.png'),

adapt(4, 'a', 'pictures/1/1.png'),
adapt(4, 'a', 'pictures/1/2.png'),
adapt(4, 'a', 'pictures/1/3.png'),
],

[
adapt(4, 'a', 'pictures/1/28.png'),
adapt(4, 'a', 'pictures/1/27.png'),
adapt(4, 'a', 'pictures/1/26.png'),
adapt(4, 'a', 'pictures/1/25.png'),
adapt(4, 'a', 'pictures/1/24.png'),
adapt(4, 'a', 'pictures/1/23.png'),
adapt(4, 'a', 'pictures/1/22.png'),

adapt(4, 'a', 'pictures/1/7.png'),
adapt(4, 'a', 'pictures/1/8.png'),
adapt(4, 'a', 'pictures/1/9.png'),
],

[
adapt(4, 'a', 'pictures/1/21.png'),
adapt(4, 'a', 'pictures/1/20.png'),
adapt(4, 'a', 'pictures/1/19.png'),
adapt(4, 'a', 'pictures/1/19.png'),
adapt(4, 'a', 'pictures/1/18.png'),
adapt(4, 'a', 'pictures/1/18.png'),
adapt(4, 'a', 'pictures/1/17.png'),

adapt(4, 'a', 'pictures/1/4.png'),
adapt(4, 'a', 'pictures/1/5.png'),
adapt(4, 'a', 'pictures/1/6.png'),
],

[
adapt(4, 'a', 'pictures/7/17.png'),
adapt(4, 'a', 'pictures/7/18.png'),
adapt(4, 'a', 'pictures/7/19.png'),
adapt(4, 'a', 'pictures/7/19.png'),
adapt(4, 'a', 'pictures/7/20.png'),
adapt(4, 'a', 'pictures/7/20.png'),
adapt(4, 'a', 'pictures/7/21.png'),

adapt(4, 'a', 'pictures/7/4.png'),
adapt(4, 'a', 'pictures/7/6.png'),
adapt(4, 'a', 'pictures/7/5.png'),
]
]



tarakan_pictures = [

[adapt(2, 'a', 'pictures/4/103201.png'), 
adapt(2, 'a', 'pictures/4/103200.png')],

[adapt(3, 'a', 'pictures/4/100900.png'),
adapt(3, 'a', 'pictures/4/100899.png'),
adapt(3, 'a', 'pictures/4/100898.png')],

[adapt(4, 'a', 'pictures/4/100901.png'),
adapt(4, 'a', 'pictures/4/100902.png'),
adapt(4, 'a', 'pictures/4/100903.png')],

[adapt(8, 'a', 'pictures/4/64681.png'),
adapt(8, 'a', 'pictures/4/64682.png')],

[adapt(10, 'a', 'pictures/2/9.png')]

]

lazer = [
0,
adapt(0.5, 'a', 'pictures/5/3.png'),
adapt(0.5, 'a', 'pictures/5/2.png'),
adapt(0.5, 'a', 'pictures/5/4.png'),
adapt(0.5, 'a', 'pictures/5/1.png')
]


items = [
adapt(4, 'a', 'pictures/3/64496.png'),
adapt(4, 'a', 'pictures/3/allstatsup.png'),
adapt(4, 'a', 'pictures/3/brimstone.png'),
adapt(4, 'a', 'pictures/3/dmgup.png'),
adapt(4, 'a', 'pictures/3/heart.png'),
adapt(4, 'a', 'pictures/3/speedup.png'),
adapt(4, 'a', 'pictures/3/tearsup.png')
]

menu = adapt(4, '0', 'pictures/6/a.png')
death = adapt(1, '0', 'pictures/6/i.png')
victory  = adapt(1,'0', 'pictures/6/h.png')

rooms = [
adapt(1, '0', 'pictures/6/3.jpg'),
adapt(3, '0', 'pictures/6/b.png'),
adapt(3, '0', 'pictures/6/d.png'),
adapt(3, '0', 'pictures/6/g.png'),
adapt(3, '0', 'pictures/6/e.png')
]

health = adapt(1, 'a', 'pictures/8/3.png')

bullet = adapt(1, 'a', 'pictures/8/1.png')
