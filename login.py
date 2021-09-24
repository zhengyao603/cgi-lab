#!/usr/bin/env python3
import cgi, cgitb, os
from secret import username, password
from templates import _wrapper, secret_page, after_login_incorrect

# Create insatnce of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
user_name = form.getvalue('username')
pwd = form.getvalue('password')

# check if the username match password
if user_name == username and pwd == password:
	if not os.environ['HTTP_COOKIE']:
		print("Set-Cookie:Username = %s;" %(username))
		print("Set-Cookie:Password = %s;" %(password))
	print("Content-type:text/html\r\n\r\n")
	print("<html>")
	print("<head>")
	print("<title>Cookies Set - Second CGI Program</title>")
	print("</head>")
	print("<body>")
	print(secret_page(username, password))
	# Question 5
	print("<p>Question 5:</p>")
	print("<p>Cookies: %s</p>" %(os.environ['HTTP_COOKIE']))
	print("</body>")
	print("</html>")
else:
	print("Content-type:text/html\r\n\r\n")
	print("<html>")
	print("<head>")
	print("<title>Login Fail - Second CGI Program</title>")
	print("</head>")
	print("<body>")
	print(after_login_incorrect())
	print("</body>")
	print("</html>")