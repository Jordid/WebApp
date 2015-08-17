import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(user, password, asunto, mensaje, destinatario)
{
	gmail = smtplib.SMTP('smtp.gmail.com', 587)
	gmail.starttls()
	gmail.login(user, password)
	gmail.set_debuglevel(1)
	header = MIMEMultipart()
	header['Subject'] = asunto
	header['From'] = user
	header['To'] = destinatario
	mensaje = MIMEText("<p>"+mensaje+"</p>", 'html')
	header.attach(mensaje)
	gmail.sendmail(remitente,destinatario,header.as_string())
	gmail.quit()
}