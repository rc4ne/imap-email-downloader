from imap_tools import MailBox, AND
import os
import time

os.system("cls")
print("#### Using default output path to Desktop.. ")
PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
mailbox = MailBox('<MAILBOX URL>') # if dealing with gmail then imap.gmail.com
# else depends on organisation - webmail.organisation.com

mailbox.login('<USERNAME>', '<PASSWORD>', initial_folder='INBOX')
if mailbox:
    print("#### Login Successful...\n")

query = input("Enter subject to search for: ")
print('\n')
count = 0
for msg in mailbox.fetch(AND(subject=query)):
    count = count+1
    print("#### Processing mail number {}, recieved from {} ====\n".format(count,msg.from_))
    if not os.path.exists(PATH+"\\Email\\"+msg.uid):
        os.makedirs(PATH+"\\Email\\"+msg.uid)
    with open(PATH+'\\Email\\{}\\{}'.format(msg.uid,msg.uid+".txt"), 'w',encoding="utf-8") as f:
        f.write("FROM : {} \nSUBJECT: {} \nMESSAGE : {} \n".format(msg.from_,msg.subject,msg.text))
    for att in msg.attachments:
        with open(PATH+'\\Email\\{}\\{}'.format(msg.uid,att.filename.replace("\r\n","_")), 'wb') as f:
            f.write(att.payload)
mailbox.logout()