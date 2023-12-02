input = open("01/input.txt", "r").read().split("\n")

# Problem 02
numbers = {"one": 1,"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
def getNumber(line, first):
    line = line if first else line[::-1]
    for (idx, char) in enumerate(line):
        if char.isdigit(): return char
        for (key, value) in numbers.items():
            searchIdx = line.find(key if first else key[::-1])
            if searchIdx == idx: return value
print("Problem 02: " + str(sum(map(int, [str(getNumber(line, True)) + str(getNumber(line, False)) for line in input]))))