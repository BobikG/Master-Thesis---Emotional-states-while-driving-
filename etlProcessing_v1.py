fileWrite = open("putDataInsideTable.sql", "w")
print("Start")
n=0

with open("./N_MV_20220505.txt") as f:
    for line in f: # read file line by line
        fileWrite.write("INSERT INTO `ShortRangeRadar`(`TIMED`,`INDEXD`,`HeartRate`,`HR_Quality`,`RespirationRate`,`RR_Quality`,`IE`,`RAbin`,`STATED`) VALUES('")
        check = line.find(",")
        fileWrite.write(line[0:check])
        fileWrite.write("'")
        fileWrite.write(line[check:-2])
        fileWrite.write(");")
        fileWrite.write("\n")
        #print(line[23:-2])
        #print(line[:-2])
        n=n+1

print(n)
fileWrite.close()
