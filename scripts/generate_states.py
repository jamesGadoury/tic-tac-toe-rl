from collections import defaultdict, deque
from json import dump

from common import REACHED_PATH, TERMINAL_STATES_PATH, serialize

from tic_tac_toe import new_board
from tic_tac_toe.tic_tac_toe import Board, available_plays, is_game_over, transition


def main():
    q: deque[Board] = deque([new_board()])
    reached_from: dict[str, list[str]] = defaultdict(list)
    terminal_states: list[str] = []

    while q:
        node = q.popleft()
        if is_game_over(node):
            terminal_states.append(serialize(node))
            continue
        for play in available_plays(node):
            child = transition(node, play)
            if child not in q:
                q.append(child)
            reached_from[serialize(child)].append(serialize(node))

    with open(REACHED_PATH, "w") as f:
        dump(reached_from, f)

    with open(TERMINAL_STATES_PATH, "w") as f:
        dump(terminal_states, f)


if __name__ == "__main__":
    main()
