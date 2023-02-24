import pygame as pg

pg.init() # initialize pygame

# costants
SCREEN_SIZE = (800, 800)
CELL_SIZE = 800//20
GRID_COLOR = (255,255,255)
BACKGROUND_COLOR = (55,55,55)

screen = pg.display.set_mode(SCREEN_SIZE) # creating a screen with the given size
clock = pg.time.Clock() # creating a default clock

# game loop
running = True
while running:
    for event in pg.event.get(): # handle pygame events
        if event.type == pg.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR) # setting background color

    # draw grid
    for y in range(0, SCREEN_SIZE[1], CELL_SIZE):
        pg.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_SIZE[0],y))
        
    for x in range(0, SCREEN_SIZE[0], CELL_SIZE):
        pg.draw.line(screen, GRID_COLOR, (x, 0), (x,SCREEN_SIZE[1]))
    
    pg.display.update()


pg.quit() # destroy pygame istance