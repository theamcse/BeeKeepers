#!C:\Python27\python.exe
import MySQLdb
print "Content-Type:text/html\n\n"
import cgi
data=cgi.FieldStorage()
name=data.getvalue('name')
email=data.getvalue('email')
phone=data.getvalue('phone')
password=data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()
query="insert into panel values('"+name+"','"+email+"','"+phone+"','"+password+"')"
cmd.execute(query)
con.commit()
print "<script>alert('You are Successfully Registered');window.location.href='index.html';</script>"