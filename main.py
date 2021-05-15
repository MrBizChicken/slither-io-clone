from constants import *
import sys, pygame, player, enemy




sprites = pygame.sprite.Group()
sprites.add(player.Player(50, 50, (255, 0, 255)))
sprites.add(enemy.Enemy(400, 50, (200, 0, 0)))


screen_size = pygame.FULLSCREEN
surface = pygame.display.set_mode((0, 0), screen_size)
pygame.init()

def main():
    clock = pygame.time.Clock()


    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

        clock.tick(TICK_RATE)


        update()
        draw()


    pygame.quit()
    sys.exit()

def draw():
    
    surface.fill((100, 100, 100))#background


    sprites.draw(surface)

    pygame.display.flip()


def update():
    sprites.update()


if __name__ == "__main__":
    main()
