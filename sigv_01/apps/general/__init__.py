import smtplib

from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

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
	    print("OKKK :D fine")
	    msgPdf.add_header('Content-ID', '<pdf1>') # if no cid, client like MAil.app (only one?) don't show the attachment
	    print("OKKK :D fine2")
	    msgPdf.add_header('Content-Disposition', 'attachment', filename=options.pdf)
	    print("OKKK :D fine2again")
	    msgPdf.add_header('Content-Disposition', 'inline', filename=options.pdf)

	#msgRoot.attach(msgHtml)
	#msgRoot.attach(msgImg)
	msgRoot.attach(msgPdf)
	print("OKKK :D fine or wellsdsds")

	# Send the message via local SMTP server.
	s = smtplib.SMTP('smtp.gmail.com', 587)
	print("OKKK :D fine ok")
	s.starttls()
	print("---"+user+"---")
	print("---"+password+"---")
	s.login(user, password)
	print("OKKK :D fine or wellsdsds")
	s.set_debuglevel(1)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(options.sender, options.recipient, msgRoot.as_string())
	#s.sendmail("akirevacacela@gmail.com", "estefaniavacacela@gmail.com", msgRoot.as_string())
	s.quit()