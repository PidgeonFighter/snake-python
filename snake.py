import pygame as pg

pg.init()  # initialize pygame

# costants
SCREEN_SIZE = (800, 800)
CELL_SIZE = 800//20
CELLS = (SCREEN_SIZE[0]//CELL_SIZE, SCREEN_SIZE[1]//CELL_SIZE)

SNAKE_MOTION_TIME = 500
SNAKE_MOTION_EVENT = pg.USEREVENT + 1

BACKGROUND_COLOR = (55, 55, 55)
GRID_COLOR = (255, 255, 255)
SNAKE_COLOR = (255, 0, 0)

# snake class


class Snake:

    def __init__(self, x, y):
        self.cells = [(x, y)]
        self.direction = (0, 0)

    def draw(self, surface: pg.Surface):
        for x, y in self.cells:
            r = pg.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(surface, SNAKE_COLOR, r)

    def __move(self, x, y):
        self.direction = (x, y)
        new_head = (self.cells[0][0]+x, self.cells[0][1]+y)
        self.cells.insert(0, new_head)
        self.cells.pop()
        pg.time.set_timer(SNAKE_MOTION_EVENT, SNAKE_MOTION_TIME, 1)

    def move(self, direction: tuple):
        self.__move(*direction)

    def update(self):
        self.__move(*self.direction)


# creating a screen with the given size
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()  # creating a default clock
# creating our letaly venomous snake 😯
snake: Snake = Snake(CELLS[0]//2, CELLS[1]//2)
pg.time.set_timer(SNAKE_MOTION_EVENT, SNAKE_MOTION_TIME, 1)
direction = (0, 0)

# game loop
running = True
while running:
    frame_time = clock.tick(60)

    keys = pg.key.get_pressed()
    if keys[pg.K_w] or keys[pg.K_UP]:
        direction = (0, -1)
    if keys[pg.K_s] or keys[pg.K_DOWN]:
        direction = (0, +1)
    if keys[pg.K_a] or keys[pg.K_LEFT]:
        direction = (-1, 0)
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        direction = (+1, 0)

    for event in pg.event.get():  # handle pygame events
        if event.type == pg.QUIT:
            running = False
        if event.type == SNAKE_MOTION_EVENT:
            if direction == (0, 0):
                snake.update()
            else:
                snake.move(direction)
                direction = (0, 0)

    screen.fill(BACKGROUND_COLOR)  # setting background color

    # draw grid
    for y in range(0, SCREEN_SIZE[1], CELL_SIZE):
        pg.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_SIZE[0], y))

    for x in range(0, SCREEN_SIZE[0], CELL_SIZE):
        pg.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_SIZE[1]))

    snake.draw(screen)

    pg.display.update()


pg.quit()  # destroy pygame istance
