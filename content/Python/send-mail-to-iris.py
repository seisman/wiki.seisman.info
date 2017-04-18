#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Send emails to BREQ_FAST for waveform datas
#
#  Author:  Dongdong Tian @ USTC
#  Date:    2014-08-23
#
#  Hosts:
#  =========== ===================== ==========
#  Service     Host                  Port
#  =========== ===================== ==========
#  163         smtp.163.com          25
#  USTC mail   mail.ustc.edu.cn      25
#  Outlook     smtp-mail.outlook.com 587
#  =========== ===================== ==========
#
#  Revision History:
#    2014-08-23  Dongdong Tian  Initial Coding
#    2015-10-29  Dongdong Tian  Support outlook
#

import sys
import time
import random
from smtplib import SMTP
from email.mime.text import MIMEText

# Your email accout, password, SMTP server and port
sender = "username@163.com"
passwd = "xxxxxxxx"
host = "smtp.163.com"
port = 25

# BREQ_FAST mail address
recipient = 'breq_fast@iris.washington.edu'

if len(sys.argv) == 1:
    print("Usage:")
    print("  python %s mailfile ..." % sys.argv[0])
    sys.exit()
else:
    print("Total %d mails to send!" % len(sys.argv[1:]))

for mail in sys.argv[1:]:
    print("Sending %s ..." % mail)

    with open(mail) as f:
        msg = MIMEText(f.read())

    msg['From'] = sender
    msg['To'] = recipient

    with SMTP(host=host, port=port) as smtp:
        smtp.set_debuglevel(0)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, passwd)
        smtp.send_message(msg)

    time.sleep(random.uniform(3, 10))
