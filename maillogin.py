import smtplib
def maillogin():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("wecobreakfast@gmail.com","weco123#")
    msg = "Welcom to WECO"
    server.sendmail('momohododo08@gmail.com', 'ddebisiolaniyan@gmail.com',msg)
    server.quit()

def main():
    maillogin()

main()

