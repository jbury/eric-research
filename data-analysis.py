import sys
import csv
import math

#TODO delete
print ("the number of arguments: ", len(sys.argv))
print ("The arguments are: ", str(sys.argv))

videoLengthSeconds = int(input("Enter the length of the video in seconds: "))
if(len(sys.argv) < 2):
#if(len(sys.argv)!=2):
    print ("Error: No .csv file provided.  Exiting.")
    print ("Seriously, just drag your .csv file over this script.  EZ PZ")
    input()
    sys.exit()

file = sys.argv[1]
#with open(sys.argv[1], 'r') as f:
#Get the number of lines in the file
fileSize = sum(1 for line in open(file, 'r'))

with open(file, 'r') as f:
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
    #Do I need all these ()'s?  Probably not, but they're here anyway.
    return math.acos(((leg1**2) + (leg2**2) - (hypot**2))/(2*leg1*leg2))

#Two tuples go in, the distance between them comes out-You can't explain that!
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
