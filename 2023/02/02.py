from math import prod
input = open("02/input.txt", "r").read().split("\n")

# Problem 01
max = {"red": 12, "green": 13, "blue": 14}
def checkLine01(line):
    for pulls in [pull.split(", ") for pull in [data.strip() for data in line[line.find(":") + 1:].split(";")]]:
        values = {}
        for pull in pulls:
            firstSpace = pull.find(" ")
            values[pull[firstSpace + 1:]] = pull[0:firstSpace]
        for key, value in values.items():
            if int(value) > max[key]: return 0
    return int(line[line.find(" ") + 1:line.find(":")])
print("Problem 01: " + str(sum([checkLine01(line) for line in input])))

# Problem 02
def checkLine01(line):
    maxValues = {"red": 0, "green": 0, "blue": 0}
    for pulls in [pull.split(", ") for pull in [data.strip() for data in line[line.find(":") + 1:].split(";")]]:
        for pull in pulls:
            firstSpace = pull.find(" ")
            value = int(pull[0:firstSpace])
            color = pull[firstSpace + 1:]
            if value > maxValues[color]: maxValues[color] = value
    return prod(maxValues.values())
print("Problem 02: " + str(sum([checkLine01(line) for line in input])))