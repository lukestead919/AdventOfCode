from utils import read_data_file_as_lines
import numpy as np


def apply(image: np.ndarray, filter: list):
    image = np.pad(image, 1, mode='edge')
    m, n = image.shape
    new_image = np.zeros_like(image)

    for x in range(1, m-1):
        for y in range(1, n-1):
            input = image[x-1: x+2, y-1: y+2].flatten().tolist()
            binary_input = ''.join([str(i) for i in input])
            decimal_input = int(binary_input, 2)
            new_image[x, y] = filter[decimal_input]

    # replace edge that didn't get mapped
    return np.pad(new_image[1:-1, 1:-1], 1, mode='edge')


def apply_times(image, filter, times):
    for _ in range(times):
        image = apply(image, filter)
    return image


def main():
    data = read_data_file_as_lines(20)
    filter = [1 if d == '#' else 0 for d in data[0]]
    image = [[1 if d == '#' else 0 for d in line] for line in data[2:]]
    image = np.array(image)
    image = np.pad(image, 5)
    image = apply_times(image, filter, 2)
    print("part 1", np.sum(image))
    image = apply_times(image, filter, 48)
    print("part 2", np.sum(image))


main()
