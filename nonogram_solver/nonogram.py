from typing import (
    List,
    Optional,
)


class Nonogram:
    """Class for nonogram parameters and board."""

    verticals: List[List[int]] = [[]]
    horizontals: List[List[int]] = [[]]
    board: List[List[Optional[int]]] = [[]]

    def __init__(
        self,
        verticals: List[List[int]],
        horizontals: List[List[int]],
    ) -> None:
        self.verticals = verticals
        self.horizontals = horizontals
        self.fill_board(len(verticals), len(horizontals))

    def fill_board(self, width: int, height: int) -> None:
        """Initializes the board with the given width and height."""
        self.board = [[None] * width for _ in range(height)]
