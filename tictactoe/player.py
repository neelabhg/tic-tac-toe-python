import re
from .board import CellOccupiedError, PositionOutOfBoundsError
from .position import Position


class Player:
    def __init__(self, board, token):
        self.board = board
        self.token = token
        self.player_name = 'Player'

    def get_next_move(self):
        raise NotImplementedError('Subclass must define get_next_move')

    def __str__(self):
        return '{0} ({1})'.format(self.player_name, self.token)


class SimpleAI(Player):
    '''A Tic-tac-toe AI that simply picks the first available spot'''

    def __init__(self, board, token):
        super().__init__(board, token)
        self.player_name = 'Computer'

    def get_next_move(self):
        for column in range(self.board.num_columns):
            for row in range(self.board.num_rows):
                cell = self.board.cells_by_row[row][column]
                if cell.is_empty():
                    return Position(column, row)
        raise RuntimeError('Could not find a legal move')


class Human(Player):
    __position_re = re.compile(r'^[(\s]*(?P<column>\d+)\s*,\s*(?P<row>\d+)[\s)]*$')

    def __init__(self, board, token):
        super().__init__(board, token)
        self.player_name = 'Human'

    @classmethod
    def __parse_position(cls, s):
        match = cls.__position_re.match(s)
        if not match:
            raise ValueError(
                '"{0}" is not a valid position. '
                'A position must be specified as a "(column, row)" pair. '
                'Parentheses and whitespace are optional.'.format(s)
            )
        (column, row) = map(int, match.group('column', 'row'))
        return Position(column, row)

    def get_next_move(self):
        while True:
            try:
                i = input('Specify the position to place your token ({0}) as a (column, row) pair: '.format(self.token))
                position = self.__parse_position(i)
                cell = self.board.get_cell(position)
                if cell.is_occupied():
                    raise CellOccupiedError(position)
            except (PositionOutOfBoundsError, ValueError, CellOccupiedError) as e:
                print(e)
            else:
                return position
