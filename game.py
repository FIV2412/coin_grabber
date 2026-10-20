import pygame

from random import randint, choice

SCREEN_WIDTH, SCREEN_HEIGHT = 480, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
cent_x, cent_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
BOARD_BACKGROUND_COLOR = (30, 30, 30)
PLAYER_COLOR = (0, 120, 255)
COIN_COLOR = (255, 215, 0)
BORDER_COLOR = (93, 216, 228)
SPEED = 10
x, y = 100, 200

class GameObject:
    """Базовый игровой Объект"""

    def __init__(self, position=None, body_color=None):
        """Сохраняет позицию и цвет объекта"""
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Отрисовывает объект (переопределяется в наследниках)."""
        pass
class Player(GameObject):
    def __init__(self):
        """Создает игрока по центру поля"""
        super().__init__((cent_x, cent_y), PLAYER_COLOR)
            
        
            
    def draw(self, surface):
         pygame.draw.circle(
                 surface,
                 PLAYER_COLOR,
                 (self.position[0]  + GRID_SIZE // 2, self.position[1]  + GRID_SIZE // 2), GRID_SIZE // 2 - 1, width=2   
                  )

        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = Player()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x = (x + GRID_SIZE) % SCREEN_WIDTH
            if event.key == pygame.K_LEFT:
                x = (x - GRID_SIZE) % SCREEN_WIDTH
            if event.key == pygame.K_UP:
                y = (y - GRID_SIZE) % SCREEN_HEIGHT
            if event.key == pygame.K_DOWN:
                y = (y + GRID_SIZE) % SCREEN_HEIGHT

    screen.fill(BOARD_BACKGROUND_COLOR)
    player.draw(screen)
    pygame.display.update()
    clock.tick(30)