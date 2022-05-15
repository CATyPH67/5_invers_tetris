import random


class TetrisFigure:
    def __init__(self, table: list, dimension: int):
        self.table = table
        self.dimension = dimension


class Square(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1],
                          [1, 1]], 2)


class LineVertical(TetrisFigure):
    def __init__(self):
        super().__init__([[1],
                          [1],
                          [1]], 2)


class LineHorizontal(TetrisFigure):
    def __init__(self):
        super().__init__([1, 1, 1], 1)


class AngleVerticalLeftTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1],
                          [1, 0],
                          [1, 0]], 2)


class AngleVerticalLeftBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 0],
                          [1, 0],
                          [1, 1]], 2)


class AngleVerticalRightTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1],
                          [0, 1],
                          [0, 1]], 2)


class AngleVerticalRightBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[0, 1],
                          [0, 1],
                          [1, 1]], 2)


class AngleHorizontalLeftTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1, 1],
                          [1, 0, 0]], 2)


class AngleHorizontalLeftBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 0, 0],
                          [1, 1, 1]], 2)


class AngleHorizontalRightTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1, 1],
                          [0, 0, 1]], 2)


class AngleHorizontalRightBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[0, 0, 1],
                          [1, 1, 1]], 2)

# gff


class ZVerticalLeft(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 0],
                          [1, 1],
                          [0, 1]], 2)


class ZVerticalRight(TetrisFigure):
    def __init__(self):
        super().__init__([[0, 1],
                          [1, 1],
                          [1, 0]], 2)


class ZHorizontalLeft(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1, 0],
                          [0, 1, 1]], 2)


class ZHorizontalRight(TetrisFigure):
    def __init__(self):
        super().__init__([[0, 1, 1],
                          [1, 1, 0]], 2)


class PimpleVerticalLeft(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 0],
                          [1, 1],
                          [1, 0]], 2)


class PimpleVerticalRight(TetrisFigure):
    def __init__(self):
        super().__init__([[0, 1],
                          [1, 1],
                          [0, 1]], 2)


class PimpleHorizontalTop(TetrisFigure):
    def __init__(self):
        super().__init__([[1, 1, 1],
                          [0, 1, 0]], 2)


class ZHorizontalBottom(TetrisFigure):
    def __init__(self):
        super().__init__([[0, 1, 0],
                          [1, 1, 1]], 2)


def create_random_figure() -> TetrisFigure:
    factory_dict = {
        0: Square,
        1: Square,
        2: Square,
        3: Square,
        4: LineVertical,
        5: LineVertical,
        6: LineHorizontal,
        7: LineHorizontal,
        8: AngleVerticalLeftTop,
        9: AngleVerticalLeftBottom,
        10: AngleVerticalRightTop,
        11: AngleVerticalRightBottom,
        12: AngleHorizontalLeftTop,
        13: AngleHorizontalLeftBottom,
        14: AngleHorizontalRightTop,
        15: AngleHorizontalRightBottom,
        16: ZVerticalLeft,
        17: ZVerticalRight,
        18: ZHorizontalLeft,
        19: ZHorizontalRight,
        20: PimpleVerticalLeft,
        21: PimpleVerticalRight,
        22: PimpleHorizontalTop,
        23: ZHorizontalBottom
    }
    figure_number = random.randint(0, 23)
    return factory_dict[figure_number]()


