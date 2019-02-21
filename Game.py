import pygame
import os


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.move = 0
        self.end_game = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        ii = 0
        for i in range(self.top, self.height * self.cell_size + self.left, self.cell_size):
            jj = 0
            for j in range(self.left, self.width * self.cell_size + self.top, self.cell_size):
                pygame.draw.rect(screen, (0, 0, 0), (j, i, self.cell_size, self.cell_size), 5)
                if self.board[ii][jj] == 1:
                    pygame.draw.line(screen, pygame.Color("red"), (j, i), (j + self.cell_size, i + self.cell_size), 10)
                    pygame.draw.line(screen, pygame.Color("red"), (j, i + self.cell_size), (j + self.cell_size, i), 10)
                elif self.board[ii][jj] == 2:
                    pygame.draw.circle(screen, pygame.Color("blue"), (j + self.cell_size // 2, i + self.cell_size // 2),
                                       self.cell_size // 2, 10)
                jj += 1
            ii += 1
        if self.end_game == 1:
            self.cross_win()
        if self.end_game == 2:
            self.zero_win()

    def zero_win(self):
        pygame.draw.circle(screen, pygame.Color('blue'), (40, 50), self.cell_size // 2, 10)
        pygame.draw.line(screen, pygame.Color("black"), (90, 0), (90, 110), 5)
        pygame.draw.line(screen, pygame.Color("black"), (90, 110), (0, 110), 5)
        pygame.draw.line(screen, pygame.Color('blue'), (100, 0), (120, 100), 10)
        pygame.draw.line(screen, pygame.Color('blue'), (120, 100), (140, 0), 10)
        pygame.draw.line(screen, pygame.Color('blue'), (140, 0), (160, 100), 10)
        pygame.draw.line(screen, pygame.Color('blue'), (160, 100), (180, 0), 10)
        pygame.draw.line(screen, pygame.Color('blue'), (200, 0), (200, 100), 10)
        pygame.draw.line(screen, pygame.Color('blue'), (220, 0), (220, 100), 10)
        pygame.draw.line(screen, pygame.Color('blue'), (220, 0), (260, 100), 10)
        pygame.draw.line(screen, pygame.Color('blue'), (260, 100), (260, 0), 10)

    def cross_win(self):
        pygame.draw.line(screen, pygame.Color("red"), (0, 0), (80, 100), 10)
        pygame.draw.line(screen, pygame.Color("red"), (0, 100), (80, 0), 10)
        pygame.draw.line(screen, pygame.Color("black"), (90, 0), (90, 110), 5)
        pygame.draw.line(screen, pygame.Color("black"), (90, 110), (0, 110), 5)
        pygame.draw.line(screen, pygame.Color('red'), (100, 0), (120, 100), 10)
        pygame.draw.line(screen, pygame.Color('red'), (120, 100), (140, 0), 10)
        pygame.draw.line(screen, pygame.Color('red'), (140, 0), (160, 100), 10)
        pygame.draw.line(screen, pygame.Color('red'), (160, 100), (180, 0), 10)
        pygame.draw.line(screen, pygame.Color('red'), (200, 0), (200, 100), 10)
        pygame.draw.line(screen, pygame.Color('red'), (220, 0), (220, 100), 10)
        pygame.draw.line(screen, pygame.Color('red'), (220, 0), (260, 100), 10)
        pygame.draw.line(screen, pygame.Color('red'), (260, 100), (260, 0), 10)

    def get_cell(self, mouse_pos):
        x = mouse_pos[0] - self.left
        y = mouse_pos[1] - self.top
        if x < 0 or y < 0:
            return None
        if y >= self.height * self.cell_size:
            return None
        if x >= self.width * self.cell_size:
            return None
        return y // self.cell_size, x // self.cell_size

    def on_click(self, cell_coords):
        if self.end_game == 0:
            if self.board[cell_coords[0]][cell_coords[1]] == 0:
                self.board[cell_coords[0]][cell_coords[1]] = self.move + 1
                self.move += 1
                self.move %= 2
            for i in range(3):
                if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                    if self.board[0][i] == 1:
                        self.end_game = 1
                    if self.board[0][i] == 2:
                        self.end_game = 2
                if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                    if self.board[i][0] == 1:
                        self.end_game = 1
                    if self.board[i][0] == 2:
                        self.end_game = 2
            if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
                if self.board[0][0] == 1:
                    self.end_game = 1
                if self.board[0][0] == 2:
                    self.end_game = 2
            if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
                if self.board[0][2] == 1:
                    self.end_game = 1
                if self.board[0][2] == 2:
                    self.end_game = 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        try:
            self.on_click(cell)
        except Exception:
            return False


pygame.init()
size = width, height = 512, 512
screen = pygame.display.set_mode(size)
board = Board(3, 3)
board.set_view(146, 146, 80)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill(pygame.Color("yellow"))
    board.render()
    pygame.display.flip()
