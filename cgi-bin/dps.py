#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

y=cgi.FieldStorage()
docker = y.getvalue("dps")
cmd1 = "sudo docker ps"

output1 = sp.getstatusoutput(cmd1)

status1 = output1[0]
out1 = output1[1]
print("Running Instance details \n")
print(out1)

