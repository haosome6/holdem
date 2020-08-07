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
    username: str
    _password: str
    total_amount: int

    def __init__(self, username: str, password: str) -> None:
        """Initialize the player with username <username>, password <password>
        and total_chips <total_chips>.
        """
        self.username = username
        self._password = password
        self.total_amount = 0

    def log_in(self, password: str) -> bool:
        """Return True iff <password> matches this Player's password.
        """
        return self._password == password
