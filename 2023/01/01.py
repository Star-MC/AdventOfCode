input = open("01/input.txt", "r").read().split("\n")
numbers = {"one": 1,"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def getNumber(line):
    for (idx, char) in enumerate(line):
        if char.isdigit(): return char
        for (key, value) in numbers.items():
            searchIdx = line.find(key)
            searchIdx = searchIdx if searchIdx != -1 else line.find(key[::-1])
            if searchIdx == idx: return value

output = [str(getNumber(line)) + str(getNumber(line[::-1])) for line in input]
print(sum(map(int, output)))