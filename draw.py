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
	win.blit(tarakan.picture, tarakan.picture.get_rect(center = tarakan.coordinates()))
	pygame.draw.ellipse(win, tarakan.color, (math.trunc(tarakan.x-tarakan.half_wight), math.trunc(tarakan.y-tarakan.half_hight), 2*tarakan.half_wight, 2*tarakan.half_hight))
	if tarakan.type == 4:
		BOSS_HP(win, tarakan.health)

def HP(win, player):
	for i in range (player.health ):
		pygame.draw.rect(win, (255,0 ,0), ((10 + i*30), 10, 10, 10) )

def CD(win, player):
	pygame.draw.rect(win, (255, 0, 0), (2*scene.win_wight-200, 10, 150, 30), 3)
	if player.td == 0:
		pygame.draw.rect(win, (255, 0, 0), (2*scene.win_wight-200, 10, 150, 30))
	elif player.td < player.cd_max:
		L = 150 - 150*player.td / player.cd_max
		pygame.draw.rect(win, (255, 0, 0), (2*scene.win_wight-200, 10, L, 30)) 

def damage(win, player):
	if player.td > player.cd_max*player.weapon:
		if player.weapon == 1:
			lazer(win, player)
		else:
			bullet(win, player)

def lazer(win, player):
    pygame.draw.rect(win, (0,0,255), player.lazer.coordinates, 5)

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
    win.blit(pictures_name.body, pictures_name.body.get_rect(center = (player.x, player.y)))
    wings(win, player)

def wings(win, player):
	if pictures_name.time_wings == 80:
		pictures_name.time_wings = 0
	win.blit(pictures_name.azazel_wings[pictures_name.time_wings//10], pictures_name.azazel_wings[pictures_name.time_wings//10].get_rect(center = (player.x, player.y)))
	pictures_name.time_wings += 1