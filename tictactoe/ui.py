class UserInterface:
    pass


class ConsoleUserInterface(UserInterface):
    def __init__(self):
        pass

    def display_separator(self):
        print('_' * 40)

    def display_board(self, board):
        self.display_separator()
        print(board)

    def display_current_player(self, player):
        print('Now playing: {0}'.format(player))

    def display_winner(self, player):
        print('{0} wins!'.format(player))

    def display_tie(self):
        print('It\'s a tie!')

    def display_exit_message(self):
        self.display_separator()
        print('Exiting. Thanks for playing!')
