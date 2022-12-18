from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'mahamatalhabib224@gmail.com'
email_password = 'azxzhciyezvxbnzk'

email_receiver = 'sitag75358@paxven.com'

subject = 'Trust yourself'
body = '''
You should trust yourself if you are a developer
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as s:
    s.login(email_sender, email_password)
    s.sendmail(email_sender, email_receiver, em.as_string())
