from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Gholamreza Mohammadi"
message["to"] = "gmohammadi.iasbs@gmail.com"
message["subject"] = "This is a test"
body = template.substitute(name="Reza")
message.attach(MIMEText("body", "html"))
message.attach(MIMEImage(Path("Reza.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("gmohammadi.iasbs@gmail.com", "todayskyisblue1234")
    smtp.send_message(message)
    print("Sent...")
