import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

send_address = 'hoge@example.com'
password = 'hoge'

from_address = 'hoge@example.com'

subject = 'test subject'

address_dict = {
  'hoge01@example.com' : 'test01',
  'hoge02@example.com' : 'test02',
}

# SMTPサーバに接続
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()
smtpobj.login(send_address, password)

# メール作成
for address, name in address_dict.items():
  body_text = f'''{name}さま
'''
  msg = MIMEText(body_text)
  msg['Subject'] = subject
  msg['From'] = from_address
  msg['To'] = address
  msg['Date'] = formatdate()

  # 作成したメールを送信
  smtpobj.send_message(msg)

smtpobj.close()
