from aoc.aoc2019.solutions import problem3


def test_examples_1():
    path1 = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
    path2 = ["U62","R66","U55","R34","D71","R55","D58","R83"]
    assert problem3.get_closest_cross_to_origin(path1, path2) == 159

    path1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
    path2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
    assert problem3.get_closest_cross_to_origin(path1, path2) == 135


def test_examples_2():
    path1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
    path2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
    assert problem3.get_earliest_cross(path1, path2) == 610

    path1 = ["R98", "U47", "R26", "D63", "R33",
             "U87", "L62", "D20", "R33", "U53", "R51"]
    path2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
    assert problem3.get_earliest_cross(path1, path2) == 410
