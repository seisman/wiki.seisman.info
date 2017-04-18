#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  筛选邮箱中指定的邮件并获取邮件正文
#
#  Author: Dongdong Tian @ USTC
#  Date:   2016-07-28
#

import email
from imaplib import IMAP4

host = 'mail.ustc.edu.cn'
port = '143'
username = 'username@mail.ustc.edu.cn'
password = 'password'

with IMAP4(host, port) as M:
    # 登录
    M.login(username, password)
    # 选择收件箱
    M.select('INBOX')
    # 筛选特定发件人的邮件
    type, data = M.search(None, '(FROM "autodrm@norsar.no")')
    # 对邮件做循环
    for num in data[0].split():
        # 获取邮件中的TEXT部分
        type, data = M.fetch(num, "(BODY[TEXT])")
        msg = email.message_from_bytes(data[0][1])
        print(msg)
