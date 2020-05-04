import pygame
import scene
import player_config  
import tarakan
import draw
import math
import pictures_name



class Game():
    def __init__(self):
        self.win = pygame.display.set_mode((2*scene.win_wight, 2*scene.win_hight))
        self.parameter = 'Menu' 
        self.menu_mode = dict(status = 'main', number = 0)

    def menu(self):
        time_delay = 50
        self.load_save()
        self.menu_mode['save?'] = self.save_status
        if self.save_status == 0:
            self.menu_mode['number'] = 1
        self.menu_mode['number'] = 0
        while self.parameter == 'Menu':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            draw.menu(self.win, self.menu_mode)
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_DOWN]):
                self.menu_mode['number'] = ( self.menu_mode['number'] + 1 )%3
                time_delay = 20
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_UP]):
                self.menu_mode['number'] = ( self.menu_mode['number'] - 1 )%3
                time_delay = 20
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_RETURN]):
                time_delay = 30
                if self.menu_mode['status'] == 'main':
                    if (self.menu_mode['number'] == 0) and self.save_status == 1:
                        self.map = scene.Map(0)
                        self.player = player_config.Player(50, scene.win_hight)
                        self.map.create_map()
                        self.parameter = 'New room'
                        self.load_save()
                    elif self.menu_mode['number'] == 1:
                        self.menu_mode['status'] = 'level difficalty'
                        self.menu_mode['number'] = 0
                    elif self.menu_mode['number'] == 2:
                        self.parameter = 'Exit'
                elif self.menu_mode['status'] == 'level difficalty':
                    self.map = scene.Map(2*self.menu_mode['number'])
                    self.player = player_config.Player(50, scene.win_hight)
                    self.map.create_map()
                    self.menu_mode['status'] = 'main'
                    self.menu_mode['number'] = 0
                    self.parameter = 'New room'
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_ESCAPE]):
                time_delay = 30
                if self.menu_mode['status'] == 'main':
                    self.parameter = 'Exit'
                else:
                    self.menu_mode['status'] = 'main'
            if time_delay > 0:
                time_delay -= 1
            pygame.display.update()


    def update_screen(self):
        while self.parameter == 'New room':
            self.room = scene.Room(self.map.rooms[self.map.now_location[0]][self.map.now_location[1]])
            self.parameter = 'Play game'
            self.play()
            self.exit_room()

    def play(self):
        while self.parameter == 'Play game':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.actions()

            self.player.damage()
    

            draw.room(self.win, self.map, self.player.x, self.player.y)                  #рисуем локацию
            draw.draw_player(self.win, self.player)


            for tar in self.room.tarakanS:
                draw.tarakan(self.win, tar)
                tar.dinamics(self.player)
                self.player.get_damage(tar)
                if tar.health <= 0:
                    self.room.tarakanS.remove(tar)
    

            if self.room.time_before_create > 0:
                self.room.time_before_create -= 1
            if self.map.mini_map_time > 0:
                self.map.mini_map_time -= 1
            if len(self.room.tarakanS) == 0:
                if self.room.number_wave > self.room.list_enemies[0]:
                    self.parameter = 'Exit room'
                    self.room.list_enemies[0] = 0
                else:
                    draw.pip(self.win)
                    if ( abs( self.player.x - scene.win_wight ) < 25 + self.player.size ) and ( abs( self.player.y - scene.win_hight ) < 25 + self.player.size ):
                        self.room.create_enemies(self.room.list_enemies[self.room.number_wave])


            self.player.health_check(self)
            pygame.display.update()


    def exit_room(self):
        if self.parameter == 'Exit room' and self.room.status == 'BOSS' :
            self.parameter = 'Victory'
        if self.parameter == 'Exit room' and self.room.status == 'GOLD' :
            self.room.create_items()
        while self.parameter == 'Exit room':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.actions()

            draw.room(self.win, self.map, self.player.x, self.player.y)                  #рисуем локацию
            draw.draw_player(self.win, self.player)

            draw.gate(self.win, self.room.gate.coordinates, self.map)
            self.room.gate.input(self)
            self.room.items_check(self.player, self.map.rooms[self.map.now_location[0]][self.map.now_location[1]])
            draw.items(self.win, self.room.items)


            self.player.damage()
            if self.map.mini_map_time > 0:
                self.map.mini_map_time -= 1
            pygame.display.update()


    def actions(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.player.move_left()

        if keys[pygame.K_d]:
            self.player.move_right()

        if keys[pygame.K_w]:
            self.player.move_up()

        if keys[pygame.K_s]:
            self.player.move_down()

        if keys[pygame.K_UP]:
            self.player.damage_up()

        if keys[pygame.K_DOWN]:
            self.player.damage_down()

        if keys[pygame.K_LEFT]:
            self.player.damage_left()

        if keys[pygame.K_RIGHT]:
            self.player.damage_right()
    
        if keys[pygame.K_q]:
            self.player.change_weapon() 

        if keys[pygame.K_r]:
            self.parameter = 'Restart'

        if keys[pygame.K_ESCAPE]:
            self.parameter = 'Save' 

        if keys[pygame.K_TAB]:
            if self.map.mini_map_time == 0:
                self.map.mini_map_time = 30
                self.map.mini_map = -self.map.mini_map

    def title_death(self):
        while self.parameter == 'Death':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()       
            draw.title_death(self.win)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.parameter = 'Menu'
            pygame.display.update()


    def title_victory(self):
        while self.parameter == 'Victory':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()        
            draw.title_victory(self.win)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.parameter = 'Menu'
            pygame.display.update()

    def save(self):
        if self.parameter == 'Save':
            file = open('save.txt', 'w')
            file.write(str(1) + '\n') #факт того, что сохранение существует
            file.write(str(self.player.health) + '\n')
            file.write(str(len(self.player.taken_items)) + '\n')
            for item in self.player.taken_items:
                file.write(str(item) + '\n')
            file.write(str(self.map.now_location[0]) + '\n')
            file.write(str(self.map.now_location[1]) + '\n')
            file.write(str(self.player.x) + '\n')
            file.write(str(self.player.y) + '\n')
            for i in range (0, self.map.max_map_size):
                for j in range (0, self.map.max_map_size):
                    room = self.map.rooms[i][j]
                    file.write( room['status']+ '\n')
                    file.write( str(room['enemies'][0]) + '\n')
                    for k in range (0, room['enemies'][0]):
                        for l in range (0, 5):
                            file.write( str(room['enemies'][k+1][l]) + '\n')
            file.close()
            self.parameter = 'Menu'
        elif  self.parameter == 'Menu':
            self.delete_save()


    def load_save(self):
        file = open('save.txt', 'r')
        self.save_status = int(file.readline())
        if self.save_status == 1 and self.parameter == 'New room':
            self.player.health = int( file.readline() )
            lenght =  int( file.readline() ) 
            for i in range (0, lenght):
                self.player.get_item(scene.list_items[int( file.readline())])
            self.map.now_location[0] = int(file.readline())
            self.map.now_location[1] = int(file.readline())
            self.player.x = int(file.readline())
            self.player.y = int(file.readline())
            for i in range (0, self.map.max_map_size):
                for j in range (0, self.map.max_map_size):
                    self.map.rooms[i][j]['status'] = file.readline().replace('\n','')
                    self.map.rooms[i][j]['enemies'] = [0]
                    self.map.rooms[i][j]['enemies'][0] = int(file.readline())
                    for k in range (0, self.map.rooms[i][j]['enemies'][0]):
                        self.map.rooms[i][j]['enemies'].append([0, 0, 0, 0, 0])
                        for l in range (0, 5):
                            self.map.rooms[i][j]['enemies'][k+1][l] = int(file.readline())
        file.close()


    def delete_save(self):
        file = open('save.txt', 'w')
        file.write(str(0))
        file.close()




def main():
    game = Game()
    while game.parameter != 'Exit':
        game.menu()
        game.update_screen()
        game.title_death()
        game.title_victory()
        game.save()
    pygame.quit()

