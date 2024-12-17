import pygame


class VirtualKeyboard(pygame.Surface):
    width = 500
    height = 200

    def __init__(self, manager):
        super().__init__((self.width, self.height))
        self.manager = manager

        # Создание кнопок для клавиатуры
        self.buttons = {}
        self.init_buttons()

    def init_buttons(self):
        pass #Todo
