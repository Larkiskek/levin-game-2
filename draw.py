import pygame
import player_config
import scene
import pictures_name
import math

def draw_player(win,object):
	player(win, object)
	HP(win, object)
	damage(win, object)
	CD(win, object)

    
def tarakan(win, tarakan):
	if tarakan.animation_time == -1:
		tarakan.animation_time = 20*len(tarakan.picture) -1
	win.blit(tarakan.picture[tarakan.animation_time//20], tarakan.picture[tarakan.animation_time//20].get_rect(center = tarakan.coordinates()))
	tarakan.animation_time -= 1
	#pygame.draw.ellipse(win, tarakan.color, (math.trunc(tarakan.x-tarakan.half_wight), math.trunc(tarakan.y-tarakan.half_hight), 2*tarakan.half_wight, 2*tarakan.half_hight))
	if tarakan.type == 4:
		BOSS_HP(win, tarakan.health)

def HP(win, player):
	for i in range (player.health ):
		pygame.draw.rect(win, (255,0 ,0), ((10 + i*30), 10, 10, 10) )

def CD(win, player):
	pygame.draw.rect(win, (255, 0, 0), (2*scene.win_wight-200, 10, 150, 30), 3)
	if player.td >= player.cd_max:
		pygame.draw.rect(win, (255, 0, 0), (2*scene.win_wight-200, 10, 150, 30))
	elif player.td < player.cd_max:
		L = 150*player.td / player.cd_max
		pygame.draw.rect(win, (255, 0, 0), (2*scene.win_wight-200, 10, L, 30)) 

def damage(win, player):
			lazer(win, player)
			bullet(win, player)

def lazer(win, player):
	if player.lazer.status == 'ON':
		pygame.draw.rect(win, (255, 0,0), player.lazer.coordinates, 5)

def bullet(win, player):
	for bullet in player.bullets:
		pygame.draw.rect(win, (0,0,255), bullet.coordinates)

def room(win):
	win.fill((0,0,100))

def gate(win, coordinates):
	pygame.draw.rect(win, (255, 255 ,255), coordinates )


def start_page(win):
	win.fill((255, 215, 0))

def title_victory(win):
	win.fill((255, 255, 255))

def title_death(win):
	win.fill((128, 0, 0))

def pip(win):
	pygame.draw.rect(win, (255, 0, 0), ( scene.win_wight-25, scene.win_hight -25, 50, 50), 5)

def BOSS_HP(win, HP):
	pygame.draw.rect(win, (255, 0, 0), (scene.win_wight-200, 2*scene.win_hight - 50, 400, 30), 5)
	pygame.draw.rect(win, (255, 0, 0), (scene.win_wight-200, 2*scene.win_hight - 50, 4*HP // 30, 30)) 

def items(win, items):
	for item in items:
		pygame.draw.rect(win, item[2], item[3])


def player(win, player):
    pygame.draw.rect(win, player.color, player.coordinates()) #рисуем игрока
    body(win, player)
    if player.direction == 1:
    	wings(win, player)
    	head(win, player)
    else:
    	head(win, player)
    	wings(win, player)
    player.direction = 0

def wings(win, player):
	if player.time_wings == 80:
		player.time_wings = 0
	win.blit(pictures_name.azazel_wings[player.time_wings//10], pictures_name.azazel_wings[player.time_wings//10].get_rect(center = (player.x, player.y)))
	player.time_wings += 1

def body(win, player):
	win.blit(pictures_name.azazel_body[player.direction], pictures_name.azazel_body[player.direction].get_rect(center = (player.x, player.y)))


def head(win, player):
	pass

	#head = pictures_name.azazel_body[player.direction]