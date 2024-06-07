import pygame

class Game_window:
    def __init__(self, game_name, window_width, window_height):
        self.__game_name = game_name
        self.__window_width = window_width
        self.__window_height = window_height
        self.__window = None
        self.__game_running = True
    
    def enabling(self):
        pygame.init()
        pygame.display.set_caption(self.__game_name)
        self.__window = pygame.display.set_mode((self.__window_width, self.__window_height))
        self.__window.fill((0, 151, 0))
    
    def rendering(self):
        while self.__game_running:
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__game_running = False
                
                pygame.display.update()
    
    def terminating(self):
        pygame.quit()
    
#--------------------------------------------------------------------------------------------------------------------------------------------------        


interface = Game_window("First Game", 800, 600)

interface.enabling()
interface.rendering()
interface.terminating()
