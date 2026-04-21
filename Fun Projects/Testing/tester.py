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
        self.image = pygame.transform.scale(self.image, (25, 40))
        self.rect = self.image.get_rect(center=(400, 350))
        self.speed = 5
        self.floor_y = 460
        self.y_velocity = 0
        self.gravity = 0.8
        self.jump_strength = -12.5
        self.is_jumping = False
        self.border_width = 100

    def jump(self):
        if not self.is_jumping:
            self.y_velocity = self.jump_strength
            self.is_jumping = True

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 100:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 700:
            self.rect.x += self.speed

        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity

        if self.rect.y >= self.floor_y:
            self.rect.y = self.floor_y
            self.y_velocity = 0
            self.is_jumping = False

# Setup
player = Player()
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()

    # 1. CLEAR THE SCREEN FIRST
    screen.fill((255, 255, 255)) # White background

    # 2. DRAW ENVIRONMENT
    # Draw the borders every frame so they stay on top of the white background
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 100)) # Top
    pygame.draw.rect(screen, (0, 0, 0), (0, 500, 800, 100)) # Bottom
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 600)) # Left
    pygame.draw.rect(screen, (0, 0, 0), (700, 0, 100, 600)) # Right

    # 3. UPDATE AND DRAW SPRITES
    all_sprites.update()
    all_sprites.draw(screen)

    #4. REFRESH
    pygame.display.flip()
    clock.tick(60)

pygame.quit()