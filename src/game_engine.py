from enum import Enum

import deck
import validator
import time
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
        self.lock = 0
        self.__calculate_chances__()

    def __calculate_chances__(self):
        print("HERE" + str(self.last_drawn.get_rank()))
        cnt_lower = self.deck.get_cnt_lower_by_card(self.last_drawn)
        cnt_higher = self.deck.get_cnt_higher_by_card(self.last_drawn)
        cnt_all = self.deck.get_cnt_all_cards()

        print(cnt_all, cnt_lower, cnt_higher)
        if cnt_all != 0:
            self.chance_lower = round((cnt_lower / cnt_all) * 100, 2)
            self.chance_higher = round((cnt_higher / cnt_all) * 100, 2)

    def __calculate_points(self, is_higher, bet_price):
        if is_higher:
            self.points += 100 * (100 - self.chance_higher) * (bet_price / self.balance)
        else:
            self.points += 100 * (100 - self.chance_lower) * (bet_price / self.balance)

        self.points = round(self.points, 2)

    def shuffle(self) -> (float, float, float):
        if self.lock != 1 and self.deck.get_cnt_all_cards() < 51:
            self.points = round(self.points / 2, 2)
            self.deck.shuffle()
            self.last_drawn = self.deck.draw_card()
            self.__calculate_chances__()

        return self.points, self.chance_lower, self.chance_higher

    def bet(self, bet_price: float, is_higher: bool) -> (float, float, float, float):

        if self.lock == 1:
            return self.balance, self.points, self.chance_lower, self.chance_higher
        else:
            self.lock = 1
            is_bet_possible = validator.is_bet_possible(self.balance, bet_price)
            if is_bet_possible == 0:
                self.lock = 0
                return self.balance, self.points, self.chance_lower, self.chance_higher

            curr_card = self.deck.draw_card()
            guess = self.__check_guess(curr_card, is_higher)

            if guess.value == 1:
                self.__calculate_points(is_higher, bet_price)

            self.last_drawn = curr_card
            self.__calculate_chances__()

            self.__update_balance(guess, bet_price)

            # should update points
            # should add field for cnt_guesses

            time.sleep(0.2)
            self.lock = 0

            return self.balance, self.points, self.chance_lower, self.chance_higher

    def get_last_drawn(self) -> card.Card:
        return self.last_drawn

    def __check_guess(self, curr_card, is_higher) -> GUESS:
        guess: GUESS
        print(self.last_drawn.get_rank(), curr_card.get_rank())
        if self.last_drawn.get_rank() > curr_card.get_rank():
            if is_higher:
                guess = GUESS.WRONG
            else:
                guess = GUESS.CORRECT
        elif self.last_drawn.get_rank() < curr_card.get_rank():
            if is_higher:
                guess = GUESS.CORRECT
            else:
                guess = GUESS.WRONG
        else:
            guess = GUESS.DRAW

        return guess

    def __update_balance(self, guess, bet_price) -> None:
        print(guess)
        print(bet_price)
        if guess.value == 1:
            self.balance += bet_price
        elif guess.value == 0:
            self.balance -= bet_price
