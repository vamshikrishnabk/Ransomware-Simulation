import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path



# SMTP server configuration for Gmail
smtp_server = 'smtp.gmail.com'  
smtp_port = 587  
smtp_username = ''   # username
smtp_password = ''   # password 


# Requesting the recipient's email address from the user
recipient_email = input("Enter email address ")

# Path to the attachment file
attachment_path = r'/home/sn1318/Downloads/unnamed.png'


# Creating an EmailMessage object
email_message = EmailMessage()
email_message['From'] = smtp_username
email_message['To'] = recipient_email
email_message['Subject'] = 'Free Gift!!'


# Setting the body of the email
email_message.set_content('Thank you for participating in our monthly lottery. Please find the attached gift to claim your gift. You will need to click on the link to access the gift. \n https://drive.google.com/file/d/1ONknU4ALNpJBeDIgtxHQu61wQ7DdcRox/view?usp=drive_link') 



def attach_file_to_email(email_message, file_path):
    # Attach a file to an email message
    file_name = Path(file_path).name
    ctype = 'application/octet-stream'  
    maintype, subtype = ctype.split('/', 1)
    # Open the file to be attached
    with open(file_path, 'rb') as fp:
        email_message.add_attachment(fp.read(), maintype=maintype, subtype=subtype, filename=file_name)

# Attach the specified file to the email
attach_file_to_email(email_message, attachment_path)

try:
    # Sending the email through SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(smtp_username, smtp_password)   # Log in to the SMTP server
        server.send_message(email_message) # Send the email
        print('Email sent successfully!')
except Exception as e:
    print(f'An error occurred: {e}')
