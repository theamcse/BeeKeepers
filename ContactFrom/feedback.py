#!C:\Python27\python.exe
import MySQLdb
print "Content-Type:text/html\n\n"
import cgi
data=cgi.FieldStorage()
username=data.getvalue('username')
userphone=data.getvalue('userphone')
vendorname=data.getvalue('vendorname')
vendorphone=data.getvalue('vendorphone')
remark=data.getvalue('remark')
con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()
query="insert into feedback values('"+username+"','"+userphone+"','"+vendorname+"','"+vendorphone+"','"+remark+"')"
cmd.execute(query)
con.commit()
print "<script>alert('Your feedback is successfully Saved');window.location.href='../index.html';</script>"