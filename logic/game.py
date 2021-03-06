from logic import figure_factory


class Game:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        self.figures = [figure_factory.create_random_figure(),
                        figure_factory.create_random_figure(),
                        figure_factory.create_random_figure()]
        self.score = 0
        self.game_over = False

    def make_move(self, tetrisFigure: figure_factory.TetrisFigure, figure_x: int, figure_y: int):
        if self.is_move_possible(tetrisFigure, figure_x, figure_y):
            x = figure_x
            y = figure_y
            figure_table = tetrisFigure.table

            if tetrisFigure.dimension == 1:
                for num in figure_table:
                    self.board[y][x] = num + self.board[y][x]
                    x = x + 1

            if tetrisFigure.dimension == 2:
                for row in figure_table:
                    for num in row:
                        self.board[y][x] = num + self.board[y][x]
                        x = x + 1
                    x = figure_x
                    y = y + 1

            self.check_line_filling()

            i = self.figures.index(tetrisFigure)
            self.figures[i] = figure_factory.create_random_figure()

            self.game_over = self.is_game_over()

    def is_move_possible(self, tetrisFigure: figure_factory.TetrisFigure, figure_x: int, figure_y: int) -> bool:
        if figure_x < 0 or figure_y < 0:
            return False

        x = figure_x
        y = figure_y
        figure_table = tetrisFigure.table

        if tetrisFigure.dimension == 1:
            if len(figure_table) + x <= len(self.board[0]):
                for num in figure_table:
                    if num + self.board[y][x] > 1:
                        return False
                    x = x + 1
            else:
                return False

        if tetrisFigure.dimension == 2:
            if len(figure_table) + y <= len(self.board) and len(figure_table[0]) + x <= len(self.board[0]):
                for row in figure_table:
                    for num in row:
                        if num + self.board[y][x] > 1:
                            return False
                        x = x + 1
                    x = figure_x
                    y = y + 1
            else:
                return False

        return True

    def check_line_filling(self):
        new_score = 0
        for y in range(len(self.board)):
            is_line_fill = True
            for x in range(len(self.board[0])):
                if self.board[y][x] == 0:
                    is_line_fill = False
            if is_line_fill:
                for x in range(len(self.board[0])):
                    self.board[y][x] = 0
                new_score = new_score * 2 + 100
        for x in range(len(self.board[0])):
            is_line_fill = True
            for y in range(len(self.board)):
                if self.board[y][x] == 0:
                    is_line_fill = False
            if is_line_fill:
                for y in range(len(self.board)):
                    self.board[y][x] = 0
                new_score = new_score * 2 + 100

        self.score = self.score + new_score

    def is_game_over(self) -> bool:
        for figure in self.figures:
            for y in range(len(self.board) - len(figure.table)):
                for x in range(len(self.board[0]) - len(figure.table[0])):
                    if self.is_move_possible(figure, x, y):
                        return False
        return True
