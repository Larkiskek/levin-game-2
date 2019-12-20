import scene
import tarakan
import draw
import math

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.color = (255, 0 , 0)

        self.cd_max = 200 # td - это time damage. Функция перезарядки. td_max - это фактическая, а td - оставшаяся до следующего выстрела
        self.td = 0
        self.rate_of_lazer_fire = 1

        self.shoot_cd_max = 30
        self.shoot_cd = 0

        self.speed = 7

        self.lazer_characters = {'lenght':80, 'wight':25, 'damage':50}
        self.bullet_characters = {'speed': 5,'damage': 30}

        self.max_health = 3
        self.health = self.max_health

        self.weapon = -1

        self.time_wings = 0
        self.time_head = 0
        self.direction = 0
        self.direction_head = 0

        self.direction_horizontal = 0
        self.direction_vertical = 0
        self.lazer = Lazer( self )
        self.lazer.update(self)
        self.bullets = [] 

        self.size = 60
        self.time_weapon = 20

    def move_up(self):
        if self.y >=100:
            self.y -= self.speed
        self.direction = 1
    def move_down(self):
        if self.y <= 2*scene.win_hight - 100:
            self.y += self.speed
        self.direction = 2
    def move_right(self):
        if self.x <= 2*scene.win_wight - 20:
            self.x += self.speed
        self.direction = 3
    def move_left(self):
        if self.x >= 20:
            self.x -= self.speed
        self.direction = 4

    def coordinates(self):
        return (self.x, self.y) 




            
    def damage_up(self):
        self.direction_vertical = -1
        self.direction_horizontal = 0
        self.direction_head = 1
        self.shot()
    def damage_down(self):
        self.direction_vertical = 1
        self.direction_horizontal = 0
        self.direction_head = 2
        self.shot()
    def damage_right(self):
        self.direction_vertical = 0
        self.direction_horizontal = 1
        self.direction_head = 3
        self.shot()
    def damage_left(self):
        self.direction_vertical = 0
        self.direction_horizontal = -1
        self.direction_head = 4
        self.shot()

    def shot(self):
            if (self.weapon == 1):
                if self.lazer.status == 'OFF':
                    self.lazer.status = 'CD'
                    if self.td < self.cd_max:
                        self.td += self.rate_of_lazer_fire
                    self.lazer.update_directions(self)
            else:
                if self.shoot_cd == 0:
                    self.shoot_cd = self.shoot_cd_max
                    bullet = Bullet(self.x, self.y, self.direction_horizontal, self.direction_vertical, self.bullet_characters) 
                    self.bullets.append( bullet )

    

    def damage(self):
        if (self.td >= self.cd_max) and self.lazer.status == 'OFF':
            self.lazer.status = 'ON'
        if self.lazer.status == 'OFF':
            self.td = 0
        if self.lazer.status == 'ON':
            self.lazer.update(self)
            self.td -= 2
        if self.lazer.status != 'ON' or self.td <= 0: 
            self.lazer.status = 'OFF'

        if self.shoot_cd != 0:
            self.shoot_cd -= 1 
        for bullet in self.bullets:
            bullet.move()
            if bullet.distance > bullet.distance_max:
                self.bullets.remove(bullet)





    def change_weapon(self):
        if self.time_weapon != 0:
            self.time_weapon -= 1
        if self.lazer.status == 'OFF':
            self.weapon = -self.weapon
            self.time_weapon = 20

    def get_damage(self, tarakan):
        if tarakan.stop_move == (tarakan.stop_move_max - 1) :
            self.health -= 1

    def health_check(self, game):
        if self.health <= 0:
            game.parameter = 'Death'






        
class Bullet():
    def __init__(self, x, y, direction_horizontal, direction_vertical, bullet_characters):
        self.x = x
        self.y = y

        self.speed = bullet_characters['speed']
        self.size = 15

        self.speed_x =  direction_horizontal * self.speed
        self.speed_y =  direction_vertical * self.speed 

        self.coordinates = ( self.x, self.y )

        self.distance = 0
        self.distance_max = 500
        self.damage = bullet_characters['damage']
        
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.distance += self.speed  
        self.coordinates = ( self.x, self.y )







class Lazer():
    def __init__(self, player):
        self.lenght_max = player.lazer_characters['lenght'] # размер дамаг-площадки. Без _max -динамические величины, показывающие область дамага сейчас
        self.wight_max = player.lazer_characters['wight']
        self.status = 'OFF'

        self.damage = player.lazer_characters['damage']

        self.direction_horizontal = player.direction_horizontal
        self.direction_vertical = player.direction_vertical
        self.direction = player.direction_head

        self.x_0 = (player.direction_horizontal)*abs(player.direction_horizontal-1)*self.lenght_max - abs(player.direction_vertical)*self.wight_max
        self.y_0 = (player.direction_vertical)*abs(player.direction_vertical-1)*self.lenght_max - abs(player.direction_horizontal)*self.wight_max
        self.wight = 2*abs(player.direction_vertical)*self.wight_max + 2*abs(player.direction_horizontal)*self.lenght_max
        self.hight = 2*abs(player.direction_horizontal)*self.wight_max + 2*abs(player.direction_vertical)*self.lenght_max


    def update(self, player):
        self.x = self.x_0 + player.x
        self.y = self.y_0 + player.y
        self.coordinates = (self.x, self.y, self.wight, self.hight)

    def update_directions(self, player):
        self.direction = player.direction_head
        self.direction_horizontal = player.direction_horizontal
        self.direction_vertical = player.direction_vertical        
        self.x_0 = (player.direction_horizontal)*abs(player.direction_horizontal-1)*self.lenght_max - abs(player.direction_vertical)*self.wight_max
        self.y_0 = (player.direction_vertical)*abs(player.direction_vertical-1)*self.lenght_max - abs(player.direction_horizontal)*self.wight_max
        self.wight = 2*abs(player.direction_vertical)*self.wight_max + 2*abs(player.direction_horizontal)*self.lenght_max
        self.hight = 2*abs(player.direction_horizontal)*self.wight_max + 2*abs(player.direction_vertical)*self.lenght_max
