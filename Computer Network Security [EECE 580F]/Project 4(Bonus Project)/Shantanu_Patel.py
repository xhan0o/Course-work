##############################################
#Author: Shantanu Patel
#Submission of Computer Network Security Project3
##############################################

attackertable=[]
def checkreq(wrds):
    #print wrds[2]
    if len(wrds)>3:
        if len(wrds[2].split("."))>=5:
            srcip,srcport=ipport(wrds[2])
            dstip,dstport=ipport(wrds[4])
            if dstport == "smux:" or dstport == "rtsp:" or dstport == "mysql:" or dstport == "pop3s:" or dstport == "sunrpc:"  :
                #print srcip + " is attacking"
                attackerinfo=[ wrds[0] , srcip ]
                return wrds[0] , srcip
    return None , None

def findattacker(info):
    for data in info:
        print data[0]
    return
def ipport(data):
    x=data.rfind(".")
    ip= data[:x]
    port= data[x+1:]
    return ip,port

import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("--online",action='store_true')
args = parser.parse_args()
print args
alldata=[]
ipdict={}
portdct={}
if args.online:
    ################################################################################
    #                            ONLINE PROGRAM Starts here                          #
    ################################################################################
    for line in sys.stdin:
        wrds=line.split()
        #print len(wrds)
        time , ipatk = checkreq(wrds)
        l = wrds
        if time is None:
            continue
        if ipatk in ipdict:  #same word,+1 to that occurance
            ipdict[ipatk]['count'] +=  1
        else:                   #new word add that word to dictionary and make occurance 1
            ipdict[ipatk] = {'count' : 1}
        for key in ipdict:
            if ipdict[key]['count']>=5:
                print wrds[0]+"\t" + str(key) + " is attacking"
                if ipdict[key]['count'] >=8:
                    ipdict[key]['count']=0
