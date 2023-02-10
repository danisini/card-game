import random
from enum import Enum
import pygame
import card


class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for suit in card.Suits:
            for rank in range(1, 14):
                self.cards.append(card.Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

