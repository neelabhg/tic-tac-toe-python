from .tokens import VALID_TOKENS, TOKEN_EMPTY


class Cell:
    def __init__(self):
        self.token = TOKEN_EMPTY

    def __str__(self):
        return self.token

    def is_empty(self):
        return self.token == TOKEN_EMPTY

    def is_occupied(self):
        return not self.is_empty()

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        if value not in VALID_TOKENS:
            raise ValueError('Invalid token {0}'.format(value))
        self._token = value
