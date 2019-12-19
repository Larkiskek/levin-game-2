import pygame
import scene
import player_config  
import tarakan
import draw
import math
import pictures_name



class Game():
    def __init__(self):
        self.player = player_config.Player(50, win_hight, 40, 20) #x, y, half_wight, half_hight
        self.win = pygame.display.set_mode((2*scene.win_wight, 2*scene.win_hight))
        self.parameter = 'Menu' # 0 - выход, 1 - игра, 2 - смерть, 3 - вход в комнату

    def update_screen(self):
        if self.parameter == 'Restart':
            self.parameter = 'New room'
        for i in range (0, 5):
            if self.parameter == 'New room':
                self.room = scene.Room(i)
                self.parameter = 'Continue game'
            else: 
                break
            self.play()
            self.exit_room()

    def play(self):
        while self.parameter == 'Continue game':
            print
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.actions()

            self.player.damage()
    

            draw.room(self.win)                  #рисуем локацию
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
                    self.parameter = 'Items' 
                else:
                    draw.pip(self.win)
                    if ( abs( self.player.x - scene.win_wight ) < 25 ) and ( abs( self.player.y - scene.win_hight ) < 25 ):
                        self.room.create_enemies(scene.list_enemies)


            self.player.health_check(self)
            pygame.display.update()


    def exit_room(self):
        if self.parameter == 'Items':
            self.room.create_items()
        while self.parameter == 'Items':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.actions()

            draw.room(self.win)                  #рисуем локацию
            draw.draw_player(self.win, self.player)

            draw.gate(self.win, self.room.gate.coordinates)
            self.room.gate.input(self)
            self.room.items_check(self.player)
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


    def menu(self):
        time_delay = 50
        while self.parameter == 'Menu':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            draw.start_page(self.win)
            if (time_delay == 0 and pygame.key.get_pressed()[pygame.K_RETURN]):
                self.parameter = 'New room'
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.parameter = 'Exit'
            if time_delay > 0:
                time_delay -= 1
            pygame.display.update()


    def title_death(self):
        while self.parameter == 'Death':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()       
            draw.title_death(self.win)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.parameter = 'Menu'
                self.player = player_config.Player(50, win_hight, 40, 20)
            pygame.display.update()


    def title_victory(self):
        while self.parameter == 'New room':
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()        
            draw.title_victory(self.win)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.parameter = 'Menu'
                self.player = player_config.Player(50, win_hight, 40, 20)
            pygame.display.update()



def main():
    game = Game()
    while game.parameter != 'Exit':
        game.menu()
        game.update_screen()
        game.title_death()
        game.title_victory()


    pygame.quit()

win_wight = 500
win_hight = 500
main()
