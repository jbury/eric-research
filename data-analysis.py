import sys
import csv
import math

print ("the number of arguments: ", len(sys.argv))
print ("The arguments are: ", str(sys.argv))

Default = 'C:\\\\Users\\\\Eric\\\\Desktop\\\\eric-research\\\\30sec.csv'

videoLengthSeconds = int(input("Enter the length of the video in seconds: "))
if(len(sys.argv) == 2):
#if(len(sys.argv)!=2):
    print ("Error: No .csv file provided")
    input()
    sys.exit()
#with open(sys.argv[1], 'r') as f:
#Get the number of lines in the file
fileSize = sum(1 for line in open(Default, 'r'))

with open(Default, 'r') as f:
    myReader = csv.reader(f, dialect='excel')

    frameCount = fileSize - 1

    stepSize = int(math.floor(frameCount / videoLengthSeconds))
    print('Step size is: ', stepSize)
    steps = []

    for row in myReader:
        if((int(row[0])-1) % stepSize == 0):
            print(int(row[0]))
            steps.append((float(row[1]), float(row[2])))

    print(len(steps))
    print(steps[0])



x = input("YAY")



def cosineRule(leg1, leg2, hypot):
    return math.acos((leg1**2 + leg2**2 - hypot**2)/(2*leg1*leg2))
