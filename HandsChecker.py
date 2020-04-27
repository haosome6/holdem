from Card import Card


class HandsChecker:
    """To check the strength of hands.

    === Representation Invariant ===
    The length of list of cards passed in should be equal to 7.
    """

    def _straight_flush(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return "straight flush" and five cards make straight flush in tuple
        iff <cards> makes a straight flush, otherwise return the result of
        running _full_house with <cards>.
        """

    def _full_house(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return "full house" and five cards make full house in tuple iff
        <cards> makes a full house, otherwise return the result of running
        _flush with <cards>.
        """

    def _flush(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return "flush" and five cards make flush in tuple iff <cards> makes a
        flush, otherwise return the result of running _straight with <cards>.
        """

    def _straight(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return "straight" and five cards make straight in tuple iff <cards>
        makes a straight, otherwise return the result of running
        _three_of_a_kind with <cards>.
        """

    def _three_of_a_kind(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return "three of a kind" and five cards make it in tuple iff <cards>
        makes a three of kind, otherwise return the result of running _two_pair
        with <cards>.
        """

    def _two_pair(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return "two pair" and five cards make it in tuple iff <cards> makes a
        two pair, otherwise return the result of running _one_pair with <cards>.
        """

    def _one_pair(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return "one pair" and five cards make it in tuple iff <cards> makes a
        one pair, otherwise return the result of running _high_card with <cards>.
        """

    def _high_card(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return "high card" and five biggest cards in <cards> by descending
        order."""

    def _check_hands(self, cards: list[Card]) -> tuple[str, list[Card]]:
        """Return the strongest hand <cards> can make, and five cards make it.
        """

    def get_hands_type(self, cards: list[Card]) -> str:
        """Return the name of the strongest hand that <cards> can make.
        """

    def get_hands_cards(self, cards: list[Card]) -> list[Card]:
        """Return the five cards that make strongest hand.
        """

