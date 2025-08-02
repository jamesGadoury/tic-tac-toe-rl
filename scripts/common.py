from functools import cache
from pathlib import Path
from typing import cast

from tic_tac_toe import Board, new_board

REACHED_PATH: Path = Path("reached.json")
TERMINAL_STATES_PATH: Path = Path("terminal_states.json")


@cache
def serialize(b: Board) -> str:
    return "".join(str(c) for c in b)


@cache
def deserialize(b: str) -> Board:
    return cast(Board, tuple([int(c) for c in b]))
