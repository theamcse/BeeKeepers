#!C:\Python27\python.exe
import MySQLdb
print "Content-Type:text/html\n\n"
import cgi
data=cgi.FieldStorage()

phone=data.getvalue('phone')

con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()
query="delete from seekers where phone = '"+phone+"'"
cmd.execute(query)
con.commit()
print "<script>alert('You are Successfully Deleted');window.location.href='showall.py';</script>"