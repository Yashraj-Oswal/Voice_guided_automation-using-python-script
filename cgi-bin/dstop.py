#!/usr/bin/python3

print("content-type: text/html")
print()

print("""
<html>
<head><title></title>
<style>
input[type=submit]{
  width: 10%;
  background-color:royalblue;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}
</style>
</head>
<body>
<a href="http://172.20.10.4/dockerstop.html"><input type="submit" value="back"></a>
</body>
</html>
""")

import subprocess as sp
import cgi

x = cgi.FieldStorage()

osname1 = x.getvalue("t2")
cmd="sudo docker stop {0}".format(osname1)

output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]

if status == 0:
	print("OS {} has been terminated..".format(osname1))
	print()
else:
	print("Something went wrong : {} \n".format(out))
	print()


