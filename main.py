import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from email.utils import formataddr


app = Flask(__name__) 

@app.route('/', methods=['GET'])  
def index(): 
    return "<h1>Serai Shipping API</h1>"

@app.route('/send-email', methods=['GET', 'POST'])
def respond():
    data = request.get_json()
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "devrahul4798@gmail.com"
    receiver_email = "devrahul4798@gmail.com"
    password = "rahkavlit"
    name = data['name']
    email = data['email']
    contact = data['contact']
    content = data['data']

    # Create a secure SSL context
    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "Business Enquiry - Serai Shipping Services"
    message["From"] = formataddr(('Serai Shipping Business', 'serai@seraishipping.com'))
    message["To"] = receiver_email
    # message["Name"] = name

    # Create the plain-text and HTML version of your message
    text = f"""\
    Hi Team,
    There's a business enquiry for you! 
    
    Please find the enquiry details as mentioned below: 

    Name - {name}

    Email - {email} 

    Contact Number - {contact}
    
    Message - {content}
    
    Have a great day ahead!
    """
    html = f"""\
    <html>
    <body>
        <p>Hi Team, <br>
        There's a business enquiry for you from {name} with email - {email} and contact {contact} with message {message}<br>
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

# # Try to log in to server and send email

