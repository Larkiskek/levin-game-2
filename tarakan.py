import scene
import player_config
import random
import math
import pictures_name


class Tarakan():
    def __init__(self, x, y, characteristic):
        self.x = x
        self.y = y
        self.shift_x = characteristic[9]
        self.shift_y = characteristic[10]

        self.type = characteristic[0]
        self.picture = pictures_name.tarakan_pictures[self.type]
  
        self.half_hight = characteristic[2] //2
        self.half_wight = characteristic[1] //2
        self.p = self.half_hight / self.half_wight
        self.color = characteristic[5]

        self.speed = characteristic[4]
        self.stop_move = 0 # Переменная остановки движения. После того, как таракан нанёс урон игроку, он останавливается, и переменная становится ненулевой
        self.stop_move_max = 100
        self.damage_radius = 10 # Радиус дамага таракана

        self.static_move_count = 0

        self.health = characteristic[3]

        self.jump_speed_x = 0
        self.jump_speed_y = 0
        self.jump_duration = characteristic[6]
        self.jump_cd = characteristic[7]
        self.jump_speed = characteristic[8]
        self.jump_time = self.jump_duration + self.jump_cd

        self.animation_time = 0


    def coordinates(self):
        return (self.x - self.shift_x, self.y-self.shift_y )

    def close_player(self, players):
        r = 10000
        for player in players:
            player_r = ( (abs(player.x - self.x)+player.size)**2 + (abs(self.y - player.y)+player.size)**2 )**0.5
            if player_r < r:
                x = player.x
                y = player.y
                r = player_r
        return (r, x, y)


    def move(self, players):
        if self.stop_move == 0:
            #r = ( (abs(player.x - self.x)+player.size)**2 + (abs(self.y - player.y)+player.size)**2 )**0.5
            close_player_coordinates = self.close_player(players)
            r = close_player_coordinates[0]
            player_x = close_player_coordinates[1]
            player_y = close_player_coordinates[2]
            self.jump()
            self.x += int(self.speed * (player_x - self.x) // r) + self.jump_speed_x
            self.y += int(self.speed * (player_y - self.y) // r) + self.jump_speed_y
        else:
            self.stop_move -= 1


    def get_damage(self, player):
        if player.lazer.status == 'ON':
            if ( self.x > player.lazer.coordinates[0] - self.half_wight ) and ( self.y > player.lazer.coordinates[1] - self.half_hight ) and (  (player.lazer.coordinates[0] + player.lazer.coordinates[2] + self.half_wight ) > self.x  ) and (  (player.lazer.coordinates[1] + player.lazer.coordinates[3] + self.half_hight) > self.y) and (player.weapon == 1):
                self.health -= player.lazer.damage
        for bullet in player.bullets:
            if ( self.x > bullet.x - self.half_wight ) and ( self.y > bullet.y - self.half_hight ) and (  (bullet.x + bullet.size + self.half_wight ) > self.x  ) and (  (bullet.y + bullet.size + self.half_hight) > self.y):
                self.health -= bullet.damage
                player.bullets.remove(bullet)
        if ( (player.x - self.x)**2 + (self.p*(player.y - self.y))**2 < self.half_wight**2 ) and self.stop_move == 0:
                self.stop_move = self.stop_move_max
                player.health -= 1



    def jump(self):
        if self.jump_time == self.jump_duration:
            fi = random.random()*2*math.pi
            self.jump_speed_x = int(self.jump_speed*math.cos(fi))
            self.jump_speed_y = int(self.jump_speed*math.sin(fi))
        elif self.jump_time == 0:
            self.jump_speed_x = 0
            self.jump_speed_y = 0
            self.jump_time = self.jump_duration + self.jump_cd
        self.jump_time -= 1
        if ( self.x > 2*scene.win_wight - self.half_wight ) or ( self.x < 5 + self.half_wight ):
            self.jump_speed_x = -self.jump_speed_x
        if ( self.y > 2*scene.win_hight - 100 - self.half_hight ) or ( self.y < 100 + self.half_hight ):
            self.jump_speed_y = -self.jump_speed_y

        



