import pytest

from aoc.aoc2019.solutions import problem1

print(problem1.fuel_needed_for_mass(10))


@pytest.mark.parametrize("mass, fuel", [
    (0, -2),
    (-1, -3),
    (3, -1),
    (300, 98),
    (301, 98),
    (302, 98),
    (303, 99)
])
def test_fuel_needed_for_mass(mass, fuel):
    assert problem1.fuel_needed_for_mass(mass) == fuel
