import numpy as np
from utils import read_data_file_as_lines


def iterate_right(array: np.ndarray):
    _, n = array.shape
    new_array = np.array(array)
    rights = np.argwhere(array == ">")
    for i, j in rights:
        jr = (j+1) % n
        if array[i, jr] == '.':
            new_array[i, j] = '.'
            new_array[i, jr] = '>'
    return new_array


def iterate_down(array: np.ndarray):
    m, _ = array.shape
    new_array = np.array(array)
    downs = np.argwhere(array == "v")
    for i, j in downs:
        id = (i+1) % m
        if array[id, j] == '.':
            new_array[i, j] = '.'
            new_array[id, j] = 'v'
    return new_array


def iterate(array: np.ndarray):
    array = iterate_right(array)
    array = iterate_down(array)
    return array


def main():
    data = read_data_file_as_lines(25)
    data = [[a for a in line] for line in data]
    array = np.array(data)
    last_array = np.array([])
    i=0
    print(array)
    while not np.array_equal(array, last_array):
        i += 1
        last_array = array
        array = iterate(array)
        if i in [1, 2, 3, 4, 5, 10]:
            print(i)
            print(array)
    print(i)

main()