import pygame
from Cell import Cell


class CrossWordle(pygame.Surface):
    MATRIX_WIDTH = 6

    def __init__(self, dest, letter_matrix, manager, cell_size):
        super().__init__((len(letter_matrix[0]) * (cell_size[0] + 10), len(letter_matrix) * (cell_size[1] + 10)))
        self.dest = dest
        self.cell_matrix = []
        self.init_cell_matrix(letter_matrix, manager, cell_size)

    def init_cell_matrix(self, letter_matrix, manager, cell_size):
        for i in range(self.MATRIX_WIDTH):
            row = []
            for j in range(self.MATRIX_WIDTH):
                row.append(Cell(relative_rect=pygame.Rect((self.dest[0] + 5 + (10 + cell_size[0]) * i,
                                                           self.dest[1] + 5 + (10 + cell_size[1]) * j), cell_size),
                                manager=manager))