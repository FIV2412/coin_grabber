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
            (self.position[0]  + GRID_SIZE // 2,
             self.position[1]  + GRID_SIZE // 2), GRID_SIZE // 2 - 1, width=2
                  )

    def move(self, dx, dy):
        """Сдвигает игрока на dx, dy клеток сквозь края."""
        x, y = self.position
        new_x = (x + dx * GRID_SIZE) % SCREEN_WIDTH
        new_y = (y + dy * GRID_SIZE) % SCREEN_HEIGHT
        self.position = (new_x, new_y)

class Coin(GameObject):
    """Монета, которую собирает игрок."""

    def __init__(self):
        """Ставит монету в случайную клетку поля."""
        x = randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        super().__init__((x, y), COIN_COLOR)

    def draw(self, surface):
        """Рисует залитую монету."""
        pygame.draw.circle(
            surface,
            self.body_color,
            (self.position[0] + GRID_SIZE // 2,
             self.position[1] + GRID_SIZE // 2),
            GRID_SIZE // 2 - 2
        )


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = Player()
coin = Coin()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move(1, 0)
            if event.key == pygame.K_LEFT:
                player.move(-1, 0)
            if event.key == pygame.K_UP:
                player.move(0, -1)
            if event.key == pygame.K_DOWN:
                player.move(0, 1)

    screen.fill(BOARD_BACKGROUND_COLOR)
    player.draw(screen)
    coin.draw(screen)
    pygame.display.update()
    clock.tick(30)