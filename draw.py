import pygame
import player_config
import scene
import pictures_name
import math

def draw_player(win, player):
	animation_player(win, player)
	HP(win, player)
	bullet(win, player)
	CD(win, player)
	stats(win, player)

    
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
		win.blit(pictures_name.health, pictures_name.health.get_rect(center = (20 + 30*i, 20)))

def CD(win, player):
	pygame.draw.rect(win, (255, 0, 0), (10, 45, 150, 30), 3)
	if player.td >= player.cd_max:
		pygame.draw.rect(win, (255, 0, 0), (10, 45, 150, 30))
	elif player.td < player.cd_max:
		L = 150*player.td / player.cd_max
		pygame.draw.rect(win, (255, 0, 0), (10, 45, L, 30)) 
	if player.weapon == 1:
		win.blit(pygame.font.Font(None, 30).render('LAZER', 1, (180, 0, 0)), (10, 80))
	else :
		win.blit(pygame.font.Font(None, 30).render('BULLETS', 1, (0, 0, 180)), (10, 80))




def lazer(win, player):
	if player.lazer.status == 'ON':
		win.blit(pictures_name.lazer[player.lazer.direction], pictures_name.lazer[player.lazer.direction].get_rect(center = (player.x+player.lazer.direction_horizontal*100, player.y+player.lazer.direction_vertical*100+10)))		

def bullet(win, player):
	for bullet in player.bullets:
		pygame.draw.rect(win, (0, 0, 255), (bullet.x - bullet.size, bullet.y - bullet.size, 2*bullet.size, 2*bullet.size))
		win.blit(pictures_name.bullet, pictures_name.bullet.get_rect(center = bullet.coordinates))
	
def stats(win, player):
	win.blit(pygame.font.Font(None, 30).render('SPEED:', 0, (0, 0, 0)), (5, 2*scene.win_hight-200))
	win.blit(pygame.font.Font(None, 30).render(str(player.speed), 0, (0, 0, 0)), (150, 2*scene.win_hight-200))
	if player.weapon == 1:
		win.blit(pygame.font.Font(None, 30).render('DAMAGE:', 0, (180, 0, 0)), (5, 2*scene.win_hight-180))
		win.blit(pygame.font.Font(None, 30).render(str(player.lazer_characters['damage']), 0, (0, 0, 0)), (150, 2*scene.win_hight-180))
		win.blit(pygame.font.Font(None, 30).render('CD:', 0, (180, 0, 0)), (5, 2*scene.win_hight-160))
		win.blit(pygame.font.Font(None, 30).render(str(player.rate_of_lazer_fire), 0, (0, 0, 0)), (150, 2*scene.win_hight-160))
		win.blit(pygame.font.Font(None, 30).render('RANGE:', 0, (180, 0, 0)), (5, 2*scene.win_hight-140))
		win.blit(pygame.font.Font(None, 30).render(str(player.lazer_characters['lenght']), 0, (0, 0, 0)), (150, 2*scene.win_hight-140))
	else:
		win.blit(pygame.font.Font(None, 30).render('DAMAGE:', 0, (0, 0, 180)), (5, 2*scene.win_hight-180))
		win.blit(pygame.font.Font(None, 30).render(str(player.bullet_characters['damage']), 0, (0, 0, 0)), (150, 2*scene.win_hight-180))
		win.blit(pygame.font.Font(None, 30).render('CD:', 0, (0, 0, 180)), (5, 2*scene.win_hight-160))
		win.blit(pygame.font.Font(None, 30).render(str(player.shoot_cd_max), 0, (0, 0, 0)), (150, 2*scene.win_hight-160))
		win.blit(pygame.font.Font(None, 30).render('SPEED:', 0, (0, 0, 180)), (5, 2*scene.win_hight-140))
		win.blit(pygame.font.Font(None, 30).render(str(player.bullet_characters['speed']), 0, (0, 0, 0)), (150, 2*scene.win_hight-140))


