from pygame import*
import time as t

W, H = 1000, 700
win = display.set_mode((W, H))
display.set_caption('Ping-pong')
back = (200, 255, 255)
win.fill(back)

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
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.right < H - 5:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.right < H - 5:
            self.rect.y += self.speed
        
#class Enemy(GameSprite):
#    def update(self):
#        global max_lose
#        global lost
#        self.rect.y += self.speed
#        if self.rect.y > H:
#            self.rect.y = 0
#            self.rect.x = randint(80, W - 80)

clock = time.Clock()
run = True
FPS = 80

while run:
    for e in event.get():
        if e == QUIT:
            run == False
    display.update()
    clock.tick(FPS)
