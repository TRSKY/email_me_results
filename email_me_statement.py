import smtplib

from email.mime.text import MIMEText

def send_msg(msg, header=""):
	msg = MIMEText(str(msg) + "\n" + "Script print statement autosend.")

	if header=="":
		msg["Subject"] = "Script has terminated"
	else: 
		msg["Subject"] = header
	
  me = "Your new email address "
	you = "Your email address"

	msg["From"] = me
	msg["To"] = you

	server = smtplib.SMTP(host="smtp.gmail.com", port=587)
	server.starttls()
	server.login(me, 'your new email address password')


	server.sendmail(me, [you], msg.as_string())
	server.quit()

	print "\nmessage sent\n"
