import pygame

class Game_frontend:
    def __init__(self, game_name, window_width, window_height):
        self.game_name = game_name
        self.window_width = window_width
        self.window_height = window_height
        self.game_running = True
    
    def enabling(self):
        def rendering():
            while self.game_running:
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_running = False

        pygame.init()
        pygame.display.set_caption(self.game_name)
        window = pygame.display.set_mode((self.window_width, self.window_height))
        rendering()
        pygame.quit()

#--------------------------------------------------------------------------------------------------------------------------------------------------        

interface = Game_frontend("First Game", 500, 500)
interface.enabling()
