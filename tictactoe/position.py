class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

    def __str__(self):
        return 'Position({0}, {1})'.format(self.column, self.row)
