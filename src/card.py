from enum import Enum
import pygame


class Suits(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3


class Card:
    suit = None
    rank = None
    image = None

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image = pygame.image.load('../resources/cards/' + suit.name.lower() + '_' + str(rank) + '.svg')

    def get_rank(self) -> int:
        return self.rank

    def get_suit(self) -> Suits:
        return self.suit
