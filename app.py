import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify



try:
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "devrahul4798@gmail.com"
    receiver_email = "devrahul4798@gmail.com"
    password = input("Type your password and press enter:")
    message = "Hello Test with python"

    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    #server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
        # Print any error messages to stdout
        print(e)
finally:
        server.quit() 