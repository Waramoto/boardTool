#! /bin/bash 

sudo shutdown +1  # raspberry with screen

ssh pi@192.168.88.231 sudo shutdown now # raspberry 1.1 

ssh pi@192.168.88.222 sudo shutdown now # raspberry 2.1

ssh pi@192.168.88.243 sudo shutdown now # raspberry 3.1 

# "Raspbery Pi down "

ssh fedya@192.168.88.227 -S sudo shutdown now  # orange 1.2
ssh fedya@192.168.88.217 -S sudo shutdown now  # orange 1.3
ssh fedya@192.168.88.216 -S sudo shutdown now  # orange 2.2
ssh fedya@192.168.88.219 -S sudo shutdown now  # orange 2.3
ssh fedya@192.168.88.218 -S sudo shutdown now  # orange 3.2
ssh fedya@192.168.88.249 -S sudo shutdown now  # orange 3.3

# "Orange Pi down" 

ssh admin@192.168.88.2 system shutdown 
ssh admin@192.168.88.1 system shutdown 

# "Mikrotik down" 
