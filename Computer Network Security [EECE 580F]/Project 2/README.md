##############################################
#Author: Shantanu Patel
#Submission of Computer Network Security Project2, Undergrad task
##############################################

------------------------------------------
dnsproject.py
------------------------------------------
--> Tried finding close gaps(15 seconds), It worked but was not that robust.
--> Added another condition , that one partition should have atlease 5 dns calls
__________________________________________________________
Opens website 1 >>  5-7 dns entries very close
(wait of long time)
--some other entries with little discreet time
(wait of long time)
Opens website 2 >>  5-7 dns entries very close
(after 30 seconds only)
Opens website 3 >>  5-7 dns entries very close
__________________________________________________________
by detecting time gaps along with condition of partition length, we can determine websites
***For any changes made in any programs find "change" , all comments has the keyword change in each edits.***
------------------------------------------
Task 2
------------------------------------------
--->Added domain names to domains.cfg.
--->Checked and tested initially by adding 'google.com 192.168.127.127' to domains.cfg and running nslookup
_______________________________________________________

xhan0o:~/dns2proxy# nslookup mail.google.com
Server: 192.168.127.127
Address: 192.168.127.127
_______________________________________________________
---> After that, tried opening websites and blocking certain portions and frames, It worked.

-------------------------------------------
Task 3
-------------------------------------------
--->Found the functions which uses the domains.cfg && prints returned values
--->Edited std_A_qry function and whichever modules uses domains and spoof gets True flag for blocking and other returns False
---> if value in A_qry came from any function uses domains or spoof 'Blocking=True' else 'False'
---> While printing
If blocking != True => print

-------------------------------------------
Task 4
-------------------------------------------
--->5 websites are attached, For simplicity and ease reports were generated with bit different dnsproject.py
--->Websites:
1)www.bbc.com
2)www.businessinsider.com
3)www.cnn.com
4)www.footytube.com
5)www.nytimes.com
6)test: bit.ly/Akashk

-------------------------------------------
Task 5
-------------------------------------------
-->While task 3 already found the function which prints. Used Temp variable to store ip address and returned on call.
-->Included that  returned value while printing other stuff.
