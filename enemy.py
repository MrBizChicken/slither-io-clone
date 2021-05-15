import main_block, pygame

class Enemy(main_block.Main_block):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.speed = 5

    def update(self):
        
        self.chase()
    #
    # def move(self):
    #
    #     gw = pygame.display.Info().current_w
    #     gh = pygame.display.Info().current_w
    #     self.rect = self.rect.move(self.speed, 0)
    #
    #     if self.rect.right > gw or self.rect.left < 0:
    #         self.speed = -self.speed
    #




    def chase(self):
        group = self.groups()[0]
        player = group.sprites()[0]
        # print(player.rect)

        if player.rect.y  > self.rect.y:
            self.rect = self.rect.move(0, self.speed)

        if player.rect.y < self.rect.y:
            self.rect = self.rect.move(0, -self.speed)

        if player.rect.x  > self.rect.x:
            self.rect = self.rect.move(self.speed, 0)

        if player.rect.x < self.rect.x:
            self.rect = self.rect.move(-self.speed, 0)