def room(win, the_map, x, y):
	win.fill((240, 255 ,255))
	#win.blit(pictures_name.rooms[0], pictures_name.rooms[0].get_rect(center = (scene.win_wight, scene.win_hight)))
	mini_map(win, the_map, x, y)

def gate(win, coordinates, the_map):
	for j in range (0, 4):
		if the_map.rooms[the_map.now_location[0]+the_map.next_room[j][0]][the_map.now_location[1]+the_map.next_room[j][1]]['status'] != 'close':
			pygame.draw.rect(win, (255, 215 , 0), coordinates[j])

def menu(win, mode):
	win.fill((255, 140 , 0))
	pygame.font.init()
	win.blit(pygame.font.Font(None, 100).render('MENU', 1, (180, 0, 0)), (405, 50))
	if mode['status'] == 'main':
		if mode['number'] == 0:
			win.blit(pygame.font.Font(None, 50).render('New game', 1, (180, 0, 0)), (410, 750))
			win.blit(pygame.font.Font(None, 50).render('Exit', 1, (180, 0, 0)), (455, 800))
		elif mode['number'] == 1:
			win.blit(pygame.font.Font(None, 50).render('New game', 1, (255, 255, 0)), (410, 750))
			win.blit(pygame.font.Font(None, 50).render('Exit', 1, (180, 0, 0)), (455, 800))
		else :
			win.blit(pygame.font.Font(None, 50).render('New game', 1, (180, 0, 0)), (410, 750))
			win.blit(pygame.font.Font(None, 50).render('Exit', 1, (255, 255, 0)), (455, 800))
		if mode['save?'] == 1:
			if mode['number'] == 0:
				win.blit(pygame.font.Font(None, 50).render('Continue', 1, (255, 255, 0)), (415, 700))
			else :
				win.blit(pygame.font.Font(None, 50).render('Continue', 1, (180, 0, 0)), (415, 700))
		else :
			win.blit(pygame.font.Font(None, 50).render('Continue', 1, (84, 84, 82)), (415, 700))

	else:
		win.blit(pygame.font.Font(None, 60).render('Difficulty select', 1, (180, 0, 0)), (350, 600))
		if mode['number'] == 0:
			win.blit(pygame.font.Font(None, 50).render('I am to young to die', 1, (255, 255, 0)), (350, 700))
			win.blit(pygame.font.Font(None, 50).render('Hurt me plenty', 1, (180, 0, 0)), (385, 750))
			win.blit(pygame.font.Font(None, 50).render('Nightmare', 1, (180, 0, 0)), (415, 800))
		elif mode['number'] == 1:
			win.blit(pygame.font.Font(None, 50).render('I am to young to die', 1, (180, 0, 0)), (350, 700))
			win.blit(pygame.font.Font(None, 50).render('Hurt me plenty', 1, (255, 255, 0)), (385, 750))
			win.blit(pygame.font.Font(None, 50).render('Nightmare', 1, (180, 0, 0)), (415, 800))
		else :
			win.blit(pygame.font.Font(None, 50).render('I am to young to die', 1, (180, 0, 0)), (350, 700))
			win.blit(pygame.font.Font(None, 50).render('Hurt me plenty', 1, (180, 0, 0)), (385, 750))
			win.blit(pygame.font.Font(None, 50).render('Nightmare', 1, (255, 255, 0)), (415, 800))


	#win.blit(pictures_name.menu, pictures_name.menu.get_rect(center = (scene.win_wight, scene.win_hight)))

def title_victory(win):
	win.fill((224, 255 ,255))
	pygame.font.init()
	win.blit(pygame.font.Font(None, 100).render('YOU WIN!', 1, (255, 215, 0)), (375, 50))
	win.blit(pygame.font.Font(None, 36).render('Press "Enter" to exit to menu', 1, (255, 215, 0)), (325, 700))
	#win.blit(pictures_name.victory, pictures_name.victory.get_rect(center = (scene.win_wight, scene.win_hight)))

