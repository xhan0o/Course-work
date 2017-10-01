Project 3 - Detection of NMAP attacks
################################################################################
Input: ./*.log
all log files from current dictionary
Output: filename1.log-->
          Attacker1 attacked at  ['time 1','time 2']
          Attacker2 attacked at  ['time 1']
################################################################################
analysys.py is for making snense of data and analysing packets, it returns the IPs and unique IPs. Approach of it will be used for bonus tasks.



Brief: Tried analyse data from.
Code is devided into 2 parts.
Part 1: finding attacker
part 2: Finding timing of multiple / single attacks by single / multiple attackers

Once making sense try to filtering out possible attacks and shifting them into
one and more tables. filtering process counts the ports accessed and number of time accessed.
With those filtered tables which returns possible attackers.
After getting attackers, we try matching port requests to find out the time of attack.

Program:
1) Read log file
2) Transfering data to list
3) Making table of useful packets
4) count packets which scanned specific ports
5) Keep count of number of times scanned and IPs which scanned specific ports
6) If count of port scan is > 3 , IsAttacker, return attacker list
7) From attacker list finding times of attack.
8) From attacker list , matching attacker and packet where it requested for soem specific ports
9) Return the time.
10) For multiple attacks from same time, used time difference.(It's just patch here, we can do by finding type of scan and using it here)



There is another file analysis.py , which I will be using for bonus tasks. It returns the port and unique ports with counts of them in each attack.
