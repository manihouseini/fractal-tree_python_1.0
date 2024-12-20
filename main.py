import pygame, setting
from sys import exit
import tree
from utility import tools, pygame_tools

pygame.init()


class App:
    def __init__(self, WIDTH, HEIGHT, FPS) -> None:
        self.get_inputs()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CLOCK = pygame.time.Clock()
        self.FPS = FPS
        self.running = True

    def get_inputs(self):
        print(
            "use left and right mouse buttons while moving the mouse 2 animate the tree"
        )
        self.IS_CLEARED = int(
            tools.take_input("should the screen clear? 1 for yes 0 for no (1) : >", 1)
        )
        if not self.IS_CLEARED:
            self.SPEED_OF_SHIFT = tools.take_input(
                "at what speed should the shape form? (1): >", 1
            )

    def setup(self):
        self.starting_angle = 0

    def update(self):
        if self.IS_CLEARED:
            self.WIN.fill((0, 0, 0))
        else:
            self.starting_angle += self.SPEED_OF_SHIFT
        pygame_tools.debug(self.starting_angle, 10)
        tree.draw_tree(
            self.WIN, self.WIDTH / 2, self.HEIGHT, 10, 150, self.starting_angle
        )

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if pygame.mouse.get_pressed()[0]:
            self.starting_angle += 0.3
        if pygame.mouse.get_pressed()[2]:
            self.starting_angle -= 0.3

    def run(self):
        self.setup()
        while self.running:
            self.events()

            self.update()

            self.CLOCK.tick(self.FPS)
            pygame.display.set_caption(str(self.CLOCK.get_fps()))
            pygame.display.flip()


app = App(setting.window["width"], setting.window["height"], setting.window["fps"])
app.run()
