import cgi

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

print("Username is ",username)