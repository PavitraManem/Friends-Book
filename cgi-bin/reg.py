import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
firstname=form.getvalue('firstname')
lastname=form.getvalue('lastname')
username=form.getvalue('username')
password=form.getvalue('password')
cpassword=form.getvalue('cpassword')
email=form.getvalue('email')
phone=form.getvalue('phone')

import sqlite3 as s
conn=s.connect('Friend_Book.db')
conn.execute('insert into reg values(?,?,?,?,?,?,?)',(firstname,lastname,username,password,cpassword,email,phone))
print('context_type:text/html')
print()
print('''

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

<html>
<head>
<title>login</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link rel="stylesheet" type="text/css" href="/style.css" />
<script src="js/login.js"></script>
</head>

<body>
	<div id="header">
		<span class="logo"><h1>FRIENDS BOOK</h1></span>			
			<div class="list">
			<ul id="menu">
				<li><a href="/index.html"><p><h3>HOME</h3></p></a></li>	
			</div>																																										<div class="inner_copy"><a href="http://www.greatdirectories.org/blog.html">blog directories</a><a href="http://www.bestfreetemplates.org/categories/blog/">blog templates</a></div>
		
		<img src="images/spacer.gif" alt="setalpm" width="120" height="120" border="0" usemap="#Map" class="rss" />
		<div id="container_demo" >
		<a class="hiddenanchor" id="toregister"></a>
		<a class="hiddenanchor" id="tologin"></a>
		<div id="wrapper">
			<CENTER>

				<form  action="cgi-bin/login.py" autocomplete="on"> </br></br></br>
					<h2>Log in</h2> </br>
					<p> 
					<input id="username" name="username" required="required" type="text" placeholder="userid"/>
					</p>
					<p> 
					<input id="password" name="password" required="required" type="password" placeholder="password" /> 
					</p>
					<p class="keeplogin"> 
					</br>
					</p>
					<p class="login button"> 
					<a href="/personal.html"><input type="submit" value="Login" onClick="validate()" /> </a>
					</p>
					<p class="change_link">
						Not a member yet ?
						<a href="/signup.html" class="to_register">Join us</a>
					</p>
				</form></CENTER>
			</div>
		</div>
</body>
</html>



''')
conn.commit()
conn.close()
