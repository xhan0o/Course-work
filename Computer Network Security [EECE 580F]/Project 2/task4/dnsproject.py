import datetime
from pprint import pprint
def timedifference(a,b):
    timediff=datetime.datetime.strptime(b,"%H:%M:%S:%f")-datetime.datetime.strptime(a,"%H:%M:%S:%f")
    return timediff


lines=[]
unique=[]
file=open("Test_dnslog_with_blocking.txt","r+")
for line in file.readlines():
    #print line
    words = line.split()
    if  words[9] != 'AAAA':
        #print words
        lines.append(words)
#pprint (lines)
j=0
i = 0
while i < len(lines)-1:
    x = timedifference(lines[i][1],lines[i+1][1])
    if x.total_seconds()>150:
        print x
        print lines[i+1]
        unique.append(lines[j:i+1])
        j=i
    i+=1
unique.append(lines[j+1:])
#pprint (unique)
print (unique[0][0])
#print unique[4]

file=open("Test_report_with_blocking.txt","w")
for i in range(0,len(unique)):
    file.write(unique[i][0][7]+ ":"+str (len(unique[i])) + "    Time:" + unique[i][0][0]+ "  "+ unique[i][0][1] + "\n")
    for j in range(0,len(unique[i])):
        file.write(str(j+1) + ". " + unique[i][j][7] + "\n")
file.close()
#print timedifference(a,b)
