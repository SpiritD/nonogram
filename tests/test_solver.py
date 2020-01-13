import pytest

from nonogram_solver.solver import (
    solve,
    Solver,
)


@pytest.mark.parametrize(
    'line, specs, expected',
    [
        [
            [None, None, None, None],
            [4],
            [[1, 1, 1, 1]],
        ],
        [
            [None, None, None, None],
            [1, 1],
            [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1]],
        ],
        [
            [1, None, None, None],
            [1, 1],
            [[1, 0, 1, 0], [1, 0, 0, 1]],
        ],
        [
            [0, None, None, None],
            [1, 1],
            [[0, 1, 0, 1]],
        ],
    ]
)
def test_permutations(line, specs, expected):
    solver = Solver(None)
    results = list(var for var in solver._permutations(line=line, specs=specs))
    assert results == expected


@pytest.mark.parametrize(
    'line, specs, expected',
    [
        [
            [None, None, None, None],
            [4],
            [1, 1, 1, 1],
        ],
        [
            [None, None, None, None],
            [1, 1],
            [None, None, None, None],
        ],
        [
            [None, 1, None, None],
            [3],
            [None, 1, 1, None],
        ],
    ]
)
def test_solve_line(line, specs, expected):
    solver = Solver(None)
    results = list(var for var in solver._solve_line(line=line, specs=specs))
    assert results == expected


@pytest.mark.parametrize(
    'rows, cols, expected',
    [
        [
            [[2, 2], [4], [1, 1, 1], [2], [1, 1, 1], [3, 1]],
            [[1, 1, 2], [1, 1], [1, 1], [4], [2, 1], [3, 2]],
            [
                [1, 1, 0, 0, 1, 1],
                [0, 0, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
                [1, 0, 0, 1, 0, 1],
                [1, 1, 1, 0, 0, 1],
            ],
        ],
        [
            [[1], [2]],
            [[2], [1]],
            [
                [1, 0],
                [1, 1],
            ],
        ],
        [
            [[3], [2], [1, 1], [2], [3], [1, 1]],
            [[1, 1, 2], [1, 2], [6], [1]],
            [
                [1, 1, 1, 0],
                [0, 0, 1, 1],
                [1, 0, 1, 0],
                [0, 1, 1, 0],
                [1, 1, 1, 0],
                [1, 0, 1, 0],
            ],
        ],
    ],
)
def test_solve_nonogram(rows, cols, expected):
    assert solve(verticals=cols, horizontals=rows) == expected
