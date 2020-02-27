#!C:\Python27\python.exe
import MySQLdb
import cgi
print "Content-Type:text/html\n\n"
data=cgi.FieldStorage()
phone=data.getvalue('id').strip(' ')
#print id
con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()
query="delete from seekers where phone='"+phone+"'"
cmd.execute(query)
con.commit()
con.close()
print "<script>alert('Record Deleted');window.location.href='check.py';</script>"

