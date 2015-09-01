import smtplib

from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

def enviar_email(user, password, asunto, mensaje, destinatario, pdf):
	"""gmail = smtplib.SMTP('smtp.gmail.com', 587)
	gmail.starttls()
	gmail.login(user, password)
	gmail.set_debuglevel(1)
	header = MIMEMultipart()
	header['Subject'] = asunto
	header['From'] = user
	header['To'] = destinatario
	mensaje = MIMEText("<p>hola que hace</p>", 'html')
	header.attach(mensaje)
	gmail.sendmail(remitente,destinatario,header.as_string())
	gmail.quit()"""
	"""print("Ok1")
	gmail = smtplib.SMTP('smtp.gmail.com', 587)
	gmail.starttls()
	print("Ok2")
	gmail.login(user, password)
	gmail.set_debuglevel(1)
	print("Ok3")
	header = MIMEMultipart('related')
	print("Ok4")
	header['Subject'] = asunto
	header['From'] = user
	print("Ok5")
	header['To'] = destinatario
	filename = "C:\Users\Erika\Desktop\tmp\ok.pdf"
	
	print("Ok5SSSSLLLLLLLLLLLLLLLLL")
	pdf = open(filename, 'rb').read()
	msgPdf = MIMEApplication(pdf, 'pdf') # pdf for exemple
	print("Ok5SSSS-----")
	#msgPdf.add_header('Content-ID', '<pdf1>') # if no cid, client like MAil.app (only one?) don't show the attachment
	#msgPdf.add_header('Content-Disposition', 'attachment', filename="options.pdf")
	#msgPdf.add_header('Content-Disposition', 'inline', filename="options.pdf")
	header.attach(msgPdf)
	# Read a file and encode it into base64 format
	#fo = open(filename, "rb")
	gmail.sendmail(user,destinatario,header.as_string())
	print("Ok8")
	gmail.quit()"""


def enviar_email_factura(user, password, asunto, destinatario, pdf, nombreDoc):
	print("asassssssssssssssss")
	parser = OptionParser()
	parser.add_option("-f", "--from", dest="sender", help="sender email address", default=user)
	parser.add_option("-t", "--to", dest="recipient", help="recipient email address", default=destinatario)
	parser.add_option("-s", "--subject", dest="subject", help="email subject", default=asunto)
	parser.add_option("-i", "--image", dest="image", help="image attachment", default=False)
	parser.add_option("-p", "--pdf", dest="pdf", help="pdf attachment", default=nombreDoc)

	print("asassssssssssssssss------------")
	(options, args) = parser.parse_args()

	# Create message container.
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = options.subject
	msgRoot['From'] = options.sender
	msgRoot['To'] = options.recipient
	print(options.recipient)

	# Create the body of the message.
	html = """\
	    <p>This is an inline image<br/>
	        <img src="cid:image1">
	    </p>
	"""

	# Record the MIME types.
	msgHtml = MIMEText(html, 'html')

	msgImg=""
	if options.image is not False:
	    img = open(options.image, 'rb').read()
	    msgImg = MIMEImage(img, 'png')
	    msgImg.add_header('Content-ID', '<image1>')
	    msgImg.add_header('Content-Disposition', 'inline', filename=options.image)

	msgPdf=""
	print("asas")
	if options.pdf is not False:
	    print("sds" + options.pdf)
	    #cd ..
	    #pdf = open(options.pdf, 'rb').read()
	    msgPdf = MIMEApplication(pdf, 'pdf') # pdf for exemple
	    msgPdf.add_header('Content-ID', '<pdf1>') # if no cid, client like MAil.app (only one?) don't show the attachment
	    msgPdf.add_header('Content-Disposition', 'attachment', filename=options.pdf)
	    msgPdf.add_header('Content-Disposition', 'inline', filename=options.pdf)

	#msgRoot.attach(msgHtml)
	#msgRoot.attach(msgImg)
	msgRoot.attach(msgPdf)

	# Send the message via local SMTP server.
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(user, password)
	s.set_debuglevel(1)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(options.sender, options.recipient, msgRoot.as_string())
	#s.sendmail("akirevacacela@gmail.com", "estefaniavacacela@gmail.com", msgRoot.as_string())
	s.quit()