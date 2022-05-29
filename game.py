from pygame import *

#создай окно игры
win_width = 700
win_height = 500
FPS = 120

window = display.set_mode((win_width, win_height))
display.set_caption('Настольный теннис')
window.fill((255,255,255))
clock = time.Clock()


#Объявляем классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = None
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite) :
    def update_L(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

    def update_R(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 50:
            self.rect.y += self.speed

sprite_L = Player("dich.png", 0, win_height/2-50, 100, 100, 5)
sprite_R = Player("dich.png", win_width-100, win_height/2-50, 100, 100, 5)
ball = Player("tennis_ball.png", win_width/2-20, win_height/2-20, 40, 40, 10)


font.init()
font1 = font.SysFont('Arial', 70)

# over = font.render('Game Over', True, (255, 0 , 0))
# win = font.render('You Win', True, (250, 255 , 0))

speed_x = 1
speed_y = 1

#обработай событие «клик по кнопке "Закрыть окно"»
game = True
finish = False
while game:
    window.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                ball.rect.x = win_width/2-20
                ball.rect.y = win_height/2-20
                sprite_R.rect.x = win_width-100
                sprite_R.rect.y = win_height/2-50
                sprite_L.rect.x =0 
                sprite_L.rect.y = win_height/2-50
                finish = False
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y >= (win_height-40) or ball.rect.y <= 0:
        speed_y *= -1
    if sprite.collide_rect(ball, sprite_L):
        speed_x *= -1
    if sprite.collide_rect(ball, sprite_R):
        speed_x *= -1
    sprite_L.update_L()
    sprite_R.update_R()

    sprite_L.reset()
    sprite_R.reset()
    ball.reset()

    display.update()        
    clock.tick(FPS)