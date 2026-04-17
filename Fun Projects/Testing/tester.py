import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Restored your original image loading and cropping
        sprite_sheet = pygame.image.load('images/spritesheet.webp').convert_alpha()
        sprite_rect = pygame.Rect(35, 159, 125, 200) 
        self.image = sprite_sheet.subsurface(sprite_rect)
        
        self.rect = self.image.get_rect(center=(400, 350))
        self.speed = 5
        self.floor_y = 350
        self.y_velocity = 0
        self.gravity = 0.8
        self.jump_strength = -12.5
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.y_velocity = self.jump_strength
            self.is_jumping = True

    def update(self):
        keys = pygame.key.get_pressed()
        # Horizontal movement
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

        # Physics logic
        if self.is_jumping:
            self.y_velocity += self.gravity
            self.rect.y += self.y_velocity

            # Ground collision check
            if self.rect.y >= self.floor_y:
                self.rect.y = self.floor_y
                self.y_velocity = 0 # Fixed the missing 'self' from your draft
                self.is_jumping = False

# Setup
player = Player()
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    # Handling events in the main loop prevents the jump from being "ignored"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()

    all_sprites.update()
    
    screen.fill((250, 250, 250))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
 