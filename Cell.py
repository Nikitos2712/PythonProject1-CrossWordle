import pygame_gui
import pygame


class Cell(pygame_gui.elements.UITextEntryLine):

    def __init__(self, relative_rect, manager):
        super().__init__(relative_rect, manager, placeholder_text="_")
        self.set_text_length_limit(2)

    def update_text(self, new_char):
        if new_char == "\u0008":
            self.text = ""
        else :
            self.set_text(" " * (self.length_limit - 1) + new_char.upper())
        self.redraw()

    def change_color_to_green(self):
        self.background_colour = pygame.Color('#7fff00')
        self.rebuild()

    def change_color_to_yellow(self):
        self.background_colour = pygame.Color('#EDFF21')
        self.rebuild()

    def get_color(self):
        return self.background_colour

    def is_empty(self):
        return self.text == ""