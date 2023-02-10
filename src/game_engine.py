from enum import Enum

import deck
import validator
from src import card


class GUESS(Enum):
    CORRECT = 1
    WRONG = 0
    DRAW = 2


class GameEngine:

    def __init__(self, balance: float):
        self.balance = balance
        self.points = 0.0
        self.deck = deck.Deck()
        self.last_drawn = self.deck.draw_card()
        self.__calculate_chances__()

    def __calculate_chances__(self):
        cnt_lower = self.deck.get_cnt_lower_by_card(self.last_drawn)
        cnt_higher = self.deck.get_cnt_higher_by_card(self.last_drawn)
        cnt_all = self.deck.get_cnt_all_cards()

        if cnt_all != 0:
            self.chance_lower = (cnt_lower / cnt_all) * 100
            self.chance_higher = (cnt_higher / cnt_all) * 100

    def bet(self, bet_price: float, is_higher: bool) -> (float, card.Card):
        validator.is_bet_possible(self.balance, bet_price)
        curr_card = self.deck.draw_card()
        guess = self.__check_guess(curr_card, is_higher)
        self.last_drawn = curr_card

        self.__update_balance(guess, bet_price)

        # should update points
        # should add field for cnt_guesses

        return self.balance, curr_card

    def get_last_drawn(self) -> card.Card:
        return self.last_drawn

    def __check_guess(self, curr_card, is_higher) -> GUESS:
        guess: GUESS
        if self.last_drawn.get_rank() > curr_card.get_rank():
            if is_higher:
                guess = GUESS.WRONG
            else:
                guess = GUESS.CORRECT
        elif self.last_drawn.get_rank() > curr_card.get_rank():
            if is_higher:
                guess = GUESS.CORRECT
            else:
                guess = GUESS.WRONG
        else:
            guess = GUESS.DRAW

        return guess

    def __update_balance(self, guess, bet_price) -> None:
        if guess.value == 1:
            self.balance += bet_price
        elif guess.value == 0:
            self.balance -= bet_price














