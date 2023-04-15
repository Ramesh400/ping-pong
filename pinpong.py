from pygame import *

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
    def update_ball(self):
        pass




win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("ping-pong")
background = transform.scale(image.load("фон.jpg"), (win_width, win_height))
player1 = Gamesprite('player.png', 1, 150, 150, 200, 5)
player2 = Gamesprite('player.png', 560, 150, 150, 200, 5)

game = True 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background,(0,0))
    player1.reset()
    player2.reset()
    display.update()
    

