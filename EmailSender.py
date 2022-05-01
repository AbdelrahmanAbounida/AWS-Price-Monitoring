from re import sub
import smtplib
import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from matplotlib.pyplot import getp
from priceTracker import MOBILE_URL , getPrice
from email.message import EmailMessage
 
GMAIL_ADDRESS = os.environ.get('myGmail')
GMAIL_PASSWORD = os.environ.get('myGmailPassword')



########################## Create Message ###############################
def create_msg(subject,body,FROM,TO):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg.set_content(body)
    msg['From'] = FROM
    msg['To'] = ','.join(TO) # get a list 

    return msg


########################## Send Email ###############################
# Email parts
FROM = 'abdelrahmanaboneda@gmail.com'
TO = ["abdelrahmanaboneda@gmail.com"] # must be a list
subject = "Price's gone down"


def sendEmail(price):
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.ehlo() # Identify myself
        server.starttls() #Put the SMTP connection in TLS (Transport Layer Security) mode
        server.ehlo() # should be called again, acc.to documentation
        server.login(GMAIL_ADDRESS,GMAIL_PASSWORD)

        body = f"Congrats! The Mobile Price Has Dropped To {price} For more new information: \n go to: {MOBILE_URL}"
        msg = create_msg(subject,body,FROM,TO)# Main Message   
        #smtp.sendmail(FROM,TO,msg) #send email
        server.send_message(msg)
        print("Email Has Been Sent !!!")

        server.quit()

        '''
        ## using local server
        server = smtplib.SMTP('localhost')
        server.sendmail(FROM,TO,msg)
        server.quit()
        '''

########################## Track Price ###############################

mobile_price = getPrice(MOBILE_URL)

while True:
    mobile_price = getPrice(MOBILE_URL)
    if(float(mobile_price.split('.')[0]) < 200):
        print("Congrats! The price went down...")
        sendEmail(mobile_price)
        break