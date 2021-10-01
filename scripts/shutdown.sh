#! /bin/bash 

sudo shutdown +1 

ssh pi@192.168.88.244 sudo shutdown now

ssh pi@192.168.88.243 sudo shutdown now

ssh pi@192.168.88.233 sudo shutdown now

# "Raspbery Pi down "

ssh fedya@192.168.88.240 -S sudo shutdown now 
ssh fedya@192.168.88.247 -S sudo shutdown now 
ssh fedya@192.168.88.250 -S sudo shutdown now
ssh root@192.168.88.236 -S sudo shutdown now
ssh fedya@192.168.88.249 -S sudo shutdown now
ssh fedya@192.168.88.245 -S sudo shutdown now

# " Orange Pi down" 

ssh admin@192.168.88.2 system shutdown 
ssh admin@192.168.88.1 system shutdown 

# " Mikrotik down " 