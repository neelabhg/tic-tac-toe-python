import os
from .cell import Cell
from .position import Position
from .tokens import TOKEN_EMPTY


class PositionOutOfBoundsError(IndexError):
    def __init__(self, position):
        self.position = position
        self.message = '{0} is out of bounds'.format(position)

    def __str__(self):
        return self.message


class CellOccupiedError(Exception):
    def __init__(self, position):
        self.position = position
        self.message = 'Cell at {0} is occupied'.format(position)

    def __str__(self):
        return self.message


class Board:
    '''Represents a 2D board for the Tic Tac Toe game'''

    def __init__(self, columns=3, rows=3):
        if columns <= 0 or rows <= 0:
            raise ValueError('Cannot construct a {0}x{1} board'.format(columns, rows))
        self.num_columns = columns
        self.num_rows = rows
        self.num_empty_cells = columns * rows
        self._cells = tuple(
            tuple(Cell() for __ in range(self.num_columns))
                for __ in range(self.num_rows)
        )
        # Pre-compute different "views" of the board for faster access
        self.cells_by_row = self._cells
        self.cells_by_column = tuple(
            tuple(row[column_index] for row in self.cells_by_row)
                for column_index in range(self.num_columns)
        )
        self.cells_by_diagonal = self.__compute_diagonals()
        self.axes = self.cells_by_row + self.cells_by_column + self.cells_by_diagonal

    def __compute_diagonals(self):
        if self.num_columns != self.num_rows:
            # Not a square
            return ()
        N = self.num_columns
        # A 2D square has exactly two diagonals
        diagonal1 = tuple(self.cells_by_row[i][i] for i in range(N))
        diagonal2 = tuple(self.cells_by_row[i][N - 1 - i] for i in range(N))
        return (diagonal1, diagonal2)

    def __str__(self):
        lines = ('|'.join(map(str, row)) for row in self.cells_by_row)
        return os.linesep.join(lines)

    def get_cell(self, position):
        '''Return the board cell at the given position'''
        if (position.column < 0 or position.column >= self.num_columns or
            position.row < 0 or position.row >= self.num_rows):
            raise PositionOutOfBoundsError(position)
        return self.cells_by_row[position.row][position.column]

    def add_token(self, position, token):
        '''Add a token to the board at position (column, row)'''
        cell = self.get_cell(position)
        if cell.is_occupied():
            raise CellOccupiedError(position)
        cell.token = token
        self.num_empty_cells -= 1

    def is_full(self):
        '''Return whether the board is full'''
        return self.num_empty_cells == 0

    def get_winning_token(self):
        '''
        Returns the token appearing across an entire axis (horizontal, vertical, or diagonal) if present, None otherwise.
        In case multiple tokens meet this condition, only the first one found will be returned.
        '''
        for axis in self.axes:
            tokens = tuple(map(lambda cell: cell.token, axis))
            first = tokens[0]
            if first != TOKEN_EMPTY and all(token == first for token in tokens):
                return first
        return None
