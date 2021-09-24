#!/usr/bin/env python3
import os, json
from templates import _wrapper, login_page

# html
print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World cmput404 class!</p>")

# Question 1
print("<p>Question 1:</p>")
print("<p>Environment Variables:</p>")
print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
print("<p></p>")

# Question 2
print("<p>Question 2:</p>")
for parameter in os.environ.keys():
	if (parameter == "QUERY_STRING"):
		print("<p>Query Parameter: %s</p>" %(os.environ[parameter]))

# Question 3
print("<p>Question 3:</p>")
for parameter in os.environ.keys():
	if (parameter == "HTTP_USER_AGENT"):
		print("<p>User Browser: %s</p>" %(os.environ[parameter]))

# Question 4
print("<p>Question 4:</p>")
print(login_page())