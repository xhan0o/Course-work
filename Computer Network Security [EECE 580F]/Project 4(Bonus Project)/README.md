README

Scanproject.py has two type on inputs.
1) System in (pipe)
2) Normal (based on project 3)

Usage example:
>> cat tcp_ss.log | py scanproject.py --online

arg = online for using pipe input
Returns one or more lines when finds attack
If attack is longer , it keeps printing attack running.
**WORKS FOR ATTACKED BY MULTIPLE IPs**

Normal run:
>> py scanproject.py

Scans whole dictionary and reads all files and do as per project 3.



Change log:
Features added to Project3>
1) type of scan : O , F, sN , sS or sV
2) Real time scanning with pipe and argument of --online
3) more robust and reliable

features of --online usage:
1) Reads real-time and analyse
2) Returns attack when detected
3) CAN DIFFERENCEATE MULTIPLE ATTACKS DONE BY MULTIPLE IP

Bugs:
1) doesnt predict ss and sv scan different
2) Doesnt support for close multiple attack from same IP
3) --online prints more than once per one attack
