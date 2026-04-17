import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the sheet
        sprite_sheet = pygame.image.load('images/spritesheet.webp').convert_alpha()
        
        # Define the area of the sprite (using the coords from earlier)
        sprite_rect = pygame.Rect(35, 159, 125, 200)

        # FIXED: Pygame REQUIRES the variable to be named 'self.image'
        self.image = sprite_sheet.subsurface(sprite_rect)
        
        self.rect = self.image.get_rect(center=(400, 300))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        
        # Horizontal movement with boundary checks
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
            
        # Vertical movement with boundary checks
        if keys[pygame.K_UP] and self.rect.top > 0:
            while True:
                if keys[pygame.K_LEFT] and self.rect.left > 0:
                    self.rect.x -= self.speed
                if keys[pygame.K_RIGHT] and self.rect.right < 800:
                    self.rect.x += self.speed
                self.rect.y -= 5
                #USE TIME TO CREAT JUMPING
                
        

# Setup sprite group
player = Player()
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    screen.fill((250, 250, 250)) 
    all_sprites.draw(screen) 
    pygame.display.flip() 

    clock.tick(60)

pygame.quit()
