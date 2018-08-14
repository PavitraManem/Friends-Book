import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
fname=form.getvalue('name')
import sqlite3 as s
conn=s.connect('Friend_Book.db')
d=conn.execute('''select * from slam where fname=?''',(fname,))
data=d.fetchall()

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

		<table>''')
for i in data:
    print('<tr>')
    
    print(''' </br></br><font size="5" color="red">first name:</font>''',i[0],'''</br></br>
         <font size="5" color="red">last name:</font>''',i[1],'''</br></br>
        <font size="5" color="green">dob:</font>''',i[2],'''</br></br>
       
	<font size="5" color="red">email  id:</font>''',i[3],'''</br></br>
       <font size="5" color="red">phone no:</font>''',i[4],'''</br></br>
       <font size="5" color="red">gender:</font>''',i[5],'''</br></br>
       <font size="5" color="red">friends catagory:</font>''',i[6],'''</br></br>
       <font size="5" color="red">favorite color:</font>''',i[7],'''</br></br>
       <font size="5" color="red">favorite food:</font>''',i[8],'''</br></br>
       <font size="5" color="red">favorite sport:</font>''',i[9],'''</br></br>
       <font size="5" color="red">favorite hero:</font>''',i[10],'''</br></br>
       <font size="5" color="red">favorite heroine:</font>''',i[11],'''</br></br>
       <font size="5" color="red">favorite place:</font>''',i[12],'''</br></br>
       <font size="5" color="red">your best friends:</font>''',i[13],'''</br></br>
       <font size="5" color="red">your best views on me:</font>''',i[14],'''</br></br>''')
    
    print('''</tr>''')
print('''</table></CENTER>
			</div>
		</div>
</body>
</html>

''')

conn.commit()
conn.close()
