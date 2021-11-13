
# smpt=smart mail transfer protocol
# Library for sending mail

import smtplib
import  ProcessText as pt
def sendmail(message):
    print(message
          )
    my_email = "paulkpraveen1@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    # to encrypt the mail we are sending we are using starttls
    connection.starttls()
    connection.login(user=my_email, password="Senjutest1$")
    connection.sendmail(from_addr=my_email,
                        to_addrs="paulkpraveen@gmail.com",
                        msg="Subject:Birthday\n\n"+message)
    connection.close()



import  datetime as dt

currentday=dt.datetime.today()
textmsg=pt.TextLoader()
if currentday.weekday()==5:
    sendmail(textmsg.loadtext("quotes.txt"))



