#!C:\Python27\python.exe
import MySQLdb
print "Content-Type:text/html\n\n"
import cgi
data=cgi.FieldStorage()
phone=data.getvalue('phone')
password=data.getvalue('pass')
deptt=data.getvalue('depart')
con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()



query="select phone,pass from panel where phone='"+phone+"' and pass='"+password+"'"
cmd.execute(query)
res = cmd.fetchall()
if res and deptt=="user":
	print"""
	<html>
    <head>
        <style type="text/css">

#mybtn,#mybtn2,#mybtn3,#mybtn4 {
  background-color: #C06C84;
  padding: .5em;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  border-radius: 6px;
  color: #fff;
  font-family: 'Oswald';
  font-size: 20px;
  text-decoration: none;
  border: none;
  font-family: 'Jua', sans-serif;
}

</style>  

<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css?family=Jua" rel="stylesheet">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" content="footer, address, phone, icons" />
    <link rel="stylesheet" href="css/demo.css">
    <link rel="stylesheet" href="css/footer-distributed-with-address-and-phones.css">
    
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">

    <link href="http://fonts.googleapis.com/css?family=Cookie" rel="stylesheet" type="text/css">


        <title>BeeKeepers | Get your problem solved</title>
        <script type="text/javascript" src="jquery-3.3.1.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" type="text/css" href="style.css">
        <link rel="stylesheet" type="text/css" href="codedude.ttf">
        <link href="https://fonts.googleapis.com/css?family=Do+Hyeon" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Kirang+Haerang" rel="stylesheet">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    </head>
    <body>
        <header>
        	<nav>
        		<div class="menu-icon" id="home">
        			<i class="fa fa-bars fa-2x"></i>
        		</div>
        		<div class="logo">
        			BeeKeepers
        		</div>
        		<div class="menu">
        			<ul>
        				<li><a href="#home" id="li_home">Home</a></li>
        				<li><a href="#abtus">About Us</a></li>
        				<li><a href="#serv">Our Services</a></li>
        				<li><a href="#seven">Contact Us</a></li>
        			</ul>
        		</div>
        	</nav>
        	<div id="textbox">
        		<h2>BeeKeepers</h2>
        		<span id="sub-text">We provide solution to your problems</span>
        		<a id="btn-get" href="ContactFrom/reg.html">Get a Job</a>
        	</div>
        	
        </header>
       
		<main class="main">
        	<div class="content" id="abtus">
                <p id="content-title">BeeKeepers<p>
                <p id="content-subtitle">-Our Story-<p>
        		<p>
        			We are a team of 5 members provoding the website solutions to any organisation, business, community, University or School etc.
        		</p>
        		<p>
        			CodeDude was established in 2018 and is based in Lucknow, Uttar Pradesh, India.
        		</p>
        		<p>
        			The burning of coal and wood, and the presence of many horses in concentrated areas made the cities the primary sources of pollution. The Industrial Revolution brought an infusion of untreated chemicals and wastes into local streams that served as the water supply. King Edward I of England banned the burning of sea-coal by proclamation in London in 1272, after its smoke became a problem
        		</p>
        	</div>
            <a id="serv"></a>
            <div class="content2">
                <p id="services--title">Our Services</p>

<!--Flippers_Start-->

        <div class="maincontainer">

              <div class="thecard">
                <div class="first">    
            </div>
                <div class="thefront"></div>

                <div class="theback"><h1></h1><p> </p>
                    <button id="myBtn">Get a Plumber</button></div>

              </div>
            
        </div>
              
        <div class="maincontainer">

              <div class="thecard">
                <div class="second"> </div>
                <div class="thefront"></div>

                <div class="theback"><h1></h1><p> </p>
                    <button id="myBtn2">Get an Electrician</button></div>

              </div>
        </div>
                
           
              
        <div class="maincontainer">

              <div class="thecard">
                <div class="third"></div>
                <div class="thefront"></div>

                <div class="theback"><h1></h1><p> </p>
                    <button id="myBtn3">Get a Maid</button></div>

              </div>
                   
        </div>

              
        <div class="maincontainer">

                <div class="thecard"> 
                <div class="forth"></div>
                <div class="thefront"></div>
                <div class="theback"><h1></h1><p> </p>
                <button id="myBtn4">Any Other</button></div>
                </div>

        </div>

<!--Flippers_end-->

            </div>
   
        </main>
        
<!-- Footer 1 -->

<footer class="footer-distributed">
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

        <!-- Footer 2 -->
		
		<footer class="page-footer font-small special-color-dark pt-4">

			<!-- Footer Elements -->
			<div class="container">

			<!-- Social buttons -->
			<ul class="list-unstyled list-inline text-center">
				<li class="list-inline-item">
					<a href="#" class="btn-floating btn-fb mx-1">
					<i class="fa fa-facebook"> </i>
					</a>
				</li>
				<li class="list-inline-item">
					<a href="#"  class="btn-floating btn-tw mx-1">
				<i class="fa fa-twitter"> </i>
				</a>
			</li>
        <li class="list-inline-item">
          <a href="#"  class="btn-floating btn-gplus mx-1">
            <i class="fa fa-google-plus"> </i>
          </a>
        </li>
        <li class="list-inline-item">
          <a href="#"  class="btn-floating btn-li mx-1">
            <i class="fa fa-linkedin"> </i>
          </a>
        </li>
        <li class="list-inline-item">
          <a href="#"  class="btn-floating btn-dribbble mx-1">
            <i class="fa fa-dribbble"> </i>
          </a>
        </li>
      </ul>
      <!-- Social buttons -->

    </div>
    <!-- Footer Elements -->

    <!-- Copyright -->
    <div class="footer-copyright text-center py-3">&copy; 2018 Copyright:
      <a href="#"> BeeKeepers.com</a>
    </div>
    <!-- Copyright -->

  </footer>
  <!-- Footer -->
        <script type="text/javascript">
        	//menu toogle button
        	$(document).ready(function() {
        		$(".menu-icon").on("click",function() {
        			$("nav ul").toggleClass("showing"); 
        		});
        	});
        	//scrolling effect
        	$(window).on("scroll",function() {
        		if($(window).scrollTop()) {
        			$('nav').addClass('black');
        		}
        		else {
        			$('nav').removeClass('black');
        		}
        	})
        </script>
        <script type="text/javascript">
        $(document).ready(function(){
          // Add smooth scrolling to all links
          $("a").on('click', function(event) {

            // Make sure this.hash has a value before overriding default behavior
            if (this.hash !== "") {
              // Prevent default anchor click behavior
              event.preventDefault();

              // Store hash
              var hash = this.hash;

              // Using jQuery's animate() method to add smooth page scroll
              // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
              $('html, body').animate({
                scrollTop: $(hash).offset().top
              }, 1200, function(){
           
                // Add hash (#) to URL when done scrolling (default click behavior)
                window.location.hash = hash;
              });
            } // End if
          });
        });
        
        </script>

        <!--Modal_1-->

        <div class="modal fade" id="myModal" role="dialog">
            <div class="modal-dialog">
      <!-- Modal content-->
                <div class="modal-content">
                    <div class="modal-header" style="padding:35px 50px;">
                        <h4><span class="glyphicon glyphicon-lock"></span>Enter your Preferences</h4>
                    </div>
                    <div class="modal-body" style="padding:40px 50px;">
                        <form role="form" action="res.py" method="post">
                            <input type="text" class="form-control" placeholder="Enter your State" name="state"><br>
                            <input type="text" class="form-control" placeholder="Your City" name="city"><br>
                            <input type="text" class="form-control" placeholder="Experience(in years)" name="exp">
                            <input type="hidden" value="plumber" class="form-control" name="deptt">
                            <p style="text-align: center; color: red;">Workers with higher experience will cost you more</p>
                            <button type="submit" class="btn btn-success btn-block">Submit</button>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="submit" class="btn btn-danger btn-default pull-left" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> Cancel</button>
                    </div>
                </div>
            </div>
        </div> 
        <!--mod_2-->
        <div class="modal fade" id="myModal2" role="dialog">
            <div class="modal-dialog">
      <!-- Modal content-->
                <div class="modal-content">
                    <div class="modal-header" style="padding:35px 50px;">
                        <h4><span class="glyphicon glyphicon-lock"></span>Enter your Preferences</h4>
                    </div>
                    <div class="modal-body" style="padding:40px 50px;">
                        <form role="form" action="res.py" method="post">
                            <input type="text" class="form-control" placeholder="Enter your State" name="state"><br>
                            <input type="text" class="form-control" placeholder="Your City" name="city"><br>
                            <input type="hidden" value="electrician" class="form-control" name="deptt">
                            <input type="text" class="form-control" placeholder="Experience(in years)" name="exp">
                            <p style="text-align: center; color: red;">Workers with higher experience will cost you more</p>
                            <button type="submit" class="btn btn-success btn-block">Submit</button>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="submit" class="btn btn-danger btn-default pull-left" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> Cancel</button>
                    </div>
                </div>
            </div>
        </div> 
        <!--mod_3-->
        <div class="modal fade" id="myModal3" role="dialog">
            <div class="modal-dialog">
      <!-- Modal content-->
                <div class="modal-content">
                    <div class="modal-header" style="padding:35px 50px;">
                        <h4><span class="glyphicon glyphicon-lock"></span>Enter your Preferences</h4>
                    </div>
                    <div class="modal-body" style="padding:40px 50px;">
                        <form role="form" action="res.py" method="post">
                            <input type="text" class="form-control" placeholder="Enter your State" name="state"><br>
                            <input type="text" class="form-control" placeholder="Your City" name="city"><br>
                            <input type="hidden" value="maid" class="form-control" name="deptt">
                            <input type="text" class="form-control" placeholder="Experience(in years)" name="exp">
                            <p style="text-align: center; color: red;">Workers with higher experience will cost you more</p>
                            <button type="submit" class="btn btn-success btn-block">Submit</button>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="submit" class="btn btn-danger btn-default pull-left" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> Cancel</button>
                    </div>
                </div>
            </div>
        </div>
        <!--mod_4-->
        <div class="modal fade" id="myModal4" role="dialog">
            <div class="modal-dialog">
      <!-- Modal content-->
                <div class="modal-content">
                    <div class="modal-header" style="padding:35px 50px;">
                        <h4><span class="glyphicon glyphicon-lock"></span>Enter your Preferences</h4>
                    </div>
                    <div class="modal-body" style="padding:40px 50px;">
                        <form role="form" action="res.py" method="post">
                            <input type="text" class="form-control" placeholder="What do you want?" name="deptt"><br>
                            <input type="text" class="form-control" placeholder="Enter your State" name="state"><br>
                            <input type="text" class="form-control" placeholder="Your City" name="city"><br>
                            <input type="text" class="form-control" placeholder="Experience(in years)" name="exp">
                            <p style="text-align: center; color: red;">Workers with higher experience will cost you more</p>
                            <button type="submit" class="btn btn-success btn-block">Submit</button>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="submit" class="btn btn-danger btn-default pull-left" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> Cancel</button>
                    </div>
                </div>
            </div>
        </div>
        <script>
        $(document).ready(function(){
            $("#myBtn").click(function(){
                $("#myModal").modal();
            });
        });
        </script>
       <script>
        $(document).ready(function(){
            $("#myBtn2").click(function(){
                $("#myModal2").modal();
            });
        });
        </script>
        <script>
        $(document).ready(function(){
            $("#myBtn3").click(function(){
                $("#myModal3").modal();
            });
        });
        </script>
        <script>
        $(document).ready(function(){
            $("#myBtn4").click(function(){
                $("#myModal4").modal();
            });
        });
        </script>
</div>
    </body>
</html>
"""
else:
	print "<script>alert('Wrong Credentials');window.location.href='index.html';</script>"