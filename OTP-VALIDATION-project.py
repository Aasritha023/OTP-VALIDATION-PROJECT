import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

otp = random.randint(1111,9999)
body=f"OTP for verification is {otp}"

msg = MIMEMultipart()
msg["From"] = "aasrithamodugaparapu@gmail.com"
msg["To"] = input("Enter Email Id: ")
msg["Subject"]= "OTP For Validation"
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("aasrithamodugaparapu@gmail.com", "anhd ackb vari itdh")

server.send_message(msg)
server.quit()

cotp = int(input("Enter OTP Received: "))
if otp == cotp:
    print("OTP Verification sucess")
else:
    print("Invalid OTP")
