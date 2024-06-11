import pygame

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
#--------------------------------------------------------------------------------------------------------------------------------------------------        

interface = Game_frontend("First Game", 500, 500)
interface.enabling()
