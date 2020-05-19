from __future__ import annotations


class Player:
    """A player of the game.

    ===Attributes===
    username:
        The username of the player.
    password:
        The password of the player.
    total_chips:
        The total chips of the player that is not playing.
    """
    _username: str
    _password: str
    _total_chips: int

    def __init__(self, username: str, password: str) -> None:
        """Initialize the player with username <username>, password <password>
        and total_chips <total_chips>.
        """
        self._username = username
        self._password = password
        self._total_chips = 0

    def log_in(self, password: str) -> bool:
        """Return True iff <password> matches this Player's password.
        """
        return self._password == password

    def get_username(self) -> str:
        """Return the username of this Player.
        """
        return self._username

    def add_to_total_chips(self, amount: int) -> None:
        """Deposit money into _total_chips."""
        self._total_chips += amount

    def take_from_total_chips(self, amount: int) -> None:
        """Take money from _total_chips into gaming."""
        self._total_chips -= amount
