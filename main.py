from pygame import *
import time as t

font.init()
font = font.Font(None, 32)
pl_win1 = font.render("Игрок 2 победил!", True, (250, 250, 250))
pl_win2 = font.render("Игрок 1 победил!", True, (250, 250, 250))

W, H = 850, 650
win = display.set_mode((W, H))
display.set_caption('Ping-pong')
back = (200, 255, 255)

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, width, height, spr_img, speed):
        super().__init__()
        self.image = transform.scale(image.load(spr_img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, width, height, spr_img, speed):
        super().__init__(x, y, width, height, spr_img, speed)
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < H - self.rect.height - 5:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < H - self.rect.height - 5:
            self.rect.y += self.speed
        
class Enemy(GameSprite):
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

player_r = Player(W - 65, H / 2 - 75, 50, 150, "roketka.jpg", 5)
player_l = Player(15, H / 2 - 75, 50, 150, "roketka.jpg", 5)
ball = Enemy(W / 2 - 25, H / 2 - 25, 50, 50, "ball.jpg", 0)

finish = False
lost = 0
clock = time.Clock()
run = True
FPS = 80
game_over = False

speed_x = 3
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    if finish != True:
        win.fill(back)
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(player_r, ball) or sprite.collide_rect(player_l, ball):
            speed_x *= -1
            
        if ball.rect.y > H - 50 or ball.rect.y < 0:
            speed_y *= -1
            
        player_r.update_r()
        player_l.update_l()
        ball.update()
        
        player_r.reset()
        player_l.reset()
        ball.reset()
        
        if ball.rect.x < 0:
            finish = True
            win.blit(pl_win1, (W / 2 - 100, H / 2))
            game_over = True
            
        if ball.rect.x > W - 50:
            finish = True
            win.blit(pl_win2, (W / 2 - 100, H / 2))
            game_over = True
            
    display.update()
    clock.tick(FPS)
