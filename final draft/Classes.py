import pygame



class player1Sprite(pygame.sprite.Sprite):

    def __init__(self, name, x, y):

        super().__init__()
        import pygame 
        self.name=name
        self.x=x
        self.y=y
        self.image = pygame.image.load('player1.png').convert()
        background = self.image.get_at((0, 0))
        self.image.set_colorkey(background)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.vx = self.vy = 6
        self.vJump=20
        self.mask = pygame.mask.from_surface(self.image)

            
    def update(self):
        def standing(self):
            if self.rect.centery == self.y:
                return True
        def jumping(self):
            if self.rect.centery != self.y:
                return True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left>1:
            self.rect.centerx -= self.vx
            self.direction = "left"
        if keys[pygame.K_RIGHT] and self.rect.right<999:
            self.rect.centerx += self.vx
            self.direction = "right"
        if self.rect.bottom < 300:
            if keys[pygame.K_UP] == False:
                self.rect.centery += self.vJump
                self.direction = "down"
        if keys[pygame.K_UP] and self.rect.top>100:
                self.rect.centery -= self.vJump
##            self.rect.centery = 150
                self.direction = "up"
        if self.rect.top < 0:
            self.vy *= -1

    def get_direction(self):
        return self.direction
    


        
        
        
                  
##          
##        if keys[pygame.K_DOWN]:
##            self.rect.centery += self.vy

      
class player2Sprite(pygame.sprite.Sprite):

    def __init__(self, name, x, y):

        super().__init__()
        import pygame 
        self.name=name
        self.x=x
        self.y=y
        self.image = pygame.image.load('player2.png').convert()
        background = self.image.get_at((0, 0))
        self.image.set_colorkey(background)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.vx = self.vy = 6
        self.vJump=20
        self.mask = pygame.mask.from_surface(self.image)

            
    def update(self):
        def standing(self):
            if self.rect.centery == self.y:
                return True
        def jumping(self):
            if self.rect.centery != self.y:
                return True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left>1:
            self.rect.centerx -= self.vx
            self.direction = "left"
        if keys[pygame.K_d] and self.rect.right<999:
            self.rect.centerx += self.vx
            self.direction = "right"
        if self.rect.bottom < 300:
            if keys[pygame.K_w] == False:
                self.rect.centery += self.vJump
                self.direction = "down"
        if keys[pygame.K_w] and self.rect.top>100:
                self.rect.centery -= self.vJump
                self.direction = "up"
        if self.rect.top < 0:
            self.vy *= -1

    def get_direction(self):
        return self.direction
    



class ball(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        super().__init__()
        import pygame

        self.x=x
        self.y=y
        self.image = pygame.image.load('ball.png').convert()
        background = self.image.get_at((0, 0))
        self.image.set_colorkey(background)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.vx = 0
        self.vy = 0
        self.mask = pygame.mask.from_surface(self.image)

    def set_vx(self,p):
        self.vx = p
        return self.vx
    def set_vy(self, p):
        self.vy = p
        return self.vy
    def set_x(self, p):
        self.x = p
        return self.x
    def set_y(self, p):
        self.y = p
        return self.y
        

    def update(self):
        if self.rect.left < 0 or self.rect.right > 1000:
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > 290:
            self.vy *= -1
        self.rect.centerx += self.vx
        self.rect.centery += self.vy

    def get_x(self):
        return self.rect.centerx
    def get_y(self):
        return self.rect.centery
    def get_right(self):
        return self.rect.right
    def get_left(self):
        return self.rect.left
  
    
class Net(pygame.sprite.Sprite):
    def __init__(self, x, y, LorR):
        super().__init__()
        self.x=x
        self.y=y
        self.LorR = LorR
        if self.LorR == "R":
            self.image = pygame.image.load("rightNet.png").convert()
           
        if self.LorR == "L":
            self.image = pygame.image.load("rightNet.png").convert()
            self.image = pygame.transform.flip(self.image, True, False)
           
        background = self.image.get_at((0,0))
        self.image.set_colorkey(background)
        self.rect = self.image.get_rect()        
        self.rect.top = self.y
        self.rect.left = self.x
        self.mask = pygame.mask.from_surface(self.image)

class bar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()       
        self.x=x
        self.y=y
        self.image = pygame.image.load('bar.png').convert()
        background = self.image.get_at((0, 0))
        self.image.set_colorkey(background)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.mask = pygame.mask.from_surface(self.image)

     
    
def collision(sprite, spriteGroup):
    import pygame
    if pygame.sprite.spritecollide(sprite, spriteGroup, False):
        return True

def goal(ball, screen):
    from easypg.colours import RED

    player1Score = False
    player2Score = False
    if ball.get_right() > 915 and (170 < ball.get_y() <300):
        player2Score = True
    if ball.get_left() < 85 and (170 < ball.get_y() <300):
        player1Score = True

    if player1Score == True or player2Score == True:           
       
     
        font = pygame.font.SysFont("test.ttf", 28, bold=False, italic=False)
        if player1Score == True:
            message = font.render('Player 1 Scores!', True, RED)
            if ball.get_left() < 50 and (170 < ball.get_y() <300):
                ball.set_vx(1)
                ball.set_vy(0)
        if player2Score == True:
            message = font.render('Player 2 Scores!', True, RED)
            if ball.get_right() > 950 and (170 < ball.get_y() <300):            
                ball.set_vx(-1)
                ball.set_vy(0)
        rect = message.get_rect()
        rect.center = (500,40)
        screen.blit(message, rect)
       


    
def kick(player, ball,  ballgroup):
 
 
    if collision(player, ballgroup) == True:
        direction = player.get_direction()
        if direction == "left":
            ball.set_vx(-8)
        if direction == "right":
            ball.set_vx(8)
        if direction == "up":
            ball.set_vy(-8)
        if direction == "down":
            ball.set_vy(8)

    
def barHit(bar, ball, ballgroup):
    if collision(bar, ballgroup) == True:
       ball.set_vy(-8)
        
