import pygame

from sys import exit


pygame.init() 


#screen init
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Gemini Universe")                           #game title
clock = pygame.time.Clock()                                             #sets a clock to be used to set a tic rate

#player init variables
player_width = 75
player_height = 150

#importing walk animation images
walk_animation = []
for i in range (0,22):
    frame = pygame.image.load(f'Desktop/Gemini Universe/Graphics/mc_idle/frame_{i}.gif').convert_alpha()
    sized_frame = pygame.transform.scale(frame, (player_width,player_height))
    walk_animation.append(sized_frame)


#creating title text
title_font = pygame.font.Font("Desktop/Gemini Universe/Fonts/FutureWorlds-JRRRB.ttf", 50)
title_text_surface = title_font.render("Gemini Universe", True, "Grey")
title_rect = title_text_surface.get_rect(center = (800, 50))

#background image
raw_background_surface = pygame.image.load("Desktop/Gemini Universe/Graphics/Bg 1 sky.png").convert_alpha()
background_surface = pygame.transform.scale(raw_background_surface, (10500, screen_height))      


#test platforms
test_platform = pygame.image.load("Desktop/Gemini Universe/Graphics/floor.jpg").convert_alpha()


#platform class

class Platform(pygame.sprite.Sprite):
    
    def __init__(self, image, width, height, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect(center = (x , y))
        
    def get_top(self):
        return self.rect.top
    
    def get_left(self):
        return self.rect.left 
    
    def get_rect(self):
        return self.rect
    
    def get_right(self):
        return self.rect.right

platforms = pygame.sprite.Group()

platform_1 = Platform(test_platform, 1200, 50, 800, 750)
platforms.add(platform_1)


# player class

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = walk_animation[0]
        self.rect = self.image.get_rect(center = (x,y))
        self.frame = 0
    
    def move(self, x ,y):
        self.rect.x += x
        self.rect.y += y
        if x < 0:
            self.walk_left()
        if x > 0:
            self.walk_right()
        if x == 0 and y == 0:
            self.idle_animation()
            clock.tick(60)
        
    def walk_left(self):
        #image cycle
        pass
        
    def walk_right(self):
        #image cycle
        pass
        
            
    def idle_animation(self):
        #image cycle
        self.image = walk_animation[self.frame]
        self.frame += 1
        if self.frame >= len(walk_animation):
            self.frame = 0
        
    
    def get_rect(self):
        return self.rect
    
    def get_bottom(self):
        return self.rect.bottom 
    
    def get_x(self):
        return self.rect.x 
    
player = pygame.sprite.GroupSingle()
player.add(Player(800, 450))
player_y_vel = 0
player_x_vel = 0
acc = 1
    


#Game loop
while True: 
    
    #background image loading
    
    screen.blit(background_surface,(0,0))       
    
    ##title
    
    screen.blit(title_text_surface, title_rect)

    #loading player 
    
    player.draw(screen)
    platforms.draw(screen)

  
    #platform collision and gravity 
    for p1 in player:
        for platform in platforms:
            #collision with the top of a platform detection
            if (pygame.Rect.colliderect(platform.get_rect() , p1.get_rect()) == True) and (p1.get_bottom() - platform.get_top() <= 20):
                #neutral state will be no movement
                player_y_vel = 0
                acc = 0
                player_x_vel = 0
                
                #left right and jump movements
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_a]:
                    player_x_vel = -8
                    
                if keys[pygame.K_d]:
                    player_x_vel = 8  
                
                if keys[pygame.K_SPACE] and (p1.get_bottom() - platform.get_top() <= 50):
                    player_y_vel = -25
                
                #initiating movement based on values     
                for p1 in player:
                    p1.move(player_x_vel ,  player_y_vel)
                    
            else: 
                #player gravity
                
                player_x_vel = 0
                acc = 2
                player_y_vel=+ player_y_vel + acc
                
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_a]:
                    player_x_vel = -8
                    
                if keys[pygame.K_d]:
                    player_x_vel = 8  
                
                for p1 in player:
                    p1.move(player_x_vel ,  player_y_vel)
                
        

    #event handler
    for event in pygame.event.get(): #running through all events
            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()                              #if player closes game the code ends
    
    pygame.display.update()                     #updates the display with the given information as long as the while loop is working
    clock.tick(60)                              #sets the while loop to only run faster than 60 fps
