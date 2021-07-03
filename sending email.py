import smtplib
conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()
try:
    conn.login('chdurga2001@gmail.com','6304566534')
    conn.sendmail("chdurga2001@gmail.com","durgach2001@gmail.com","Subject: hiii brooo\n\nDear Durga\n How are you")
except:
    print("sorry ! something wrong")
finally:
    conn.quit()
