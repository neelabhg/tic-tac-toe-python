import random
from .game import Game
from .board import Board
from .player import Human, SimpleAI
from .tokens import PLAYER_TOKENS
from .ui import ConsoleUserInterface


def main():
    tokens = list(PLAYER_TOKENS)
    random.shuffle(tokens)
    Game(
        ConsoleUserInterface(),
        Board(),
        tuple(tokens),
        (SimpleAI, Human),
        random.randint(0, 1)
    ).run()


if __name__ == '__main__':
    main()
