import random


class TetrisFigure:
    def __init__(self, table: list):
        self.table = table

    def get_table(self) -> list:
        return self.table


class Square(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1],
                          [1, 1]])


class LineVertical(TetrisFigure):
    def __init__(self):
        super().__init__([[1],
                          [1],
                          [1]])


class LineHorizontal(TetrisFigure):
    def __init__(self):
        super().__init__([1, 1, 1])


class AngleVerticalLeftTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1],
                          [1, 0],
                          [1, 0]])


class AngleVerticalLeftBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 0],
                          [1, 0],
                          [1, 1]])


class AngleVerticalRightTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1],
                          [0, 1],
                          [0, 1]])


class AngleVerticalRightBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[0, 1],
                          [0, 1],
                          [1, 1]])


class AngleHorizontalLeftTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1, 1],
                          [1, 0, 0]])


class AngleHorizontalLeftBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 0, 0],
                          [1, 1, 1]])


class AngleHorizontalRightTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1, 1],
                          [0, 0, 1]])


class AngleHorizontalRightBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[0, 0, 1],
                          [1, 1, 1]])


def create_random_figure() -> TetrisFigure:
    factory_dict = {
        0: Square,
        1: LineVertical,
        2: LineHorizontal,
        3: AngleVerticalLeftTop,
        4: AngleVerticalLeftBottom,
        5: AngleVerticalRightTop,
        6: AngleVerticalRightBottom,
        7: AngleHorizontalLeftTop,
        8: AngleHorizontalLeftBottom,
        9: AngleHorizontalRightTop,
        10: AngleHorizontalRightBottom
    }
    figure_number = random.randint(0, 10)
    return factory_dict[figure_number]()


