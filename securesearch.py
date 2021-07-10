import smtplib
import webbrowser
from better_profanity import profanity
def check(n):
    k=profanity.contains_profanity(n)
    return k
def email():
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.ehlo()
    conn.starttls()
    subject="Warning"
    name="Durga";
    conn.login('durgach2001@gmail.com','6304566534')
    conn.sendmail("durgach2001@gmail.com","chdurga2001@gmail.com","Subject: {}\n\nDear {}\n {}".format(subject,name,"This a warning message to you that you are search contains profanity word if this is repeating once again you will be punished"))
    conn.quit()
name=input("Enter your search")
if(check(name)):
    email()
else:
    webbrowser.open(name)
