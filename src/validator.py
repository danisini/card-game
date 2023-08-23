def is_bet_possible(balance, bet_price) -> bool:
    if balance < bet_price:
        return False

    return True
