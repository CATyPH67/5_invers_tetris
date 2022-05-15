from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from tkinter import messagebox

from logic.game import Game
from logic.figure_factory import *
from PyQt5.QtCore import Qt

white_color = 'background-color:white; border-radius:5px'
black_color = 'background-color:black; border-radius:5px'
green_color = 'background-color:green; border-radius:5px'


class MainWindowUI(QMainWindow):

    def __init__(self):
        super(MainWindowUI, self).__init__()

        uic.loadUi('ui/main_window.ui', self)
        self.show()

        self.grid = self.findChild(QGridLayout, "boardLayout")
        self.figures_layout_1 = self.findChild(QGridLayout, "figuresLayout1")
        self.figures_layout_2 = self.findChild(QGridLayout, "figuresLayout2")
        self.figures_layout_3 = self.findChild(QGridLayout, "figuresLayout3")
        self.label_score = self.findChild(QLabel, "labelScore")

        self.game = Game()
        self.selecting_figure = None
        self.selecting_figure_x = None
        self.selecting_figure_y = None
        self.init_game()

    def init_game(self):
        self.draw_game_field(self.grid, self.game)
        self.draw_figure_field(self.figures_layout_1, self.game.figures[0])
        self.draw_figure_field(self.figures_layout_2, self.game.figures[1])
        self.draw_figure_field(self.figures_layout_3, self.game.figures[2])
        self.label_score.setText(str(self.game.score))
        if self.game.game_over:
            messagebox.showinfo('game over', 'your scores: ' + str(self.game.score))

    def draw_game_field(self, layout: QtWidgets.QGridLayout, game: Game):
        size = len(game.board)
        for row in range(size):
            for column in range(size):
                label = QtWidgets.QLabel()
                label.setAlignment(Qt.AlignCenter)
                if game.board[row][column] == 0:
                    label.mousePressEvent = self.click_to_move(column, row)
                    label.setStyleSheet(white_color)
                else:
                    label.mousePressEvent = self.click_to_move(column, row)
                    label.setStyleSheet(black_color)
                layout.addWidget(label, row, column)

    def draw_figure_field(self, layout: QtWidgets.QGridLayout, figure: TetrisFigure):
        for row in range(3):
            for column in range(3):
                label = QtWidgets.QLabel()
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(white_color)
                layout.addWidget(label, row, column)

        if figure.dimension == 1:
            size = len(figure.table)
            for column in range(size):
                label = QtWidgets.QLabel()
                label.setAlignment(Qt.AlignCenter)
                if figure.table[column] == 0:
                    label.mousePressEvent = self.select_figure(figure, column, 0)
                    label.setStyleSheet(white_color)
                else:
                    label.mousePressEvent = self.select_figure(figure, column, 0)
                    if figure == self.selecting_figure:
                        label.setStyleSheet(green_color)
                    else:
                        label.setStyleSheet(black_color)
                layout.addWidget(label, 0, column)

        if figure.dimension == 2:
            size_r = len(figure.table)
            size_c = len(figure.table[0])
            for row in range(size_r):
                for column in range(size_c):
                    label = QtWidgets.QLabel()
                    label.setAlignment(Qt.AlignCenter)
                    if figure.table[row][column] == 0:
                        label.mousePressEvent = self.select_figure(figure, column, row)
                        label.setStyleSheet(white_color)
                    else:
                        label.mousePressEvent = self.select_figure(figure, column, row)
                        if figure == self.selecting_figure:
                            label.setStyleSheet(green_color)
                        else:
                            label.setStyleSheet(black_color)
                    layout.addWidget(label, row, column)

    def select_figure(self, figure: TetrisFigure, selecting_figure_x: int, selecting_figure_y: int):
        def click(event):
            self.selecting_figure = figure
            self.selecting_figure_x = selecting_figure_x
            self.selecting_figure_y = selecting_figure_y
            self.init_game()
        return click

    def click_to_move(self, figure_x: int, figure_y: int):
        def click(event):
            if self.selecting_figure is not None:
                self.game.make_move(self.selecting_figure, figure_x - self.selecting_figure_x,
                                    figure_y - self.selecting_figure_y)
                self.selecting_figure = None
                self.selecting_figure_x = None
                self.selecting_figure_y = None
                self.init_game()
        return click

