import sys
import os

def readDepths(filePath):
    with open(filePath) as f:
        depths = f.readlines()
    return depths

#Process Individual depths
def processDepthReadings(depthReadings):
    previousDepth = -1
    depthIncreases = 0

    for depth in depthReadings:
        depth = int(depth)
        if previousDepth == -1 :
            previousDepth = depth
        elif previousDepth < depth :
            previousDepth = depth
            depthIncreases += 1
        else:
            previousDepth = depth
    
    print(depthIncreases)

#Process Sum of Readings
def processDepthReadingsSum(depthReadings):
    previousSum = -1
    sumIncreases = 0

    for i in range(len(depthReadings)):
        if i < len(depthReadings) - 2:
            sum = int(depthReadings[i]) + int(depthReadings[i+1]) + int(depthReadings[i+2])
            if sum > previousSum and previousSum != -1:
                sumIncreases += 1
            previousSum = sum
        else:
            break
    
    print(sumIncreases)

def main() -> int:
    #Check Args
    if len(sys.argv) <= 1:
        print("Please specify the path for the file of depths and optionally set the second argument to 1 to process a moving sum of the next 3 depth readings")
        return 0
    elif not os.path.isfile(sys.argv[1]):
        print ("File path provided is not a file or does not exist")
        return 1
    else:
        depthReadings = readDepths(sys.argv[1])

    #Process Depth Readings
    if  len(sys.argv) > 2 and int(sys.argv[2]) == 1:
        print("hi")
        processDepthReadingsSum(depthReadings)
    else:
        processDepthReadings(depthReadings)

    #Return OK to Sys.Exit
    return 0

if __name__ == '__main__':
    sys.exit(main())