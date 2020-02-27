#!C:\Python27\python.exe
import MySQLdb  
print "Content-Type:text/html\n\n"
import cgi
data=cgi.FieldStorage()
state=data.getvalue('state')
city=data.getvalue('city')
deptt=data.getvalue('deptt')
exp=data.getvalue('exp')
con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()
query="select name,gender,phone,exp from seekers where city='"+city+"' and state='"+state+"' and deptt='"+deptt+"' and exp='"+exp+"'"
cmd.execute(query)
res = cmd.fetchall()
print"""
<!DOCTYPE html>
<html lang="en">
<head>
<style>
body header p {
  display: inline;
}
#btn-get:hover{
  color: rgb(36, 79, 158);
}
#content-title {
  text-align: center;
  font-weight: 2rem;
  font-size: 5rem;
  font-family: 'Do Hyeon', sans-serif;
}
.footer-distributed{
  background-color: #292c2f;
  box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.12);
  box-sizing: border-box;
  width: 100%;
  text-align: left;
  font: bold 16px sans-serif;

  padding: 55px 50px;
}

.footer-distributed .footer-left,
.footer-distributed .footer-center,
.footer-distributed .footer-right{
  display: inline-block;
  vertical-align: top;
}

/* Footer left */

.footer-distributed .footer-left{
  width: 40%;
}

/* The company logo */

.footer-distributed h3{
  color:  #ffffff;
  font: normal 36px 'Cookie', cursive;
  margin: 0;
}

.footer-distributed h3 span{
  color:  #5383d3;
}

/* Footer links */

.footer-distributed .footer-links{
  color:  #ffffff;
  margin: 20px 0 12px;
  padding: 0;
}

.footer-distributed .footer-links a{
  display:inline-block;
  line-height: 1.8;
  text-decoration: none;
  color:  inherit;
}

.footer-distributed .footer-company-name{
  color:  #8f9296;
  font-size: 14px;
  font-weight: normal;
  margin: 0;
}

/* Footer Center */

.footer-distributed .footer-center{
  width: 35%;
}

.footer-distributed .footer-center i{
  background-color:  #33383b;
  color: #ffffff;
  font-size: 25px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  text-align: center;
  line-height: 42px;
  margin: 10px 15px;
  vertical-align: middle;
}

.footer-distributed .footer-center i.fa-envelope{
  font-size: 17px;
  line-height: 38px;
}

.footer-distributed .footer-center p{
  display: inline-block;
  color: #ffffff;
  vertical-align: middle;
  margin:0;
}

.footer-distributed .footer-center p span{
  display:block;
  font-weight: normal;
  font-size:14px;
  line-height:2;
}

.footer-distributed .footer-center p a{
  color:  #5383d3;
  text-decoration: none;;
}


/* Footer Right */

.footer-distributed .footer-right{
  width: 20%;
}

.footer-distributed .footer-company-about{
  line-height: 20px;
  color:  #92999f;
  font-size: 13px;
  font-weight: normal;
  margin: 0;
}

.footer-distributed .footer-company-about span{
  display: block;
  color:  #ffffff;
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 20px;
}

.footer-distributed .footer-icons{
  margin-top: 25px;
}

.footer-distributed .footer-icons a{
  display: inline-block;
  width: 35px;
  height: 35px;
  cursor: pointer;
  background-color:  #33383b;
  border-radius: 2px;

  font-size: 20px;
  color: #ffffff;
  text-align: center;
  line-height: 35px;

  margin-right: 3px;
  margin-bottom: 5px;
}
</style>
  <link rel="stylesheet" type="text/css" href="res.css">
  <title>Result</title>
  <meta charset="utf-8">
  <meta name="keywords" content="footer, address, phone, icons" />
  <link href="https://fonts.googleapis.com/css?family=Do+Hyeon" rel="stylesheet">
  <link rel="stylesheet" href="css/footer-distributed-with-address-and-phones.css">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="http://fonts.googleapis.com/css?family=Cookie" rel="stylesheet" type="text/css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center" style="margin-bottom:0;background: url(resbg.jpg) 50% 50%;font-family: 'Do Hyeon', sans-serif;">
  <h1 style="color:red">BeeKeepers</h1>
  <p>We care for you</p> 
</div>


<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <a class="navbar-brand" href="#">
"""
print "<span>You are looking for a : &nbsp;",deptt,"</span>"
print"""
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item" style="position:absolute;left:91%;top:0.5rem">
      <a class="nav-link" style="position:absolute;left:0rem;" href="ContactFrom/feedback.html">Feedback</a>
      </li>    
    </ul>
  </div>  
</nav>
"""
for row in res:
	print"""<div class="row"><div class="column"><div class="card"><img src="anonymous.png" height="150px" width="150px" style="margin:0 auto">"""
	print"<h3>",row[0],"</h3>","<p>Gender :&nbsp;",row[1],"</p>","<p>Phone Number :&nbsp;",row[2],"</p>","<p>Work Experience(in years) :&nbsp;",row[3],"</p>","</div>","</div>"
	print"</div>"
print"""
<footer class="footer-distributed" id="abtus">
    <a id="seven"></a>
            <div class="footer-left">

                <h3>Bee<span>Keepers</span></h3>
                <div class="footer-company-name">&copy; 2018 Copyright:
                    <a href="#"> BeeKeepers.com</a>
                </div>
            </div>

            <div class="footer-center">

                <div>
                    <i class="fa fa-map-marker"></i>
                    <p><span>Kanpur Uttar Pradesh</span>India</p>
                </div>

                <div>
                    <i class="fa fa-phone"></i>
                    <p>+91 9554015622</p>
                </div>

                <div>
                    <i class="fa fa-envelope"></i>
                    <p><a href="mailto:support@company.com">support@beekeepers.com</a></p>
                </div>

            </div>

            <div class="footer-right">

                <p class="footer-company-about">
                    <span>About BeeKeepers</span>
                    We are an organsiation providing solution to people's domestic issues.
                </p>
            </div>

        </footer>
</div>

</body>
</html>
"""
