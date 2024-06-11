import pygame

class Game:
    def __init__(self, game_name, window_width, window_height):
        self.__game_name = game_name
        self.__game_running = True
        self.__window = None
        self.__window_width = window_width
        self.__window_height = window_height
        self.__image_target = None
        self.__music_source = None
        self.__score = None
        self.__font = None
    
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

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = hand_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), random.randint(150, HEIGHT - 50))  # y 座標從 150 開始
        self.speed = random.randint(3, 12)  # 調整速度為3到8之間的隨機值

    def update(self):
        # 更新位置
        self.rect.x += random.randint(-self.speed, self.speed)
        self.rect.y += random.randint(-self.speed, self.speed)

        # 確保目標不會超出視窗邊界
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(50, min(self.rect.y, HEIGHT - self.rect.height - 50))  
        # 遊戲區從 y=50 開始，且保留一定空間
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------        


interface = Game("First Game", 800, 600)

interface.enabling()
interface.rendering()
interface.terminating()
