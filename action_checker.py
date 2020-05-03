class ActionChecker:
    """To check if the Player's betting is valid.

    === Private Attributes ===
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
    _biggest_bet: int
    _min_valid_raise: int

    def set_biggest_bet(self, amount: int) -> None:
        pass

    def get_biggest_bet(self) -> int:
        pass

    def set_min_valid_raise(self, amount: int) -> None:
        pass

    def get_biggest_bet(self) -> int:
        pass

    def valid_action(self, amount: int) -> bool:
        """A player's call equals the current biggest bet; or a raise which
        following the rules above. However, the player always have the option to
        all-in, this decision is valid regardless of what the current biggest
        bet is.
        """

