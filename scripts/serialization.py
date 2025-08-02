from functools import cache
from typing import cast

from tic_tac_toe import Board, new_board


@cache
def serialize(b: Board) -> str:
    return "".join(str(c) for c in b)


@cache
def deserialize(b: str) -> Board:
    return cast(Board, tuple([int(c) for c in b]))
