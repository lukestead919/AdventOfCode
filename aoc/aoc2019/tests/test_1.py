import pytest
from aoc.aoc2019.solutions import problem1


@pytest.mark.parametrize("mass, fuel", [
    (0, 0),
    (-1, 0),
    (3, 0),
    (8, 0),
    (9, 1),
    (300, 98),
    (301, 98),
    (302, 98),
    (303, 99)
])
def test_fuel_needed_for_mass(mass, fuel):
    assert problem1.fuel_needed_for_mass(mass, False) == fuel


@pytest.mark.parametrize("mass, fuel", [
    (0, 0),
    (-1, 0),
    (3, 0),
    (8, 0),
    (9, 1),
    (101, 39),
    (102, 40),
    (113, 45),
    (114, 47),
    (100756, 50346),
    (1969, 966)
])
def test_fuel_needed_for_mass_recursive(mass, fuel):
    assert problem1.fuel_needed_for_mass(mass, True) == fuel


def test_example_1():
    example = "12\n14\n1969\n100756"

    assert problem1.get_total_fuel_needed(example, False) == 34241


def test_example_2():
    example = "12\n14\n1969\n100756"

    assert problem1.get_total_fuel_needed(example, True) == 50346+966+2+2
