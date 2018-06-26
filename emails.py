from email.mime.text import MIMEText
msg = MIMEText('你好,Python','plain','utf-8')
#注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype
#传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

#输入Email地址和口令
from_addr = input('From:')
password = input('Password ')

#输入收件人的地址
to_addr = input('To: ')

#输入SMTP服务器地址
smtp_server = input('SMTP Server: ')

import smtplib

#默认端口号是25
server = smtplib.SMTP(smtp_server,25)
#打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
#login()方法用来登录SMTP服务器
server.login(from_addr,password)
#sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.sendmail(from_addr,[to_addr],msg.as_string())


