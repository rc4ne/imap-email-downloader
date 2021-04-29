# imap-email-downloader
Through imap, downloads email message and attachments into folder named as email_code.
# Usage
For organisation based mailboxes:
-> Replace the URL with needed url, such as webmail.organisation.com

->Replace USERNAME , PASSWORD.

->pip install imap_tools

->Execute and search mail using subject.

->Folder will be formed on Desktop


For gmail:

-> Replace URL with imap.gmail.com

->Replace USERNAME, PASSWORD.

->pip install imap_tools

->Go to gmail.com > Settings gear at top right > See all Settings >Forwarding POP/IMAP >Enable IMAP.

->Go to https://myaccount.google.com/security turn on "Less Secure App Access" if feasible. (Warning: Potentially considered dangerous)

-> Execute the script


# Customizations
By default script uses "subject" to search for emails. To use some other way of accessing, please refer to https://pypi.org/project/imap-tools/#search-criteria \
Example: To download all the mails, mailbox.fetch(AND(all=True))


![imap](https://user-images.githubusercontent.com/83397936/116598237-37903500-a944-11eb-8f4f-78adcffa402e.JPG)



![output](https://user-images.githubusercontent.com/83397936/116598281-41199d00-a944-11eb-88df-d90df5608e2b.JPG)

