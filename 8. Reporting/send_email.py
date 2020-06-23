from email.mime.text import MIMEText
import smtplib


def send_email(email, pothole, department, add, landmark, comment):
	from_email = "your email"
	from_password = "password"
	to_email = email

	subject = "Pothole Report"
	message="Hey there, your report is <strong>%s</strong>. <br> Thanks!" % (email)

	msg = MIMEText(message, 'html')
	msg['Subject'] = subject
	msg['To'] = to_email
	msg['From'] = from_email

	gmail=smtplib.SMTP('smtp.gmail.com',587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)
	gmail.send_message(msg)
