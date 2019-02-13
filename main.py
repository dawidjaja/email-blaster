import sys
import smtplib
from config import getPassword
from message import createMessage

def main():
    fromaddr = "dalfred2000@gmail.com"
    cc = "marketing@nussucommit.com,chairperson@nussucommit.com,vicechairperson@nussucommit.com"
    
    names = [i.strip() for i in open("static/names.txt")]
    email = [i.strip() for i in open("static/email.txt")]
    assert(len(names) == len(email))
    # print(names)
    # print(email)

    start = 0
    if (len(sys.argv) != 1):
        start = int(sys.argv[1])
    for i in range(start, len(names)):
        print(i, names[i], email[i])
        companyName = names[i]
        toaddr = email[i]

        rcpt = cc.split(',') + [toaddr]

        msg = createMessage(fromaddr, toaddr, cc, companyName)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, getPassword())
        text = msg.as_string()
        server.sendmail(fromaddr, rcpt, text)
        server.quit()

if __name__ == '__main__':
    main()
