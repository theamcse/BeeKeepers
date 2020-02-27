#!C:\Python27\python.exe
import MySQLdb
print "Content-Type:text/html\n\n"

print"""
<html>
<head>
<title>Admin Activity</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
 <style>
 .ven{
	color:red;
 }</style>
</head>
<body bgcolor="cyan">"""
con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()
query = "select*from seekers"
cmd.execute(query)
res=cmd.fetchall()

print"""
<form>
<div style="width:100%;margin:0 auto;height:auto;min-height:500px;">
<table class="table";'>
"""
count=0
for row in res:
	count+=1
	if(count%2==0):
		print "<tr bgcolor=darkturquoise><td>",row[0],"</td><td>",row[1],"</td><td>",row[2],"</td><td>",row[3],"</td><td>",row[4],"</td><td>",row[5],"</td><td>",row[6],"</td><td><a href='delete.py?id=",row[4],"'>Delete</a></td></tr>"
	else:
		print "<tr bgcolor=lightblue><td>",row[0],"</td><td>",row[1],"</td><td>",row[2],"</td><td>",row[3],"</td><td>",row[4],"</td><td>",row[5],"</td><td>",row[6],"</td><td><a href='delete.py?id=",row[4],"'>Delete</a></td></tr>"	
print """</table>
</div>
</body>
</html>

"""