from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *

from logic import game
from logic.game import Game
from PyQt5.QtCore import Qt


class MainWindowUI(QMainWindow):

    def __init__(self):
        super(MainWindowUI, self).__init__()

        uic.loadUi('ui/main_window.ui', self)
        self.show()

        self.board_layout = self.findChild(QGridLayout, "boardLayout")

        self.game = Game()

        self.fill_board(self.board_layout)

    def fill_board(self, board: QGridLayout):
        point_to_label = dict()
        size = len(self.game.get_board())
        for row in range(size):
            for column in range(size):
                label = QtWidgets.QLabel()
                label.setAlignment(Qt.AlignCenter)
                if self.game.board[row][column] == 0:
                    point_to_label[(row, column)] = label
                else:
                    point_to_label[(row, column)] = label
                board.addWidget(label, row, column)
        return point_to_label
