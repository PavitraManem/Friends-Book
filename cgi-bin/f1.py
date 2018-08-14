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
 <form action="writeslam.py" method="post"></br></br></br>
      </br>
         <font size="5" color="red">first name:</font><input type="text" name="fname" id="fname"/>
         <font size="5" color="red">last name:</font><input type="text" name="lname" id="lname"/></br>
     <font size="5" color="red">dob:</font>
				<input type="date" name="dob" id="dob"/></br></br>
		
		<font size="5" color="red">   email  id      :</font><input type="email" name="email" id="email"/></br></br>
	<font size="5" color="red">	   phone no:</font><input type="text" name="phno" id="phno"></br></br>
<font size="5" color="red">gender:</font><input type="radio" name="gender" id="gender" value="female"/>female
		        <input type="radio" name="gender" id="gender" value="male"/>male
				</br></br>
	
<font size="5" color="red">friends catagory:</font><select name="category" id="category">
					     <option value="school">school</option>
						 <option value="college">college</option>
						 <option value="office">office</option>
						 <option value="others">others</option>
                 </select></br></br>
<font size="5" color="red">favorite color:</font><input type="text" name="color" id="color"/></br></br>
<font size="5" color="red">favorite food:</font><input type="text" name="food" id="food"/></br></br>
<font size="5" color="red">favorite sport:</font><input type="text" name="sport" id="sport"/></br></br>
<font size="5" color="red">favorite hero:</font><input type="text" name="hero" id="hero"/></br></br>
<font size="5" color="red">favorite heroine:</font><input type="text" name="heroine" id="heroine"/></br></br>
<font size="5" color="red">favorite place:</font><input type="text" name="place" id="place"/></br></br>
<font size="5" color="red">your best friends:</font><input type="text" name="bestfrnds" id="bestfrnds"/></br></br>
<font size="5" color="red">your best views on me:</font><input type="text area" rows="20" columns="20" name="view" id="view"/></br></br>
<p class="login button">
					<input type="submit" value="submit" /></a>
					</p><vr>_________________________________________________________________________________________________________</vr>
					
 </form>
		

					</CENTER>
			</div>
		</div>
</body>
</html>''')
