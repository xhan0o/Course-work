from pprint import pprint
def ipport(data):
    x=data.rfind(".")
    ip= data[:x]
    port= data[x+1:]
    return ip,port

def portscan(lines):
    countsrc=0
    countdst=0
    repeatcount=0
    repeatdcount=0
    KamKeLines=[]
    IPTables={}
    source_dict={}
    dest_dict={}
    dst_port={}
    port_dict={}
    portd_dict={}
    IPlist=[]
    for lines in lines:
        if len(lines)>3:
            if lines[1]=="IP":
                KamKeLines.append(lines)
    print str(len(KamKeLines))+" ip lines"
    for lines in KamKeLines:
        if len(lines[2].split("."))>=5:
            srcip,srcport=ipport(lines[2])
            if srcip in source_dict:  #same word,+1 to that occurance
                source_dict[srcip].append(srcport)
                repeatcount=repeatcount+1
            else:                   #new word add that word to dictionary and make occurance 1
                source_dict[srcip] = [srcport]
                # if srcport is not well known
                # attack_time[srcip] = time

        else:
            countsrc=countsrc+1
            #print lines[2]+" source"
        if len(lines[4].split("."))>=5:
            dstip,dstport=ipport(lines[4])
            if dstip in dest_dict:  #same word,+1 to that occurance
                dest_dict[dstip].append(dstport)
                repeatdcount=repeatdcount+1
            else:                   #new word add that word to dictionary and make occurance 1
                dest_dict[dstip] = [dstport]
        else:
            countdst=countdst+1
            #print lines[4]+ " Desti"
    #print srcip
    #print countsrc
    #print countdst
    print "IPs "+ str(source_dict.keys())
    print "xxxxxxxxxxx--Source--xxxxxxxxxxxxx"
    for key in source_dict:
        port_dict[key]=set(source_dict[key])
        numports = len(source_dict[key])
        IPTables[key] = {'numports': numports}
        print key +" ports: "+ str(numports)
    for key in port_dict:
        uniqueports=len(port_dict[key])
        IPTables[key]['uniqueports'] = uniqueports
        print key + " unique ports " + str(uniqueports)
    #print repeatcount
    print "IPs " + str(dest_dict.keys())
    print "xxxxxxxxxxx--Destination--xxxxxxxxxxxxx"
    for key in dest_dict:
        portd_dict[key]=set(dest_dict[key])
        numdports = len(dest_dict[key])
        print key +" d ports: "+ str(numdports)
    for key in dest_dict:
        uniquedports=len(portd_dict[key])
        print key + " unique d ports " + str(uniquedports)
    #print repeatdcount
    #print "Source ports----------------"
    #pprint (port_dict)
    #pprint (IPTables)
    for key,value in IPTables.items():
        value['Ratio']=float(value['uniqueports'])/float(value['numports'])
        #print value['Ratio']
        if value['Ratio']<=0.03:
            #print value['Ratio']
            IPlist.append(key)


    #pprint (IPTables)
    #print "Dest ports------------------"
    pprint (portd_dict)
    #pprint (IPTables)
    return IPlist

import glob
filestack=[]
for filename in glob.glob('*.log'):
    filestack.append(filename)


for files in filestack:
    fileread=open(files,'r+')
    print files + "-->"
    lineread=[]
    del lineread[:]
    for lines in fileread.readlines():
        words=lines.split()
        lineread.append(words)
    #print str(len(lineread)) + " Total lines"
    Table= portscan(lineread)
    print "attack is done by IPS    " + str(Table)
