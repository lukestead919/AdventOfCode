import pytest
from src.aoc.aoc2019.solutions import problem2

@pytest.mark.parametrize("input, output", [
    ([1,0,0,0,99], [2,0,0,0,99]),
    ([2,3,0,3,99], [2,3,0,6,99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])
])
def test_final_state_for_examples(input, output):
    assert problem2.run_program(input) == output


@pytest.mark.parametrize("input, output", [
    ("1,0,0,0,9", [1, 0, 0, 0, 9]),
    ("2", [2])
])
def test_to_list(input, output):
    assert problem2.toList(input) == output

