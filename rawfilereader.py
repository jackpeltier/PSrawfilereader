import sys

filename = sys.argv
size = 4

with open(filename[1], "rb") as file:
    while True:
        chunk = file.read(size)
        if not chunk:
            break
        if chunk[3] == 0b11111111 and chunk[2] == 0b11111111:
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~Event header~~~~~~~~~~~~~~~~~~~~~~~~")
        if chunk[3] == 0b10100000:
            print("---------------------------Hybrid---------------------------")
        if chunk[3] == 0b01010000:
            print("----------------------------Stub----------------------------")
        print("Binary:", end=' ')
        print(format(chunk[3], '08b'), end=' ')
        print(format(chunk[2], '08b'), end=' ')
        print(format(chunk[1], '08b'), end=' ')
        print(format(chunk[0], '08b'), end=" Hex: ")
        print(format(chunk[3], '02x'), end=' ')
        print(format(chunk[2], '02x'), end=' ')
        print(format(chunk[1], '02x'), end=' ')
        print(format(chunk[0], '02x'))


