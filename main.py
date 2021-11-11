
# smpt=smart mail transfer protocol
# Library for sending mail

import smtplib

def sendmail():
    my_email = "paulkpraveen1@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    # to encrypt the mail we are sending we are using starttls
    connection.starttls()
    connection.login(user=my_email, password="Senjutest1$")
    connection.sendmail(from_addr=my_email,
                        to_addrs="paulkpraveen@gmail.com",
                        msg="Subject:Birthday\n\nhello,praveen i wish you a nice")
    connection.close()

# sendmail()

import  datetime

date_of_birth=datetime.datetime(year=1991,month=5,day=13,hour=16,minute=30)
print(date_of_birth)


