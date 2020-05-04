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
        self.parameter = 'Menu' # 0 - выход, 1 - игра, 2 - смерть, 3 - вход в комнату
        self.start_room = 0
        self.map = scene.Map()

    def menu(self):
        time_delay = 50
        menu_mode = 0
        while self.parameter == 'Menu':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            draw.menu(self.win, menu_mode)
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_DOWN]):
                menu_mode = ( menu_mode + 1 )%2
                time_delay = 30
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_UP]):
                menu_mode = ( menu_mode - 1 )%2
                time_delay = 30
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_RETURN]):
                self.parameter = 'Restart'
                self.player = player_config.Player(50, scene.win_hight)
                if menu_mode == 0:
                    self.load_save()
                    self.parameter = 'New room'
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_ESCAPE]):
                self.parameter = 'Exit'
            if time_delay > 0:
                time_delay -= 1
            pygame.display.update()

    def update_screen(self):
        self.map.create_map()
        if self.parameter == 'Restart':
            self.start_room = 0
            self.parameter = 'New room'
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
    

            draw.room(self.win, self.map)                  #рисуем локацию
            draw.draw_player(self.win, self.player)


            for tar in self.room.tarakanS:
                draw.tarakan(self.win, tar)
                tar.dinamics(self.player)
                self.player.get_damage(tar)
                if tar.health <= 0:
                    self.room.tarakanS.remove(tar)
    

            if self.room.time_before_create > 0:
                self.room.time_before_create -= 1
            if len(self.room.tarakanS) == 0:
                if self.room.number_wave > self.room.list_enemies[0]:
                    self.parameter = 'Exit room'
                    self.room.list_enemies[0] = 0
                else:
                    draw.pip(self.win)
                    if ( abs( self.player.x - scene.win_wight ) < 25 + self.player.size ) and ( abs( self.player.y - scene.win_hight ) < 25 + self.player.size ):
                        self.room.create_enemies(scene.list_enemies)


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

            draw.room(self.win, self.map)                  #рисуем локацию
            draw.draw_player(self.win, self.player)

            draw.gate(self.win, self.room.gate.coordinates, self.map)
            self.room.gate.input(self)
            self.room.items_check(self.player, self.map.rooms[self.map.now_location[0]][self.map.now_location[1]])
            draw.items(self.win, self.room.items)

            self.player.damage()

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
            file.write(str(self.player.health) + '\n')
            file.write(str(0) + '\n')
            for i in range (0, self.player.taken_items[0] + 1):
                file.write(str(self.player.taken_items[i]) + '\n')
            file.close()
            self.parameter = 'Menu'
        elif  self.parameter == 'Menu':
            self.delete_save()

    def load_save(self):
        file = open('save.txt', 'r')
        self.player.health = int( file.readline() )
        self.start_room = int( file.readline() )
        file.close()

    def delete_save(self):
        file = open('save.txt', 'w')
        file.write(str(self.player.max_health) + '\n')
        file.write(str(0) + '\n')
        file.write(str(0) + '\n')
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

