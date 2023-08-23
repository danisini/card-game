import random
import card


class Deck:
    cards_left = None
    drawn_cards = None

    def __init__(self):
        self.last_drawn = None
        self.cards_left = []
        self.drawn_cards = []
        self.__add_cards()

    def get_cnt_lower_by_card(self, given_card: card.Card) -> int:
        cnt = 0
        for curr_card in self.cards_left:
            if curr_card.get_rank() < given_card.get_rank():
                cnt += 1

        return cnt

    def get_cnt_higher_by_card(self, given_card: card.Card) -> int:
        cnt = 0
        for curr_card in self.cards_left:
            if curr_card.get_rank() > given_card.get_rank():
                cnt += 1

        return cnt

    def get_cnt_all_cards(self) -> int:
        return len(self.cards_left)

    def draw_card(self) -> card.Card:
        self.last_drawn = self.cards_left.pop()
        self.drawn_cards.append(self.last_drawn)
        return self.last_drawn

    def shuffle(self) -> None:
        self.last_drawn = None
        self.cards_left = []
        self.drawn_cards = []

        self.__add_cards()

    def __add_cards(self) -> None:
        for suit in card.Suits:
            for rank in range(1, 14):
                self.cards_left.append(card.Card(suit, rank))

        random.shuffle(self.cards_left)


