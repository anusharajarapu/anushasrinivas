import smtplib
from email.message import EmailMessage

def sendmail(to,subject,body):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('anusharajarapu66@gmail.com','wjdr mxye ehpb juuv')
    msg = EmailMessage()
    msg['From']='anusharajarapu66@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()


#sendmail('nagalakshmidandiboina@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# sendmail('manishankarupputholla@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# sendmail('shaik.nazeerbhasha7@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
 #print('mailsended')