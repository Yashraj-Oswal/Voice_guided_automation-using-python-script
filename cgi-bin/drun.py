#!/usr/bin/python3

print("content-type: text/html")
print()

print ("""
<html>
<head><title></title>
<style>
input[type=submit]{
  width: 15%;
  background-color:royalblue;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
<head>
<body>
<a href="http://172.20.10.4/dockerrun.html"><input type="submit" value="back"></a>
<br />
</body>
</html>
""")

print()

import subprocess as sp
import os
import cgi

y=cgi.FieldStorage()
osname = y.getvalue("t1")
ostype = y.getvalue("i")
cmd = "sudo docker run -i -t -d --name {0} {1}".format(osname,ostype)

output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]

if status == 0:
	print("Os named {0} launched successfully".format(osname))
else:
	print("some error: {}\n".format(out))

