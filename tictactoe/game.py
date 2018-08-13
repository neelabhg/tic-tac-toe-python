class Game:
    '''Implements a single session of Tic-tac-toe'''

    def __init__(self, ui, board, tokens, player_factories, starting_player_index=0):
        assert len(player_factories) == len(tokens), 'Number of tokens and players must be the same'
        self.ui = ui
        self.board = board
        self.tokens = tokens
        self.current_player_index = starting_player_index
        self.num_players = len(player_factories)
        self.players = tuple(player_factories[i](board, tokens[i]) for i in range(self.num_players))

    def change_player(self):
        '''Switch the current player to the next one, in a round-robin fashion'''
        self.current_player_index = (self.current_player_index + 1) % self.num_players

    def get_current_player(self):
        return self.players[self.current_player_index]

    def is_complete(self):
        '''Determine whether the game has completed'''
        winning_token = self.board.get_winning_token()
        if winning_token:
            winning_player_index = self.tokens.index(winning_token)
            self.ui.display_winner(self.players[winning_player_index])
            return True
        if self.board.is_full():
            self.ui.display_tie()
            return True
        return False

    def tick(self):
        '''
        Perform a single iteration of the game loop.
        Return True if the game should continue, False otherwise.
        '''
        self.ui.display_board(self.board)
        if self.is_complete():
            return False
        player = self.get_current_player()
        self.ui.display_current_player(player)
        self.board.add_token(player.get_next_move(), self.tokens[self.current_player_index])
        self.change_player()
        return True

    def run(self):
        '''
        The game loop.
        Exits either when the game has ended or when the user causes a keyboard interrupt (Ctrl-C).
        '''
        try:
            while self.tick(): pass
        except KeyboardInterrupt:
            print() # Switch to a new line after the Ctrl-C control character
        finally:
            self.ui.display_exit_message()
