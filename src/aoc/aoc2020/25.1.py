from utils import read_file_as_lines

input = [int(i) for i in read_file_as_lines("DataFiles/25.txt")]

subjectNumber = 7
mod = 20201227
i=1
loop = 0
loopSize = [0, 0]

# I don't actually need both loop sizes
while loopSize[0] != 0 or loopSize[1] == 0:
    loop += 1
    i = subjectNumber*i % mod
    try:
        loopSize[input.index(i)] = loop
        print(loopSize, loop, i)
        break
    except:
        if loop < 50:
            print(loop, i)

# Now work out the encrypted key using the loopSize we just found out, and the publicKey of the other component
if (loopSize[0] != 0):
    loopSize = loopSize[0]
    publicKey = input[1]
else:
    loopSize = loopSize[1]
    publicKey = input[0]

print(loopSize, publicKey)
encryptedKey=1
for i in range(loopSize):
    encryptedKey = encryptedKey*publicKey % mod

print("encrypted key is " + str(encryptedKey))