def title_death(win):
	win.fill((139, 0 , 0))
	pygame.font.init()
	win.blit(pygame.font.Font(None, 100).render('YOU DIED', 1, (0, 0, 0)), (350, 50))
	win.blit(pygame.font.Font(None, 36).render('Press "Enter" to exit to menu', 1, (0, 0, 0)), (325, 700))
	#win.blit(pictures_name.death, pictures_name.death.get_rect(center = (scene.win_wight, scene.win_hight)))

def pip(win):
	pygame.draw.rect(win, (255, 0, 0), ( scene.win_wight-25, scene.win_hight -25, 50, 50), 5)

def BOSS_HP(win, HP):
	pygame.draw.rect(win, (255, 0, 0), (scene.win_wight-200, 2*scene.win_hight - 50, 400, 30), 5)
	pygame.draw.rect(win, (255, 0, 0), (scene.win_wight-200, 2*scene.win_hight - 50, 4*HP // 30, 30)) 

def items(win, items):
	for item in items:
		win.blit(pictures_name.items[item[1]], pictures_name.items[item[1]].get_rect(center = item[3]))


def animation_player(win, player):
    body(win, player)
    if player.direction_head == 1:
    	lazer(win, player)
    	head(win, player)
    	wings(win, player)
    else:
    	wings(win, player)
    	head(win, player)
    	lazer(win, player)
    player.direction = 0

def wings(win, player):
	if player.time_wings == 80:
		player.time_wings = 0
	win.blit(pictures_name.azazel_wings[player.time_wings//10][0], pictures_name.azazel_wings[player.time_wings//10][0].get_rect(center = (player.x , player.y+40+pictures_name.azazel_wings[player.time_wings//10][1])))
	player.time_wings += 1

def body(win, player):
	win.blit(pictures_name.azazel_body[player.direction], pictures_name.azazel_body[player.direction].get_rect(center = (player.x, player.y+40)))


def head(win, player):
	if player.lazer.status != 'ON':
		number = 6*player.td // player.cd_max
		win.blit(pictures_name.azazel_head[player.direction_head][number], pictures_name.azazel_head[player.direction_head][number].get_rect(center = (player.x, player.y-30)))
	if player.lazer.status == 'ON':
		win.blit(pictures_name.azazel_head[player.lazer.direction][8], pictures_name.azazel_head[player.lazer.direction][8].get_rect(center = (player.x, player.y-30)))		

def mini_map(win, the_map, x, y):
	if the_map.mini_map == 1:
		size = 25
	else :
		size = 15
	for i in range (0, the_map.max_map_size):
		for j in range (0, the_map.max_map_size):
			if the_map.rooms[i][j]['status'] == 'open':
				pygame.draw.rect(win, (255, 255, 255), (2*scene.win_wight-5+(i-the_map.max_map_size)*size, 5+j*size, size, size))
				#win.blit(pygame.font.Font(None, 25).render(str(the_map.rooms[i][j]['difficalty']), 0, (0, 0, 0)), (2*scene.win_wight-5+(i-the_map.max_map_size)*size, 5+j*size))
			elif the_map.rooms[i][j]['status'] == 'GOLD' :
				pygame.draw.rect(win, (255, 255, 0), (2*scene.win_wight-5+(i-the_map.max_map_size)*size, 5+j*size, size, size))
			elif the_map.rooms[i][j]['status'] == 'BOSS':
				pygame.draw.rect(win, (0, 0, 0), (2*scene.win_wight-5+(i-the_map.max_map_size)*size, 5+j*size, size, size))
			else:
				pygame.draw.rect(win, (200, 200, 200), (2*scene.win_wight-5+(i-the_map.max_map_size)*size, 5+j*size, size, size))
	pygame.draw.rect(win, (255, 0, 0), (2*scene.win_wight-5+(the_map.now_location[0]-the_map.max_map_size)*size + (x-40)*size//(2*scene.win_wight), the_map.now_location[1]*size+5+(y-200)*size//(2*scene.win_hight), 5, 5))

def FPS(win, time):
	win.blit(pygame.font.Font(None, 30).render("fps: " + str(1000//time), 1, (0, 0, 0)), (5, 950))

	#head = pictures_name.azazel_body[player.direction]