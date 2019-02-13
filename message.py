from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def getFooter():
    res = ''
    with open("static/footer.html", 'r') as footer:
        for line in footer:
            res = res + line
    return res

def getBody(companyName):
    res = ''
    with open("static/body.html", 'r') as body:
        for line in body: 
            res = res + line.replace("%COMPANY_NAME%", companyName)
    return res

def getSubject(companyName):
    res = 'Sponsorship Invitation for %COMPANY_NAME% to Join ChariTeach 2019!'
    res = res.replace("%COMPANY_NAME%", companyName)
    return res

def createMessage(fromaddr, toaddr, ccaddr, companyName):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Cc'] = ccaddr
    msg['Subject'] = getSubject(companyName)
     
    body = getBody(companyName)
    html = getFooter()
    msg.attach(MIMEText(body, 'html'))

    filename = "charITeach Proposal.pdf"
    attachment = open(filename, "rb")
     
    asAttachment = MIMEBase('application', 'octet-stream')
    asAttachment.set_payload((attachment).read())
    encoders.encode_base64(asAttachment)
    asAttachment.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(MIMEText(html, "html"))

    msg.attach(asAttachment)
    return msg
