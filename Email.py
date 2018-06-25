"""The first step is to create an SMTP object, each object is used for connection
with one server."""

import smtplib
content = "Hi This Is Python Generated email..."
server = smtplib.SMTP('smtp.gmail.com', 587)   #  using Port no. 587
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("email", "password")

#Send the mail

server.sendmail("senderemail", "recieveremail", content)
server.close()