from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("ping-pong")
background = transform.scale(image.load("фон.jpg"), (win_width, win_height))


class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.x = player_x
        self.y = player_y

    def reset(self):
        window.blit(self.image, (self.x, self.y))

class Ball(Gamesprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed)
        self.speed_x = player_speed
        self.speed_y = player_speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #сверху в них 
        if self.rect.y > 500 - 50 or self.rect.y < 0:
            self.speed_y *= -1
            
        
        #лево и право
        if self.rect.x > 700 - 50:
            self.speed_x *= -1

        elif self.rect.x < 0:
            self.speed_x *= -1

class Player(Gamesprite):
    def update_player_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
            print(1)
        
        if keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed
            print(2)
    def update_player_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed


player1 = Player('фон.jpg', 1, 150, 150, 200, 5)
player2 = Player('фон.jpg', 560, 150, 150, 200, 5)
ball = Ball('ball.png', (win_width/2), (win_height/2), 50, 50, 5)
clock = time.Clock()
FPS = 60

game = True 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    
    window.blit(background,(0,0))
    player1.reset()
    player1.update_player_l()
    player2.reset()
    
    player2.update_player_r()
    ball.reset()
    ball.update()

    display.flip()
    clock.tick(FPS)
    

