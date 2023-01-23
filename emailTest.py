import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
conn.ehlo()
conn.starttls()
conn.login('username', 'password')
conn.sendmail('from', 'to', 'Subject: ... \n\n body \n\n-...')
conn.quit()
