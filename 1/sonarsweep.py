import sys
import os

def readDepths(filePath):
    with open(filePath) as f:
        depths = f.readlines()
    return depths

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

def main() -> int:
    #Check Args
    if len(sys.argv) == 1:
        print("Please specify the path for the file of depths")
        return 0
    elif not os.path.isfile(sys.argv[1]):
        print ("File path provided is not a file or does not exist")
        return 1
    else:
        depthReadings = readDepths(sys.argv[1])

    #Process Depth Readings
    processDepthReadings(depthReadings)

    #Return OK to Sys.Exit
    return 0

if __name__ == '__main__':
    sys.exit(main())