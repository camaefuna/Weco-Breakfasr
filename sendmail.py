import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("chijioke.amaefuna@gmail.com", "Spanner_2009")
 
msg = "testing"
server.sendmail("chijioke.amaefuna@gmail.com", "ddebisiolaniyan@gmail.com", msg)
server.quit()