import copy
from typing import (
    Generator,
    List,
    Optional,
)

from nonogram_solver.nonogram import Nonogram  # type:ignore


class Solver:
    pos = 0
    work_on = "x"

    def __init__(self, nonogram: Nonogram):
        self.nonogram: Nonogram = nonogram

    def _permutations(
        self,
        line: List[Optional[int]],
        specs: List[int],
    ) -> Generator[List[Optional[int]], None, None]:
        """
        Recursive method that yields all possible permutations of the given line given the specs

         >>> get_permutations([None, None], [1])
        [1, 0]
        [0, 1]

        >>> get_permutations([1, None], [1])
        [1, 0]
        """
        # if no specs line must be empty
        if not specs:
            yield [0] * len(line)
            return

        # get first and other blocks
        block, other_blocks = specs[0], specs[1:]

        # get all possible permutations of space before the first block
        space_needed_for_other_blocks = len(other_blocks) + sum(other_blocks)
        for space in range(len(line) - space_needed_for_other_blocks - block + 1):
            # check if this amount of space is valid
            if any(line[:space]):
                break
            if any((sub_line == 0 for sub_line in line[space:space + block])) or \
                    (len(line) > (space + block) and line[space + block]) or \
                    not other_blocks and any(line[space + block:]):
                continue

            # recurse call permutations for each blocks
            for permutation in self._permutations(line[space + block + 1:], other_blocks):
                l2 = line.copy()
                l2[:space] = [0] * space  # space of length space
                l2[space:space + block] = [1] * block  # fill of length block
                if len(line) > space + block:
                    l2[space + block] = 0  # then a empty block if needed
                l2[space + block + 1:] = permutation  # then the rest
                yield l2

    def _next_step(self):
        """
        Increase the internal position counters by 1.

        For horizontal use x and y for vertical axis.
        """

        if self.work_on == "x" and self.pos >= len(self.nonogram.horizontals) - 1:
            self.work_on = "y"
            self.pos = 0
        elif self.work_on == "y" and self.pos >= len(self.nonogram.verticals) - 1:
            self.work_on = "x"
            self.pos = 0
        else:
            self.pos += 1

    def _solve_step(self, pos: int, work_on: str):
        """Solve a single step, returns whether something has changed."""

        if work_on == "x":
            step_result = self._solve_line(self.nonogram.board[pos].copy(), self.nonogram.horizontals[pos])
            did_anything = self.nonogram.board[pos] != step_result
            self.nonogram.board[pos] = step_result
        else:
            step_result = self._solve_line([c[pos] for c in self.nonogram.board], self.nonogram.verticals[pos])
            did_anything = 0
            for i, r in enumerate(step_result):
                did_anything = did_anything or r != self.nonogram.board[i][pos]
                self.nonogram.board[i][pos] = r
        return did_anything

    def _solve_line(self, line: List[Optional[int]], specs: List[int]) -> List[Optional[int]]:
        """"Solves a single line (horizontal or vertical) according to the spec."""

        permutations = self._permutations(line, specs)
        # Set fields that agree in all permutations, if a field is 1 in all permutations
        # it is set to 1 in the solved line
        columns = zip(*permutations)
        for i, states in enumerate(columns):
            if all(states):
                line[i] = 1
            elif all((cell == 0 for cell in states)):  # == 0 because we have None values
                line[i] = 0
        return line

    def solve_step(self) -> bool:
        current_pos = self.pos
        current_work_on = self.work_on

        # loop over all possible lines until we have done something or we have gone a full round without doing anything
        done_anything = self._solve_step(self.pos, self.work_on)
        while not done_anything:
            self._next_step()
            if self.pos == current_pos and self.work_on == current_work_on:
                return False
            done_anything = self._solve_step(self.pos, self.work_on)
        self._next_step()
        return True

    def solve_all(self) -> List[List[Optional[int]]]:
        """Solve all steps and return final result."""
        while True:
            if not self.solve_step():
                break
        result_board: List[List[Optional[int]]] = copy.deepcopy(self.nonogram.board)
        return result_board


def solve(
    verticals: List[List[int]],
    horizontals: List[List[int]],
) -> List[List[Optional[int]]]:
    """Function for solve given nonogram."""
    nonogram = Nonogram(
        verticals=verticals,
        horizontals=horizontals,
    )
    solver = Solver(nonogram=nonogram)
    return solver.solve_all()


if __name__ == '__main__':
    # it's just for example
    result = solve(
        [[1, 1, 2], [1, 2], [6], [1]],
        [[3], [2], [1, 1], [2], [3], [1, 1]],
    )
    for row in result:
        print(' '.join(str(i) for i in row))
