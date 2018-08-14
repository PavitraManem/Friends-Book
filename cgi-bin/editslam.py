import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
fname=form.getvalue('name')
import sqlite3 as s
conn=s.connect('Friend_Book.db')
d=conn.execute('''select * from slam where fname=?''',(fname,))
data=d.fetchall()


if(len(data)>=1):
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
			<CENTER>
 <form action="update.py" method="post"></br></br></br>
      <b>full name??<b></br>
         <font size="5" color="red">first name:</font><input type="text" name="fname" id="fname" value=''',data[0][0],'''/>
         <font size="5" color="red">last name:</font><input type="text" name="lname" id="lname" value=''',data[0][1],'''/></br>
         <font size="5" color="green">
				dob:</font><input type="text" name="dob" id="dob" value=''',data[0][2],'''/></br></br>
	
	<font size="5" color="red">	   email  id :</font><input type="text" name="email" id="email" value=''',data[0][3],'''/></br></br>
	<font size="5" color="red">	   phone no:</font><input type="text" name="phno" id="phno" value=''',data[0][4],'''></br></br>
<font size="5" color="red">	gender:</font><input type="text" name="gender" id="gender" value=''',data[0][5],'''/>
				</br></br>
	
    <font size="5" color="red">friends catagory:</font><input type name="category" id="category" value=''',data[0][6],'''></br></br>
<font size="5" color="red">favorite color:</font><input type="text" name="color" id="color" value=''',data[0][7],'''/></br></br>
<font size="5" color="red">favorite food:</font><input type="text" name="food" id="food" value=''',data[0][8],'''/></br></br>
<font size="5" color="red">favorite sport:</font><input type="text" name="sport" id="sport" value=''',data[0][9],'''/></br></br>
<font size="5" color="red">favorite hero:</font><input type="text" name="hero" id="hero" value=''',data[0][10],'''/></br></br>
<font size="5" color="red">favorite heroine:</font><input type="text" name="heroine" id="heroine" value=''',data[0][11],'''/></br></br>
<font size="5" color="red">favorite place:</font><input type="text" name="place" id="place" value=''',data[0][12],'''/></br></br>
<font size="5" color="red">your best friends:</font><input type="text" name="bestfrnds" id="bestfrnds" value=''',data[0][13],'''/></br></br>
<font size="5" color="red">your best views on me:</font><input type="text area" rows="20" columns="20" name="view" id="view"value=''',data[0][14],'''/></br></br>
<p class="login button">
					<input type="submit" value="submit" /></a>
					</p><vr>_________________________________________________________________________________________________________</vr>
					
 </form>
		

					</CENTER>
			</div>
		</div>
</body>
</html>

''')

conn.commit()
conn.close()
