import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
fname=form.getvalue('fname')
lname=form.getvalue('lname')
dob=form.getvalue('dob')
email=form.getvalue('email')
phno=form.getvalue('phno')
gender=form.getvalue('gender')
category=form.getvalue('category')
color=form.getvalue('color')
food=form.getvalue('food')
sport=form.getvalue('sport')
hero=form.getvalue('hero')
heroine=form.getvalue('heroine')
place=form.getvalue('place')
bestfrnds=form.getvalue('bestfrnds')
view=form.getvalue('view')

import sqlite3 as s
conn=s.connect('Friend_Book.db')
conn.execute('update slam set fname=?,lname=?,dob=?,email=?,phno=?,gender=?,category=?,color=?,food=?,sport=?,hero=?,heroine=?,place=?,bestfrnds=?,view=?',(fname,lname,dob,email,phno,gender,category,color,food,sport,hero,heroine,place,bestfrnds,view))

print('Content-type:text/html')
print()
print('''
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
			<CENTER></br></br></br></br></br></br>
 
<h1>data updated</h1>	

					</CENTER>
			</div>
		</div>
</body>
</html>


''')

conn.commit()
conn.close()
