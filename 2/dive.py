import sys
import os

MIN_VERSION=(3,10)
if sys.version_info < MIN_VERSION:
    print("At least %s.%s version of Python is required to run this file" % MIN_VERSION)
    sys.exit(1)

def getFileLines(filePath):
    with open(filePath) as f:
        return f.readlines()

def parseInstructions(fileLines):
    horizontal = 0
    depth = 0
    for line in fileLines:
        instruction = line.split()
        match instruction[0]:
            case "forward":
                horizontal = horizontal + int(instruction[1])
            case "up":
                depth = depth - int(instruction[1])
            case "down":
                depth = depth + int(instruction[1])
    return horizontal * depth

def parseAimInstructions(fileLines):
    aim = 0
    depth = 0
    horizontal = 0
    for line in fileLines:
        instruction = line.split()
        match instruction[0]:
            case "forward":
                horizontal = horizontal + int(instruction[1])
                depth = depth + (aim * int(instruction[1]))
            case "up":
                aim = aim - int(instruction[1])
            case "down":
                aim = aim + int(instruction[1])
    return horizontal * depth


def main():
    if len(sys.argv) <= 1:
        print("Please specify the file to read instrcutions from")
        return 0
    elif not os.path.isfile(sys.argv[1]):
        print ("File path provided is not a file or does not exist")
        return 1
    else:
        instructions = getFileLines(sys.argv[1])
        print("First Answer:", parseInstructions(instructions))
        print ("Second Answer:", parseAimInstructions(instructions))
    return 0

if __name__ == '__main__':
    sys.exit(main())