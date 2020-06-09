import pygame
import scene
import player_config  
import tarakan
import draw
import math
import pictures_name
import online



class Game():
    def __init__(self):
        self.win = pygame.display.set_mode((2*scene.win_wight, 2*scene.win_hight))
        self.parameter = 'Menu' 
        #тут нужно вернуть норм параметры
        self.menu_mode = dict(status = 'online', number = 0)
        self.using_keys = ''
        self.fps = dict(time = 0, delay = 30, value = 0, worst_time = 1)

    def menu(self):
        if self.parameter == 'Menu':
            time_delay = 50
            self.load_save()
            #self.menu_mode['status'] = 'main'
            self.menu_mode['save?'] = self.save_status
        if self.save_status == 0:
            self.menu_mode['number'] = 1
        else:
            self.menu_mode['number'] = 0
        self.menu_mode['options'] = 4
        while self.parameter == 'Menu':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.parameter = 'Exit'
            draw.menu(self.win, self.menu_mode)
            if time_delay == 0 and pygame.key.get_pressed()[pygame.K_DOWN]:
                self.menu_mode['number'] = ( self.menu_mode['number'] + 1 )%self.menu_mode['options']
                time_delay = 20
            if time_delay == 0 and pygame.key.get_pressed()[pygame.K_UP]:
                self.menu_mode['number'] = ( self.menu_mode['number'] - 1 )%self.menu_mode['options']
                time_delay = 20
            if time_delay == 0 and pygame.key.get_pressed()[pygame.K_RETURN]:
                time_delay = 30
                if self.menu_mode['status'] == 'main':
                    if (self.menu_mode['number'] == 0) and self.save_status == 1:
                        self.players_status = 'single'
                        self.map = scene.Map(0, self.players_status)
                        self.player = player_config.Player(50, scene.win_hight, 3)
                        self.parameter = 'New room'
                        self.load_save()
                    elif self.menu_mode['number'] == 1:
                        self.menu_mode['status'] = 'level difficalty'
                        self.menu_mode['options'] = 3
                        self.menu_mode['number'] = 0
                    elif self.menu_mode['number'] == 2:
                        self.parameter = 'Exit'
                    elif self.menu_mode['number'] == 3:
                        self.menu_mode['status'] = 'online'
                        self.menu_mode['options'] = 2

                elif self.menu_mode['status'] == 'level difficalty':
                    self.players_status = 'single'
                    self.map = scene.Map(2*self.menu_mode['number']+1, self.players_status)
                    self.player = player_config.Player(50, scene.win_hight, 3)
                    self.menu_mode['number'] = 0
                    self.parameter = 'New room'

                elif self.menu_mode['status'] == 'online':
                    self.players_status = 'pair'
                    self.map = scene.Map(1, self.players_status)
                    self.parameter = 'New room'
                    if self.menu_mode['number'] == 0:
                        self.serv = online.Server()
                        self.player = player_config.Player(50, scene.win_hight, 5)
                        self.player2 = player_config.Player(2*scene.win_hight-50, scene.win_hight, 5)
                        self.serv.send_save(self.player, self.map)

                    if self.menu_mode['number'] == 1:
                        self.serv = online.Client(input())
                        self.player2 = player_config.Player(50, scene.win_hight, 5)
                        self.player = player_config.Player(2*scene.win_hight-50, scene.win_hight, 5)
                        self.serv.get_save(self.player2, self.map)


            if time_delay == 0 and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                time_delay = 30
                if self.menu_mode['status'] == 'main':
                    self.parameter = 'Exit'
                else:
                    self.menu_mode['status'] = 'main'
                    self.menu_mode['options'] = 4

            if time_delay > 0:
                time_delay -= 1
            pygame.display.update()


    def play(self):
        if self.parameter == 'New room':
            while self.parameter == 'New room':
                self.room = scene.Room(self.map.rooms[self.map.now_location[0]][self.map.now_location[1]])
                self.parameter = 'Play game'
                while self.parameter == 'Play game':
                    self.battle()
                if self.parameter == 'Exit room' and self.room.status == 'BOSS' :
                    self.parameter = 'Victory'
                if self.parameter == 'Exit room' and self.room.status == 'GOLD' :
                    self.room.create_items()
                while self.parameter == 'Exit room':
                    self.exit_room()
            if self.players_status != 'single':
                self.serv.close()


    def battle(self):

        if self.players_status == 'single':
            self.battle_calculation()
        elif self.serv.status == 'server':
            self.serv.change_data(self)
            self.battle_calculation()
        elif self.serv.status == 'client':
            self.serv.change_data(self)
            self.battle_calculation_2()
        self.drawing_battle()

    def exit_room(self):

        if self.players_status == 'single':
            self.exit_room_calculation()
        elif self.serv.status == 'server':
            self.serv.change_data(self)
            self.exit_room_calculation()
        elif self.serv.status == 'client':
            self.serv.change_data(self)
            self.exit_room_calculation_2()
        self.drawing_exit_room()


    def battle_calculation(self):
        self.actions()


        self.player.damage()

        if self.players_status == 'single':
            for tar in self.room.tarakanS:
                tar.get_damage(self.player)
                tar.move([self.player])
                if tar.health <= 0:
                    self.room.tarakanS.remove(tar)
            

        self.player.health_check(self)

        if self.players_status == 'pair':
            self.player2.damage()
            for tar in self.room.tarakanS:
                tar.get_damage(self.player2)
                tar.get_damage(self.player)
                tar.move([self.player, self.player2])
                if tar.health <= 0:
                    self.room.tarakanS.remove(tar)
            self.player2.health_check(self)


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


    def battle_calculation_2(self):
        self.actions() # у каждого игрока self.player - это он
        self.player.damage()
        self.player2.damage()


    def drawing_battle(self):
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parameter = 'Exit'
        draw.room(self.win, self.map, self.player.x, self.player.y)                  #рисуем локацию
        draw.draw_player(self.win, self.player)
        draw.draw_stats(self.win, self.player)
        if self.players_status == 'pair':                 #рисуем локацию
            draw.draw_player(self.win, self.player2)
        for tar in self.room.tarakanS:
            draw.tarakan(self.win, tar)

        if (len(self.room.tarakanS) == 0) and (self.room.number_wave <= self.room.list_enemies[0]):
            draw.pip(self.win)
 

        draw.FPS(self.win, self.fps['value'])
        self.fps_upd()
        pygame.display.update()



    def exit_room_calculation(self):

        self.actions()
        self.room.gate.input(self)
        self.room.items_check(self.player, self.map.rooms[self.map.now_location[0]][self.map.now_location[1]])

        self.player.damage()
        if self.players_status == 'pair':
            self.player2.damage()
        if self.map.mini_map_time > 0:
            self.map.mini_map_time -= 1

    def exit_room_calculation_2(self):

        self.actions()
        self.room.gate.input(self)

        if self.map.mini_map_time > 0:
            self.map.mini_map_time -= 1

        self.player.damage()
        self.player2.damage()



    def drawing_exit_room(self):
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parameter = 'Exit'
        draw.room(self.win, self.map, self.player.x, self.player.y)                  #рисуем локацию
        draw.draw_player(self.win, self.player)
        draw.draw_stats(self.win, self.player)
        if self.players_status == 'pair':                 #рисуем локацию
            draw.draw_player(self.win, self.player2)

        draw.gate(self.win, self.room.gate.coordinates, self.map)
        draw.items(self.win, self.room.items)
        draw.FPS(self.win, self.fps['value'])
        self.fps_upd()
        pygame.display.update()

    def actions(self):
        keys = pygame.key.get_pressed()
        self.using_keys = ''

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
            self.using_keys += 'U'

        if keys[pygame.K_DOWN]:
            self.player.damage_down()
            self.using_keys += 'D'

        if keys[pygame.K_LEFT]:
            self.player.damage_left()
            self.using_keys += 'L'

        if keys[pygame.K_RIGHT]:
            self.player.damage_right()
            self.using_keys += 'R'
    
        if keys[pygame.K_q]:
            self.player.change_weapon()
            self.using_keys += 'q' 

        if keys[pygame.K_r]:
            if self.players_status != 'pair' or self.serv.status == 'server':
                self.parameter = 'Restart'

        if keys[pygame.K_ESCAPE]:
            if self.players_status != 'pair' or self.serv.status == 'server':
                self.parameter = 'Save'
            else:
                self.parameter = 'Menu' 

        if keys[pygame.K_TAB]:
            if self.map.mini_map_time == 0:
                self.map.mini_map_time = 30
                self.map.mini_map = -self.map.mini_map

    def title_death(self):
        while self.parameter == 'Death':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.parameter = 'Exit'      
            draw.title_death(self.win)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.parameter = 'Menu'
            pygame.display.update()


    def title_victory(self):
        while self.parameter == 'Victory':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.parameter = 'Exit'        
            draw.title_victory(self.win)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.parameter = 'Menu'
            pygame.display.update()

    def save(self):
        if self.parameter == 'Save' and self.players_status == 'single':
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
        elif self.players_status == 'pair':
            self.parameter = 'Menu'


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

    def fps_upd(self):
        if self.fps['delay'] == 0:
            self.fps['value'] = 1000 // self.fps['worst_time']
            self.fps['worst_time'] = 0
            self.fps['time'] = pygame.time.get_ticks()
            self.fps['delay'] = 30
        else:
            self.fps['delay'] -= 1
            self.fps['worst_time'] = max(pygame.time.get_ticks() - self.fps['time'], self.fps['worst_time'])
            self.fps['time'] = pygame.time.get_ticks()


    def delete_save(self):
        file = open('save.txt', 'w')
        file.write(str(0))
        file.close()




def main():
    game = Game()
    while game.parameter != 'Exit':
        game.menu()
        game.play()
        game.title_death()
        game.title_victory()
        game.save()
    pygame.quit()
