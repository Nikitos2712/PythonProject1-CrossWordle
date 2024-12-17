import pygame
import pygame_gui
from Cell import Cell
from CrossWordle import CrossWordle
from letters import LETTER_MATRIX
from VirtualKeyboard import VirtualKeyboard

SCREEN_WIDTH = 1380
SCREEN_HEIGHT = 980
CELL_WIDTH = 90
CROSSWORDLE_WIDTH = 500

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 10

        # Настройки экрана
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#, pygame.RESIZABLE
        self.screen.fill("#c4f5f0")
        pygame.display.set_caption("CrossWordle")

        #UIManager
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), theme_path="theme.json")

        #CrossWordle
        self.cross_wordle = CrossWordle((50, 25), LETTER_MATRIX, manager = self.manager,
                                        cell_size=(CELL_WIDTH, CELL_WIDTH))
        self.cross_wordle.fill("#82e4ff")
        self.screen.blit(self.cross_wordle, self.cross_wordle.dest)

        #Клавиатура
        #self.keyboard = VirtualKeyboard(self.manager)



    def launch(self):
        running = True
        while running:

            #Обновление состояния игры


            # Отрисовка
            self.manager.draw_ui(self.screen)
            pygame.display.update()


            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Обработка ввода текста
                    if event.unicode:
                        pass
                self.manager.process_events(event)

            # Контроль ФПС
            time_delta = self.clock.tick(self.fps) / 1000
            self.manager.update(time_delta)

        self.__del__()


    def __del__(self):
        pygame.quit()