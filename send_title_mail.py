from bs4 import BeautifulSoup
from requests import get
import smtplib , ssl 


url = 'https://www.kamupersoneli.net/kamu-personeli-alim-ilanlari/'

# get data 
data = get(url).text
#print(data)

title_write = open('titles.txt','w') 

#title 
bs_obj = BeautifulSoup(data, 'lxml')
main_obj = bs_obj.findAll('div',{'class':'hs-item-title hs-title-font'})
counter = 0 
for title in main_obj:
    counter +=1 
    print(str(counter).ljust(3) , ":\t".rjust(3), title.string, file = title_write)
title_write.close()


with open('titles.txt','r') as rdfile:
    data = rdfile.readlines()
    data = ''.join(data)
    data = data.strip()
    TranslateTab = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
    newdata = data.translate(TranslateTab)
print(newdata)

import smtplib , ssl 

smtp_server = 'smtp.gmail.com'
port = 465

sender_email= '' # write your gmail adress here 
context = ssl.create_default_context()
password = '' # write your password here 


# ANCHOR: message body with subject
subject = 'KAMUPERSONELI.NET BASLIKLAR'
message_body = newdata
message = f'Subject: {subject}\n\n{message_body}'

#ANCHOR: MAIN OBJECT
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.ehlo()
    server.login(sender_email,password)
    
    #recevier list 
    #put your adress here 
    receiverlist = [] 
    for receiver_email in receiverlist:
        server.sendmail(sender_email,receiver_email,message)

