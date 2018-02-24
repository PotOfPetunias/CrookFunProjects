import sys
from datetime import datetime

def record(fileName, activity, hours):
    timeFile = open(fileName, "a")
    d = str(datetime.date(datetime.now()))
    t = str(datetime.time(datetime.now()))
    timeFile.write(activity + "," + str(hours) + "," + d + "," + t + "\n")
    timeFile.close()

fileName = "practice.csv"
record(fileName, "skateboard", 1)
record(fileName, "skateboard", 1)
print(sys.argv)
