##############################################
#Author: Shantanu Patel
#Submission of Computer Network Security Project2, Undergrad task
##############################################


import datetime
from pprint import pprint
def timedifference(a,b): #function to find time difference
    timediff=datetime.datetime.strptime(b,"%H:%M:%S:%f")-datetime.datetime.strptime(a,"%H:%M:%S:%f") # Keep format in mind, I have taken %H:%M:%S:%f but sample log is %H:%M:%S.%f
    return timediff


lines=[]
unique=[]
file=open("dnslog.txt","r+")
for line in file.readlines():
    #print line
    words = line.split()
    if  words[9] != 'AAAA': #removing AAAA entries
        #print words
        lines.append(words)

#Loop to calculate time difference and adding it in last column
i=0
j=0
while i < len(lines)-1:
    x = timedifference(lines[i][1],lines[i+1][1])
    lines[i].append(x.total_seconds())
    #print lines[i][10]
    i+=1
#Partitioning , If TimeDifference >10 and partition has atleast 5 entries
#Assuming One site has atleast 5 DNS for avoiding false detection
i=0
while i < len(lines)-6:
    z=max([lines[i+1][10],lines[i+2][10],lines[i+3][10],lines[i+4][10],lines[i+5][10]])
    print lines[i][10]
    #print z
    if lines[i][10]>10 and z<10:
        print lines[i][10]
        unique.append(lines[j:i+1])
        print lines[i+1]
        #print lines[i+2]
        #print lines[i+5]
        print "xxxx"
        j=i
    i+=1
unique.append(lines[j+1:])

#writing report file
file=open("report.txt","w")
for i in range(0,len(unique)):
    file.write(unique[i][1][7]+ ":"+str (len(unique[i])) + "    Time:" + unique[i][1][0]+ "  "+ unique[i][1][1] + "\n")
    for j in range(0,len(unique[i])):
        file.write(str(j+1) + ". " + unique[i][j][7] + "\n")
file.close()
