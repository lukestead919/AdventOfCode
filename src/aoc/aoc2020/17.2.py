import numpy as np
import itertools
np.set_printoptions(threshold=np.inf)


def doGeneration():
    global arr
    nextGen = np.array(arr)
    for i, j, k, l in itertools.product(range(25), range(25), range(25), range(25)):
        value = arr[i, j, k, l]
        neighbours = np.sum(arr[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2]) - value
        # print(value, neighbours)
        if value == 1 and not (neighbours == 2 or neighbours == 3):
            nextGen[i, j, k, l] = 0
            # print(i, j, k, " 1 > 0 ", neighbours, "\n", arr[i-1:i+2, j-1:j+2, k-1:k+2])
        elif value == 0 and neighbours == 3:
            nextGen[i, j, k, l] = 1
            # print(i, j, k, " 0 > 1 ", neighbours, "\n", arr[i-1:i+2, j-1:j+2, k-1:k+2])

    arr = nextGen


with open("DataFiles/17.txt") as f:
    initialState = f.read().replace("#", "1").replace(".", "0").splitlines()
    # print(initialState)
    initialState = [[x for x in a] for a in initialState]
    # print(initialState)


arr = np.zeros((25, 25, 25, 25))

arr[8:8+len(initialState), 8:8+len(initialState), 13, 13] = initialState

# print(arr[7:17, 7:17, 12:15])

for i in range(6):
    doGeneration()

print(np.sum(arr))
