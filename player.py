import main_block, pygame

class Player(main_block.Main_block):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.speed = 10

    def update(self):
        self.input()
        self.chase()
        pygame.mouse.get_pos()

    def input(self):
        keys = pygame.key.get_pressed()
        # UP
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect = self.rect.move(0, -self.speed)

        # DOWN
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect = self.rect.move(0, self.speed)

        # LEFT
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect = self.rect.move(-self.speed, 0)

        # Right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect = self.rect.move(self.speed, 0)



    def chase(self):
        mx, my = pygame.mouse.get_pos()

        if  my  > self.rect.y:
            self.rect = self.rect.move(0, self.speed)

        if  my < self.rect.y:
            self.rect = self.rect.move(0, -self.speed)

        if mx  > self.rect.x:
            self.rect = self.rect.move(self.speed, 0)

        if mx < self.rect.x:
            self.rect = self.rect.move(-self.speed, 0)
