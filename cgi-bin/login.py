import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
username=form.getvalue('username')
password=form.getvalue('password')
ad={'username':'admin','password':'12345'}
import sqlite3
conn=sqlite3.connect('Friend_Book.db')
d=conn.execute('''select * from reg where
username=? and password=?''',(username,password))
data=d.fetchall()
d1=conn.execute('''select * from slam''')
data1=d1.fetchall()
if(username==ad['username'] and password==ad['password']):
    print('Content-type:text/html')
    print()
    print('''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>ADMIN</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link rel="stylesheet" type="text/css" href="/style.css" />
</head>

<body>
	<div id="header">
		<span class="logo"><h1>Admin's Page</h1></span>			
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

				<h2> Admin Login Succesfully</h2>
				''')
    for i in data1:
        print('<form action="viewslam.py" method="post">')
        print('<input type="hidden" value=''',i[0],''' name="name"/>''')
        print('<input type="submit" value=''',i[0],'''/>''')
        print('</form>')
   
    print('''	
		</div>
		</CENTER>
	</div>
	</div>
	<div id="footer"></div>
</body>
</html>

    ''')
elif(len(data)==1):
     print('Content-type:text/html')
     print()
     print('''
       																																				<div class="inner_copy"><a href="http://www.greatdirectories.org/blog.html">blog directories</a><a href="http://www.bestfreetemplates.org/categories/blog/">blog templates</a></div>
		
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>login</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link rel="stylesheet" type="text/css" href="/style.css" />
</head>

<body>
	<div id="header">
		<span class="logo"><h1>FRIENDS BOOK</h1></span>			
			<div class="list">
			<ul id="menu">
				<li><a href="/login.html"><p><h3>Logout</h3></p></a></li>	
			</div>																																										<div class="inner_copy"><a href="http://www.greatdirectories.org/blog.html">blog directories</a><a href="http://www.bestfreetemplates.org/categories/blog/">blog templates</a></div>
		
		<img src="images/spacer.gif" alt="setalpm" width="120" height="120" border="0" usemap="#Map" class="rss" />
		<div id="container_demo" >
		<a class="hiddenanchor" id="toregister"></a>
		<a class="hiddenanchor" id="tologin"></a>
		<div id="wrapper">
			<CENTER>
			
       <big><big><center><h1><font size="25"> personal info</font></h1></center></big></big></br></br>
        <font face="ariel" size="16" color="green">
        <form action="f1.py" method="post">
        <input type="hidden" value=''',username,''' name="name"/>
        <input type="submit" value="writeslam"/></form></br>
        <form action="viewslam.py" method="post">
        <input type="hidden" value=''',username,''' name="name"/>
        <input type="submit" value="viewslam"/></form></br>
        <form action="editslam.py" method="post">
        <input type="hidden" value=''',username,''' name="name"/>
        <input type="submit" value="editslam"/>
                  
                        </font>
       </form>
		

					</CENTER>
			</div>
		</div>
</body>
</html>


''')

else:
    print('Content-type:text/html')
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

				<form  action="login.py" autocomplete="on"> </br></br></br>
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
					<a href="personal.html"><input type="submit" value="Login" onClick="validate()" /> </a>
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

