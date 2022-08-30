import sys
from fast_mail_parser import parse_email, ParseError, PyAttachment
from datetime import datetime
from fpdf import FPDF


with open('/Volumes/TeamDrive/Nasrallah (0144)/Aufträge/22-005 Diverse Inkassoangelegenheiten/2022-08-30_SLanGegner_Re_ 47513731401.eml', 'r') as f:
    message_payload = f.read()

try:
    email = parse_email(message_payload)
except ParseError as e:
    print('Failure to parse email: ', e)
    sys.exit(1)

#print(email.subject)
#print(email.date.format('YYYY-MM-DDDD'))
#print(email.text_html)
#recipient =

sender = 'None'
recipient = 'None'
cc = 'None'
bcc = 'None'
Message_ID = 'None'

sender = email.headers.get('From')
subject = email.subject
text = email.headers.get('content"')
date_send = email.date
date_send = datetime.strptime(date_send, "%a, %d %b %Y %H:%M:%S %z")
date_str = datetime.strftime(date_send, "%Y-%m-%d %H:%M")
#recipient = email.headers.get('To')
#cc = email.headers.get('CC')
#bcc = email.headers.get('BCC')
#Message_ID = email.headers.get('Message-ID')
content = email.text_plain

print(date_send)
print(date_str)
print(content)

#
#for attachment in email.attachments:
#    #print(attachment.content)
    #print(attachment.filename.)
#    print(attachment.mimetype)


class PDF(FPDF):
    def lines(self):
        self.set_fill_color(32.0, 47.0, 250.0) # color for outer rectangle
        self.rect(5.0, 5.0, 200.0,287.0,'DF')
        self.set_fill_color(255, 255, 255) # color for inner rectangle
        self.rect(8.0, 8.0, 194.0,282.0,'FD')

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial')
pdf.text(10, 10, content)

pdf.output('macki.pdf','F')





