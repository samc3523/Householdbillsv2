import smtplib, ssl

username = 'householdbills.sc@gmail.com'
password = 'qtyrvtbqfqumhrgv'

def sendtext(number,msg):
    #password = ("qtyrvtbqfqumhrgv'")
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    #sender_email = "householdbills.sc@gmail.com"  # Enter your address
    receiver_email = number # Enter receiver address
    message = str(msg)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(username, password)
        server.sendmail(password, receiver_email, message)