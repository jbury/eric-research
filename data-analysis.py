import sys
import csv
import math
import traceback

def main():
    try:
        videoLengthSeconds = int(input("Enter the length of the video in seconds: "))
        stopThreshhold = int(input("Enter the stopping threshhold in mm/min: "))

        if(len(sys.argv) != 2):
            print ("Error: No .csv file provided.  Exiting.")
            print ("Seriously, just drag your .csv file over this script.  EZ PZ")
            input()
            sys.exit()
        file = sys.argv[1]

        #Get the number of lines in the file
        fileSize = sum(1 for line in open(file, 'r'))

        with open(file, 'r') as f:
            myReader = csv.reader(f, dialect='excel')

            frameCount = fileSize - 1

            stepSize = int(math.floor(frameCount / videoLengthSeconds))
            print('Step size is: ', stepSize)
            steps = []

            #Get the sample steps
            for row in myReader:
                if((int(row[0])-1) % stepSize == 0):
                    steps.append((float(row[1]), float(row[2])))

            #Find the distance between each consecutive step
            distA = []
            for i in range (0, len(steps)-1):
                distA.append(distance(steps[i], steps[i+1]))

            #Find the distance between each two steps
            distB = []
            for i in range (0, len(steps)-2):
                distB.append(distance(steps[i], steps[i+2]))

            #Find the average turning angle
            count = 0
            total = 0
            for i in range (0, len(distB)):
                count += 1
                total += cosineRule(distA[i], distB[i], distA[i+1])

            averageTurnAngle = total/count

            print('The average turning angle was ', averageTurnAngle, ' units?')

            #Find the number of times the larva stops
            count = 0
            for i in range (0, len(distA)):
                  if (conversion(distA[i]) < stopThreshhold):
                      count+=1

            print('The larva stopped ', count, ' times.')

    except:
        traceback.print_exc()

    input("Press enter to close")

def cosineRule(leg1, leg2, hypot):
    return math.acos(((leg1**2) + (leg2**2) - (hypot**2))/(2*leg1*leg2))

#Two tuples go in, the distance between them comes out-You can't explain that!
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def conversion(dist):
    return (dist * 60/12.2)

main()