else:
    from pprint import pprint

    #function of extracting IP and Ports from data
    def ipport(data):
        x=data.rfind(".") #finding first '.' fron right
        ip= data[:x] #anything before x is IP
        port= data[x+1:] #anything after x is .port (x+1) is removing '.'
        return ip,port

    #PortScan will process the linereads and will return a table which has possible lines of start of attack
    def portscan(lines):
        KamKeLines=[]
        KamKaTable=[]
        portdct={}
        f= 0
        scan=[]
        for lines in lines:
            if len(lines)>3:
                if lines[1]=="IP": #reading IP packets only
                    KamKeLines.append(lines) #making dictionary of useful lines wich includes port reading lines
        #print str(len(KamKeLines))+" ip lines"
        for lines in KamKeLines:  #readin those lines and making sense of source-Destinatination Ip and ports

        # packer--> Time x Sourcedata > DestData x x x ...
            if len(lines[2].split("."))>=5:
                srcip,srcport=ipport(lines[2]) #extracting IP and port from lines
                dstip,dstport=ipport(lines[4]) #extracting Ip from destination data
                #print dstport
                #if destination port is one of this , which are non usual while surfing normal internet. there is possibility of attack.
                if dstport == "smux:" or dstport == "rtsp:" or dstport == "mysql:" or dstport == "pop3s:" or dstport == "sunrpc:"  :
                    KamKaTable.append(lines) #create another dictionary of more filtered data
                if dstport in portdct:
                    portdct[dstport]['count']+=1
                else:
                    portdct[dstport]={'count':1}
        #print len(portdct)
        if len(portdct)>=1100:
            scan=[1 , 0 , 0 , 0]
        elif len(portdct)>800 and len(portdct)<1100:
            #print "SS scan"
            scan=[0 , 1 , 0 , 0]
        elif len(portdct)<50:
            #print "SN scan"
            scan=[0 , 0 , 1 , 0]
        elif len(portdct)>100 and len(portdct)<500:
            #print "Fscan"
            scan=[0 , 0 , 0 , 1]
        #for key in portdct:
            #if portdct[key]['count']<=1:
                #print key
            #    a=1
                    #print lines
        #print len(KamKaTable)
        return KamKaTable,scan

    #Find attacker from filtered data points, To detect attacks from multiple IPs. This will be major detection point
    #This function processes the filtered data and counts how many port requests has been done by specific IP
    #If there are multiple attacks by multiple IP, here it will return dictionary of multiple IPs and count of number of time port request has been done
    def findattacker(table):
        attacker={}
        counttable=[]
        for lines in table: #reading filtered data
            srcip,srcport=ipport(lines[2]) #reading source IP
            if srcip in attacker: #If source IP is in list , increase the count of requesting for malicious port
                attacker[srcip]['count']+=1
            else: # Add source IP to the list and initial count of port scanned as 1
                attacker[srcip]={'count':1}

        #print attacker
        return attacker #return the list of possible attacker IP and number of times IP tried requesting those unusual ports

    #We are collecting possible attacker IPs from last list with counts of port scanning
    #There might be possible other IPs might have tried requesting port
    #To filter realattacker this funtion will check the counts, and if port scanning is more than 3 for those unusual ports we can do
    def IsRealAttacker(table):
        PossibleAttacker=[]
        for key in table:
            if(table[key]['count'] > 3): #if port requests are more than 3 there's a good possibility of attacekr IP
                PossibleAttacker.append (key)
        #    for k,v in value:
        #        if v>=5:
        #            print key,value
        return PossibleAttacker

    #Normal time difference function
    import datetime
    def timedifference(a,b): #function to find time difference
        timediff=datetime.datetime.strptime(b,"%H:%M:%S.%f")-datetime.datetime.strptime(a,"%H:%M:%S.%f") # Keep format in mind, I have taken %H:%M:%S:%f but sample log is %H:%M:%S.%f
        return timediff


    #Funtion will process the attackers Ip and Main useful table1.
    #it will detect the time differece between requests and Try to identify multiple attacks from same IP
    #later on After defining type of attacks, we can use them to detect multiple attacks from same IP.
    #due to some constrains I wasnt able to implement that, so time is simple patch for detection if attack is timed.
    def Findattacktime(RealAttacker,KamKaTable):
        time=[]
        attacktime=[]
        #print RealAttacker
        for word in KamKaTable: #Reading previous data table of useful data and finding atttacker Ip in that
            srcip,srcport=ipport(word[2])
            if srcip == RealAttacker:
                dstip,dstport=ipport(word[4])
                if dstport=="smux:": #Matching malicious ports here
                    time.append(word[0])

                    #print word[0]
        i=0
        x=time[0].rfind(".") #Removing micro seconds
        z= time[0][:x]
        attacktime.append(z) #After matching ports, Add that to dictionary
        #For multiple attacks from same IP, checking by time difference
        while i< len(time)-1:
            x = timedifference(time[i],time[i+1])
            if x.total_seconds() >=120: #if time differecnce is more than 2 minutes considering it as another attack
                x=time[i+1].rfind(".") #removing microseconds from time
                z= time[i+1][:x]

                attacktime.append(z) #adding 2nd time of attack of same IP
            i=i+1
        return attacktime


    ################################################################################
    #                            MAIN PROGRAM Starts here                          #
    ################################################################################
    import glob
    #reading all files in current dictionary and adding *.log files to filestack
    filestack=[]
    for filename in glob.glob('*.log'):
        filestack.append(filename)

    #reading files one by one from file stack
    for files in filestack:
        fileread=open(files,'r+') #printing file name and -->
        print files + "-->"
        lineread=[]
        Oscan=0
        scan=[]
        del lineread[:]  # declaring and clearing dictionary
        for lines in fileread.readlines():
            words=lines.split()
            lineread.append(words) #dumping log file data to dictionary
            #print words
            if len(words)>5:
                if words[5] == "ICMP":
                    Oscan=Oscan+1
            else:
                continue
        #print Oscan
        #print str(len(lineread)) + " Total lines"
        Table,scan= portscan(lineread)  #Port scanning for analysis
        #pprint (Table)
        AttackerIP=findattacker(Table) #Find attacker from filtered data points
        RealAttacker=IsRealAttacker(AttackerIP) #Find Real Attacker from possible attacker list
        #print RealAttacker
        #From attacker finding time of attack
        #Multiple attacks from 1 IP and attacks with multiple IPs
        for attacker in RealAttacker: #loop for attack from multiple IPs
            attacktime=Findattacktime(attacker,Table) #Finding possible time of attack/s
            print "\t",  attacker, "attacked at ", attacktime #printing results
        if Oscan>=10:
            print "\tO scan"
        elif scan[0]==1:
            print "\tSS or SV Scan"
        elif scan[1]==1:
            print "\tSS or SV Scan"
        elif scan[2]==1:
            print "\tSN Scan"
        elif scan[3]==1:
            print "\tF Scan"
