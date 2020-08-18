class ActionChecker:
    """To check if the Player's betting is valid.

    === Private Attributes ===
    _big_blind:
        the big blind of the table
    _biggest_bet:
        current biggest bet on the table
    _min_valid_raise:
        minimum valid raise amount, any raises greater than or equal to this
        should be accepted

    === Rules of raising ===
    the minimum raise is equal to the size of the previous raise. If someone
    wishes to re-raise, they must raise at least the amount of the previous
    raise. For example, if the big blind is $2 and there is a raise of $6 to a
    total of $8, a re-raise must be at least $6 more for a total of $14.

    If a raise or re-raise is all-in and does not equal the size of the previous
    raise, it is considered as a call, and the initial raiser cannot re-raise
    again. In this case, _biggest_bet becomes the all-in, but _min_valid_raise
    stays the same.
    """
    _big_blind: int
    _biggest_bet: int
    _min_valid_raise: int

    def __init__(self, big_blind: int) -> None:
        """At the beginning of the game, the biggest bet is the big blind, and
        the min valid raise amount is two times the big blind.
        """
        self._big_blind = big_blind
        self._biggest_bet = big_blind
        self._min_valid_raise = big_blind * 2

    # set_new_street, street就是每一回合，flop是第一次发出三张公共牌的回合，turn是第四张，
    # river是第五张，这段看完可以删掉
    def set_new_street(self) -> None:
        """At the beginning of the flop, turn, and river, biggest bet and
        minimum valid raise should be re-set to zero.
        """
        self._biggest_bet, self._min_valid_raise = 0, self._big_blind

    def get_biggest_bet(self) -> int:
        return self._biggest_bet

    def get_min_valid_raise(self) -> int:
        return self._min_valid_raise

    def check_valid_action(self, bet_amount: int, is_all_in: bool) -> bool:
        """A player's call equals the current biggest bet; or a raise which
        following the rules above. However, the player always have the option to
        all-in, this decision is valid regardless of what the current biggest
        bet is.
        """
        if bet_amount == self._biggest_bet and self._biggest_bet != 0:
            return True
        # bet_amount not equal to _biggest_bet, it has to equal to or
        # greater than _min_valid_raise, otherwise it's invalid
        elif bet_amount >= self._min_valid_raise:
            self._min_valid_raise = bet_amount * 2 - self._biggest_bet
            self._biggest_bet = bet_amount
            return True
        else:
            # bet_amount is not equal to _biggest_bet, and less than
            # _min_valid_raise, it's valid iff it's all in
            if is_all_in:
                self._biggest_bet = max(self._biggest_bet, bet_amount)
                return True
            else:
                return False
