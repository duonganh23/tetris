import pygame

#game size
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# sidebar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

#WINDOW
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

#GAME BEHAVIOUR
UPDATE_START_SPEED = 600
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFF_SET = pygame.Vector2(COLUMNS // 2, -1)

#colors
yellow = '#f1e60d'
red = '#ff0505'
blue = "#0887dc"
green = "#2def06"
purple = "#8204F0"
cyan = '#00FFFF'
orange = "#f05908"
gray = "#908e8e"
line_color = '#ffffff'
score_panel_color = '#ffffff'

#shapes
TETROMINOS = {
    'T': {'shape' :[(0,0),(-1,0),(1,0),(0,-1)], 'color': purple},
    'O': {'shape':[(0,0),(0,-1),(1,0),(1,-1)], 'color': yellow},
    'J': {'shape' :[(0,0),(0,-1),(0,1),(-1,1)], 'color': blue},
    'L': {'shape' :[(0,0),(0,-1),(0,1),(1,1)],'color': orange},
    'I': {'shape' :[(0,0),(0,-1),(0,-2),(0,1)], 'color': cyan},
    'S': {'shape' :[(0,0),(-1,0),(0,-1),(1,-1)], 'color':green},
    'z': {'shape' :[(0,0),(1,0),(0,-1),(-1,-1)], 'color': red}
}
SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}