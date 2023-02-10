from enum import Enum
import pygame


class Suits(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


class Card:
    suit = None
    rank = None
    image = None

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image = pygame.image.load('../resources/cards/' + suit.name + '-' + str(rank) + '.svg')

    def get_rank(self):
        return self.rank
