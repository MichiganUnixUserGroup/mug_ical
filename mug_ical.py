import smtplib
import html
import arrow
from ics import Calendar
from urllib.request import urlopen
from email.mime.text import MIMEText
from textwrap import wrap


url = "http://www.mug.org/?page=CiviCRM&q=civicrm/event/ical&reset=1&list=1"
cal = Calendar(urlopen(url).read().decode('utf-8'))
days_out = 14

today = arrow.now()

for meeting in cal.events:
    delta = meeting.begin - today
    if delta.days == days_out:
        description = html.unescape(meeting.description)
        description_paragraphs = description.split('\n')
        mail_desc = ''
        for line in description_paragraphs:
            if len(line.strip()) == 0:
                mail_desc += '\n'
            else:
                line = wrap(line)
                mail_desc += '\n'.join(line)
                mail_desc += '\n'
        msg = MIMEText(mail_desc)
        msg['Subject'] = meeting.name
        msg['From'] = 'craig@decafbad.net'
        msg['To'] = 'announce@mug.org'
        s = smtplib.SMTP('localhost')
        s.sendmail('craig@decafbad.net', ['announce@mug.org'], msg.as_string())
