import deck


class GameEngine:

    def __init__(self, balance):
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



