from settings import *
from sys import exit

#components
from game import Game
from score import Score
from preview import Preview
from random import choice
class Main:
    def __init__(self):
        #general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetoris')
        self.game_over = False
        #shapes
        self.next_shapes = [choice(list(TETROMINOS.keys()))for shape in range(3)]
        print(self.next_shapes)

        #components
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys()))) 
        return next_shape

    def draw_game_over(self):
        self.display_surface.fill((0,0,0))
        font = pygame.font.Font(None, 60)
        text = font.render('GAME OVER', True, 'white')
        text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.display_surface.blit(text, text_rect)

        font_small = pygame.font.Font(None, 30)
        restart_text = font_small.render('Press F to restart', True, 'white')
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 30))
        self.display_surface.blit(restart_text, restart_rect)

    def restart(self):
        self.next_shapes = [choice(list(TETROMINOS.keys()))for shape in range(3)]
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()
        self.game_over = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #exit everything
                    exit()
                if event.type == pygame.KEYDOWN:
                    if self.game_over and event.key == pygame.K_f:
                        self.restart()
            if self.game.game_over:
                self.game_over = True
            #display
            self.display_surface.fill(red)
            if not self.game.game_over:
            #components
                self.game.run()
                self.score.run()
                self.preview.run(self.next_shapes)
            else:
                self.draw_game_over()
            #updating
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
    main.run()
